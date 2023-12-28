from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from werkzeug.utils import secure_filename
import os
from watchgod import run_process
import queue
import uvicorn
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from routes.all_routes import router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
HTML_FOLDER = "html"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get from folder html the index.html file
@app.get("/")
async def read_root():
    return FileResponse(Path(HTML_FOLDER) / "index.html", media_type="text/html")

app.include_router(router)

# Mount the "JS" directory at "/JS" for static files
app.mount("/JS", StaticFiles(directory="JS"), name="JS")

def main():
    host_server = os.getenv("HOST_SERVER")
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host=host_server, port=port)

if __name__ == "__main__":
    run_process('.', main)
