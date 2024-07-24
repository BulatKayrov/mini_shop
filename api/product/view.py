from fastapi import APIRouter, Depends

from api.product.model import ProductModel
from .schema import ProductCreate
from ..auth.utils import get_current_user

router = APIRouter(prefix='/product', tags=['Product'])


@router.get('/')
async def get_all_products():
    return await ProductModel.find_all()


@router.post('/')
async def create_product(product: ProductCreate, user=Depends(get_current_user)):
    if user.is_admin:
        return await ProductModel.create(**product.model_dump())
    return {'message': 'You are not allowed to create products'}
