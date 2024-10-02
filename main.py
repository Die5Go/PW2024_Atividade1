from datetime import datetime
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

NOME_PASTA_STATIC="static/"
NOME_PASTA_CADASTROS="dados/cadastros/"

def ler_static(nome_arquivo: str) -> str:
    caminho_arquivo_html = f"{NOME_PASTA_STATIC}{nome_arquivo}.html"
    with open(caminho_arquivo_html, "r", encoding="utf-8") as arquivo:
        conteudo_html = arquivo.read()
    return conteudo_html

def salvar_cadastro(nome, descricao, estoque, preco, categoria):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{NOME_PASTA_CADASTROS}cadastro_{agora}.txt"
    conteudo = f"Nome: {nome}\nDescrição: {descricao}\nEstoque: {estoque}\nPreço: {preco}\nCategoria: {categoria}"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_contato(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...), 
    categoria: str = Form(...)):
    salvar_cadastro(nome, descricao, estoque, preco, categoria)
    return RedirectResponse("/", 303)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)