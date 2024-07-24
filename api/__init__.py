__all__ = [
    'router'
]

from fastapi import APIRouter

from .auth.view import router as auth_router
from .category.view import router as category_router
from .product.view import router as product_router

router = APIRouter(prefix='/api')

router.include_router(auth_router)
router.include_router(category_router)
router.include_router(product_router)
