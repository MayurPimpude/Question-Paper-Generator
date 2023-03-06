from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html',{"request": request})

@app.get("/input", response_class=HTMLResponse)
async def input(request: Request):
    return templates.TemplateResponse('input.html',{"request": request})

@app.post("/input")
async def input1(tex: str = Form(...)):
    print(tex)
    #return templates.TemplateResponse('input.html',{"request": Request})
    return tex

# from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# app = FastAPI()
# templates = Jinja2Templates(directory='templates')

# @app.post('/disable')
# def disable_cat(cat_name: str = Form(...)):
#     return f'{cat_name}'

# @app.get('/', response_class=HTMLResponse)
# def main(request: Request):
#     return templates.TemplateResponse('index2.html', {'request': request})