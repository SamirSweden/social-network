from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
import crud
from fastapi import FastAPI , Depends , Form , HTTPException,Request
from fastapi.responses import HTMLResponse , RedirectResponse , JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import  Session
from models import Base
from schemas import UserCreate , PostCreate
from database import SessionLocal , engine
import secrets


from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user # Импортируем оригинальную функцию
from fastapi import status
from datetime import timedelta
import models

Base.metadata.create_all(bind=engine)

app  = FastAPI()
SECRET_KEY = secrets.token_urlsafe(32)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user_from_session(request: Request, db: Session = Depends(get_db)):
    token = request.session.get('access_token')
    if not token:
        # Если токена нет, пользователь не авторизован
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        from jose import JWTError, jwt
        from auth import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    current_user = None
    return templates.TemplateResponse("home.html" , {"request" : request,"posts" : posts, "current_user": current_user})

@app.get("/register" , response_class=HTMLResponse)
def show_register_form(request: Request):
    return templates.TemplateResponse("register.html" , {"request": request})


@app.post("/register")
def register_user(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_by_username(db, username=username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    crud.create_user(db=db, username=username, email=email, password=password)
    return RedirectResponse(url="/login", status_code=303)

@app.get("/panel", response_class=HTMLResponse)
def user_panel(request: Request, current_user: models.User = Depends(get_current_user_from_session), db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return templates.TemplateResponse("panel.html", {"request": request, "current_user": current_user, "posts": posts})

@app.get("/logout", response_class=HTMLResponse)
def logout(request: Request):
    # Удаляем токен из сессии
    request.session.pop('access_token', None)
    # Перенаправляем на главную
    return RedirectResponse(url="/", status_code=303)

@app.get("/login", response_class=HTMLResponse)
def show_login_form(request: Request):
    return templates.TemplateResponse("login.html" , {"request": request})

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/token")
def login(login_data: LoginData, db: Session = Depends(get_db), request: Request = None):
    user = authenticate_user(db, login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    request.session['access_token'] = access_token
    return {"msg":"login successful" , "redirect_url": "/panel"}

# @app.post("/token")
# def login(form_data: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#
#     return {"access_token": access_token, "token_type": "bearer", "redirect_url": "/panel"}
