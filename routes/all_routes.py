from fastapi import APIRouter,File, Depends,Path, HTTPException,UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse
from controllers.get import list_files
from controllers.upload import save_file
from controllers.download import check_file_exists
from controllers.download_all import download_all_files
from controllers.delete import delete_file
from controllers.delete_all import delete_all_files
from typing import List
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/get")
async def get_files():
    return await list_files()

@router.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    if not files:
        return JSONResponse(content={"error": "No files selected for upload"}, status_code=400)

    upload_responses = [await save_file(file) for file in files]
    return upload_responses

@router.get("/download/{filename}")
async def download_file(filename: str):
    return await check_file_exists(filename)

@router.get("/download-all")
async def download_all():
    try:
        return await download_all_files()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete/{filename}")
async def delete(filename: str):
    try:
        return await delete_file(filename)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/delete-all")
async def delete_all():
    try:
        return delete_all_files()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# app = APIRouter()
# app.include_router(router, prefix='/api', tags=["Search"])