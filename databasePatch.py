import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Empresa (
        id_empresa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        );
""")

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
        FOREIGN KEY(id_empresa) REFERENCES Empresa(id_empresa)
        );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
        id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_empresa INTEGER NOT NULL,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        peso REAL,
        FOREIGN KEY(id_empresa) REFERENCES Empresa(id_empresa)
        );
""")

cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 3665, '22361-003', 'Barra', 'Rio de Janeiro', '(21) 3325-1177')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Bambina', 36, '22510-050', 'Botafogo', 'Rio de Janeiro', '(21) 2246-3828')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua da Alfândega' , 33, '20070-000', 'Centro', 'Rio de Janeiro', '(21) 2263-9553')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Francisco Sá' , 35, '22080-010', 'Copacabana', 'Rio de Janeiro', '(21) 2523-4846')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Senador Vergueiro', 51, '22230-001', 'Flamengo', 'Rio de Janeiro', '(21) 2558-0458')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, Av. Rodrigo Otávio', 269, '22450-060', 'Gávea', 'Rio de Janeiro', '(21) 2511-1599')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Humaitá', 110, '22261-170', 'Humaitá', 'Rio de Janeiro', '(21) 2246-0658')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Visconde de Pirajá', 118, '21410-000', 'Ipanema', 'Rio de Janeiro', '(21) 2523-0099')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Pacheco Leão', 16, '22460-030', 'Jardim Botânico', 'Rio de Janeiro', '(21) 3874-4551')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Esteves Júnior', 36, '22231-160', 'Laranjeiras', 'Rio de Janeiro', '(21) 2285-1089')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Dias Ferreira', 290, '22431-050', 'Leblon', 'Rio de Janeiro', '(21) 2259-4699')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. Atlântica', 866, '22010-000', 'Leme', 'Rio de Janeiro', '(21) 2542-6949')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 16237, '22790-701', 'Recreio', 'Rio de Janeiro', '(21) 2437-6533')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 16237, '22790-701', 'Recreio', 'Rio de Janeiro', '(21) 2437-6533')")

#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Marechal Cantuaria', 178, '22291-060', 'Urca', 'Rio de Janeiro', '(21) 2295-1570')")

#cursor.execute("insert into Empresa(nome) values ('Zona Sul')")
#cursor.execute("insert into Empresa(nome) values ('Prix')")
#cursor.execute("insert into Empresa(nome) values ('Guanabara')")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')
#insert int Empresa values ("Prix");
#insert int Empresa values ("Guanabara");
conn.close()