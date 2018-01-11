import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

# criando a tabela (schema)
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS Empresa (
#        id_empresa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#        nome TEXT NOT NULL
#        );
#""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Localizacao_Empresa (
        id_localizacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_empresa INTEGER NOT NULL,
        endereco TEXT NOT NULL,
        numero INTEGER NOT NULL,
        cep VARCHAR(9) NOT NULL,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        telefone VARCHAR(9) NOT NULL,
        FOREIGN KEY(id_empresa) REFERENCES artist(Empresa)
        );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
        id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_empresa INTEGER NOT NULL,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        peso REAL NOT NULL,
        FOREIGN KEY(id_empresa) REFERENCES artist(Empresa)
        );
""")

print('Tabela criada com sucesso.')

conn.close()