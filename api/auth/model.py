from sqlalchemy import select, Result
from models import User, session_scope


class UserModel:

    @classmethod
    async def create(cls, password, email, image):
        async with session_scope() as session:
            instance = User(
                email=email,
                password=password,
                image=image
            )
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    @classmethod
    async def find_by_email(cls, email: str):
        async with session_scope() as session:
            stmt = select(User).where(User.email == email)
            result: Result = await session.execute(stmt)
            return result.scalar_one_or_none()
