# from fastapi import FastAPI, APIRouter, HTTPException
# from pathlib import Path

# router = APIRouter()

# # Define the path to the uploads folder
# UPLOAD_FOLDER = "uploads"

# async def check_file_exists(filename: str):
#     try:
#         file_path = Path(UPLOAD_FOLDER) / filename
#         if file_path.is_file():
#             return {"status": "done", "message": "File download successful"}
#         else:
#             raise HTTPException(status_code=404, detail="File not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error: " + str(e))

from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import zipfile

router = APIRouter()

# Define the path to the uploads folder
UPLOAD_FOLDER = "uploads"

async def check_file_exists(filename: str):
    try:
        file_path = Path(UPLOAD_FOLDER) / filename
        if file_path.is_file():
            return FileResponse(file_path)
        elif file_path.is_dir():
            folder_zip = Path(UPLOAD_FOLDER) / (filename + ".zip")
            shutil.make_archive(folder_zip.with_suffix(""), 'zip', file_path)
            return FileResponse(folder_zip)
        else:
            raise HTTPException(status_code=404, detail="File or folder not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: " + str(e))

async def download_file(filename: str):
    file_path = Path(UPLOAD_FOLDER) / filename
    if file_path.is_file():
        return FileResponse(file_path)
    elif file_path.is_dir():
        folder_zip = Path(UPLOAD_FOLDER) / (filename + ".zip")
        shutil.make_archive(folder_zip.with_suffix(""), 'zip', file_path)
        return FileResponse(folder_zip)
    else:
        raise HTTPException(status_code=404, detail="File or folder not found")