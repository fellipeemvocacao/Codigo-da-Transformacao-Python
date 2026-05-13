import sqlite3
def executar_consulta(descricao, query, parametros=()):
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    cursor.execute(query, parametros)
    resultados = cursor.fetchall()
    conn.close()
    
    print(f"\n--- {descricao} ---")
    if resultados:
        for linha in resultados:
            print(linha)
    else:
        print("Nenhum registro encontrado.")
    print("-" * (len(descricao) + 8))
executar_consulta(
    "Clientes com nome começando em 'A'",
    "SELECT * FROM Clientes WHERE nome LIKE 'A%'"
)
executar_consulta(
    "Clientes que usam Gmail",
    "SELECT * FROM Clientes WHERE email LIKE '%@gmail.com'"
)
executar_consulta(
    "Clientes em ordem Z-A",
    "SELECT * FROM Clientes ORDER BY nome DESC"
)
executar_consulta(
    "Total de clientes cadastrados",
    "SELECT COUNT(*) as total FROM Clientes"
)
executar_consulta(
    "Filtro combinado (ID > 2 e Silva)",
    "SELECT * FROM Clientes WHERE id > ? AND nome LIKE ?",
    (2, '%Silva%')
)