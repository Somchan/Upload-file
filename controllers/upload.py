# from fastapi import UploadFile, HTTPException
# from pathlib import Path
# import shutil
# # Define the path to the uploads folder
# UPLOAD_FOLDER = "uploads"

# async def save_file(file: UploadFile):
#     try:
#         file_path = Path(UPLOAD_FOLDER) / file.filename
#         with file_path.open("wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
#         return {"file": file.filename, "message": "Uploaded successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# app = FastAPI()

# # Include the router in the app
# app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
###########################################################

from fastapi import UploadFile, HTTPException
from pathlib import Path
import shutil
import logging
# Define the path to the uploads folder
UPLOAD_FOLDER = "uploads"

async def save_file(file: UploadFile):
    try:
        file_path = Path(UPLOAD_FOLDER) / file.filename

        # Check if the file with the same name already exists
        file_name_exists = file_path.is_file()

        if file_name_exists:
            # If file with the same name exists, rename the file
            new_filename = generate_new_filename(file_path)
            file_path = Path(UPLOAD_FOLDER) / new_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"file": file_path.name, "message": "Uploaded successfully"}

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

    except PermissionError as e:
        raise HTTPException(status_code=403, detail=f"Permission error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def generate_new_filename(file_path):
    """
    Generate a new filename by appending a number to the filename if it already exists.
    """
    base_name = file_path.stem  # File name without extension
    extension = file_path.suffix  # File extension including the dot

    count = 1
    while (new_path := Path(UPLOAD_FOLDER) / f"{base_name}_{count}{extension}").exists():
        count += 1

    return f"{base_name}_{count}{extension}"
