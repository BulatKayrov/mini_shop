from fastapi import APIRouter, Depends, HTTPException, status

from api.category.model import CategoryModel
from .schema import CategoryCreate
from ..auth.utils import get_current_user

router = APIRouter(prefix="/category", tags=['Category'])


@router.get("/all")
async def get_all_categories():
    return await CategoryModel.find_all()


@router.post('/create')
async def create_category(category: CategoryCreate, user=Depends(get_current_user)):
    if user.is_admin:
        return await CategoryModel.create(**category.model_dump())
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Forbidden')


@router.delete('/delete/{pk}')
async def delete_category(pk: int, user=Depends(get_current_user)):
    if user.is_admin:
        await CategoryModel.delete(pk=pk)
        return {'status': 'success'}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Forbidden')
