from fastapi import FastAPI, APIRouter, HTTPException
import os
import shutil

UPLOAD_FOLDER = "uploads"

async def delete_file(filename: str):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                # Delete folder and its contents
                shutil.rmtree(file_path)
            else:
                # Delete file
                os.remove(file_path)
                
            return {"message": f"{filename} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="File or folder not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





