from fastapi import FastAPI, APIRouter, HTTPException
from pathlib import Path
from starlette.responses import FileResponse
import os
import shutil

app = FastAPI()
router = APIRouter()

# Define the path to the uploads folder
UPLOAD_FOLDER = "uploads"
ZIP_FILENAME = "uploads.zip"

def create_zip(zip_filename: str, source_folder: str):
    try:
        # Remove the old zip file if it exists
        if os.path.exists(zip_filename):
            os.remove(zip_filename)

        # Create the new zip file
        shutil.make_archive(zip_filename[:-4], 'zip', source_folder)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def check_folder_empty(folder: str):
    return not os.listdir(folder)

async def download_all_files():
    folder = UPLOAD_FOLDER

    if not os.path.exists(folder) or check_folder_empty(folder):
        raise HTTPException(status_code=404, detail="No files to download.")

    create_zip(ZIP_FILENAME, folder)

    return FileResponse(ZIP_FILENAME, headers={"Content-Disposition": f"attachment; filename={ZIP_FILENAME}"})
