import pyodbc

def conectar():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"  # ou o nome do seu servidor
        "DATABASE=TesteFastAPI;"
        "UID=usuario_fastapi;"
        "PWD=Senha123!;"
    )