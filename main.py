from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from models.produto_model import Produto
from repositories import produto_repo
from util import salvar_cadastro

produto_repo.criar_tabela()

app = FastAPI()
templates = Jinja2Templates(directory="templates") # adicionando comentário para commit

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
    produto = Produto(None, nome, descricao, estoque, preco, categoria)
    produto = produto_repo.inserir(produto)
    if produto:
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        return RedirectResponse("/cadastro", 303)
    
@app.get("/cadastro_recebido")
def get_contato(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)