from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "pages" / "index.html")


@app.get("/register_now")
async def register_now_page(request: Request):
    return templates.TemplateResponse(request=request, name="register_now.html")


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


app.mount(
    "/",
    StaticFiles(directory=BASE_DIR / "pages"),
    name="copied_pages"
)
