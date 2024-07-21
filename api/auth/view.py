from fastapi import APIRouter, Depends
from fastapi.responses import Response

from tasks.task import send_message
from .model import UserModel
from .schema import UserCreate, UserResponse, UserLogin
from .utils import authenticate_user, create_access_token, get_current_user, get_password_hash

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register', response_model=UserResponse)
async def register_user(user: UserCreate):
    password = get_password_hash(password=user.password)
    send_message.delay(str(user.email))
    return await UserModel.create(email=user.email, password=password, image=user.image)


@router.post('/login')
async def login_user(user: UserLogin, response: Response):
    _user = authenticate_user(instance=UserModel, email=user.email, password=user.password)
    if _user:
        token = create_access_token(data={'sub': user.email})
        response.set_cookie(key='token', value=token, httponly=True)
        return {'access_token': token}


@router.get('/logout')
async def logout_user(response: Response):
    response.delete_cookie(key='token')
    return {'status': 200}


@router.get('/status')
async def status_user(user=Depends(get_current_user)):
    if user:
        return {'data': user}
    return {'status': 401}
