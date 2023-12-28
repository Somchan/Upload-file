from fastapi import FastAPI, APIRouter, HTTPException
import os
import shutil


app = FastAPI()


UPLOAD_FOLDER = "uploads"

def delete_all_files():
    try:
        folder = UPLOAD_FOLDER
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Use shutil.rmtree to remove non-empty directories
        return {"message": "All files and directories deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))