from datetime import datetime
import sqlite3

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
    conteudo = f"Nome: {nome}\nDescricao: {descricao}\nEstoque: {estoque}\nPreco: {preco}\nCategoria: {categoria}"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

def obter_conexao():
    return sqlite3.connect("dados.db")
