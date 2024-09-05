from fastapi import APIRouter, UploadFile

from domain.file_processor import FileProcessor

router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()

@router.post("/upload_file/")
async def upload_file(file: UploadFile= File(...))


@router.post("/file/add_data")
async def add_data():
    return {"message": "Dado adicionado com sucesso"}

@router.post("/file/delete_data")
async def delete_data():
    return {"message": "Dado removido com sucesso"}

@router.post("/file/list_files")
async def list_files():
    return {"message": "Lista de dados"}