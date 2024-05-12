from fastapi import FastAPI, HTTPException

from src.controller.user import c_get_user, c_delete_user, c_update_user, c_create_user

from src.models.user import User

app = FastAPI()


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário Não Encontrado")
    return db_user



@app.post('/users')
async def create_user(user: User):
    db_user = await c_get_user(user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="O usuário já existe")
    await c_create_user(user)
    return {"message": "Deu bom usuario criado com sucesso!"}




@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="O usuário não existe")
    await c_delete_user(user_id)
    return {"message": "Usuario deletado!"}



@app.put('/users/{user_id}')
async def usuarios(user_id: int, user: User):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=200, detail="O usuário não existe")
    await c_update_user(user.id, user.name, user.area, user.job_description, user.role, user.salary, user.is_active, user.last_evaluation)
    return {"message": "Usuario alterado!"}

