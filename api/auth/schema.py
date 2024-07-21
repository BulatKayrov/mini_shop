from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str
    image: str


class UserResponse(UserBase):
    pk: int
    is_admin: bool
    is_active: bool


class UserCreate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str

