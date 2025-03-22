from fastapi import APIRouter



router = APIRouter(prefix='/users', 
                   tags=['User Management'])

@router.post('/find-user', summary='Search User')
async def search_user():
  ...