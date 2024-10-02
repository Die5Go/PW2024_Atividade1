from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

NOME_PASTA_STATIC="static/"

def ler_static(nome_arquivo: str) -> str:
    caminho_arquivo_html = f"{NOME_PASTA_STATIC}{nome_arquivo}.html"
    with open(caminho_arquivo_html, "r", encoding="utf-8") as arquivo:
        conteudo_html = arquivo.read()
    return conteudo_html

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)