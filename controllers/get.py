from fastapi import APIRouter, Depends,Path, HTTPException
import os

UPLOAD_FOLDER = "uploads"

async def list_files():
    try:
        folder = UPLOAD_FOLDER
        files = os.listdir(folder)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))