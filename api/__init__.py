__all__ = [
    'router'
]

from fastapi import APIRouter

from .auth.view import router as auth_router

router = APIRouter(prefix='/api')

router.include_router(auth_router)
