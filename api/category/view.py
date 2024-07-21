from fastapi import APIRouter

from api.category.model import CategoryModel
from .schema import CategoryCreate

router = APIRouter(prefix="/category", tags=['Category'])


@router.get("/all")
async def get_all_categories():
    return await CategoryModel.find_all()


@router.post('/create')
async def create_category(category: CategoryCreate):
    return await CategoryModel.create(**category.model_dump())


@router.delete('/delete/{pk}')
async def delete_category(pk: int):
    await CategoryModel.delete(pk=pk)
    return {'status': 'success'}
