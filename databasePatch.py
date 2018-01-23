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

cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (4, 'Av. Quintino Bocaiúva', 127, '24360-022', 'São Francisco', 'Niterói', '(21) 2611-7700')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (4, 'Av. Rui Barbosa', 325, '24360-440', 'São Francisco', 'Niterói', '(21) 2611-8079')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (4, 'Estrada Francisco da Cruz Nunes', 1601, '24320-330', 'Itaipu', 'Niterói', '(21) 3254-5200')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (4, 'Av. Nossa Sra. de Copacabana', 719, '22020-001', 'Copacabana', 'Rio de Janeiro', '(21) 3269-9824')")


#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 3665, '22361-003', 'Barra', 'Rio de Janeiro', '(21) 3325-1177')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Bambina', 36, '22510-050', 'Botafogo', 'Rio de Janeiro', '(21) 2246-3828')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua da Alfândega' , 33, '20070-000', 'Centro', 'Rio de Janeiro', '(21) 2263-9553')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Francisco Sá' , 35, '22080-010', 'Copacabana', 'Rio de Janeiro', '(21) 2523-4846')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Senador Vergueiro', 51, '22230-001', 'Flamengo', 'Rio de Janeiro', '(21) 2558-0458')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. Rodrigo Otávio', 269, '22450-060', 'Gávea', 'Rio de Janeiro', '(21) 2511-1599')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Humaitá', 110, '22261-170', 'Humaitá', 'Rio de Janeiro', '(21) 2246-0658')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Visconde de Pirajá', 118, '21410-000', 'Ipanema', 'Rio de Janeiro', '(21) 2523-0099')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Pacheco Leão', 16, '22460-030', 'Jardim Botânico', 'Rio de Janeiro', '(21) 3874-4551')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Esteves Júnior', 36, '22231-160', 'Laranjeiras', 'Rio de Janeiro', '(21) 2285-1089')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Dias Ferreira', 290, '22431-050', 'Leblon', 'Rio de Janeiro', '(21) 2259-4699')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. Atlântica', 866, '22010-000', 'Leme', 'Rio de Janeiro', '(21) 2542-6949')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 16237, '22790-701', 'Recreio', 'Rio de Janeiro', '(21) 2437-6533')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Av. das Américas', 16237, '22790-701', 'Recreio', 'Rio de Janeiro', '(21) 2437-6533')")
#cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (1, 'Rua Marechal Cantuaria', 178, '22291-060', 'Urca', 'Rio de Janeiro', '(21) 2295-1570')")

#cursor.execute("insert into Empresa(nome) values ('Zona Sul')")
#cursor.execute("insert into Empresa(nome) values ('Prix')")
#cursor.execute("insert into Empresa(nome) values ('Guanabara')")
#cursor.execute("insert into Empresa(nome) values ('Diamante')")
'''
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua 24 de Maio', 432, '20950-085', 'Riachuelo', 'Rio de Janeiro', '(21) 2241-4436')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Conde de Bonfim', 536, '20520-055', 'Tijuca', 'Rio de Janeiro', '(21) 2268-3977')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Gavião Peixoto', 123, '24230-101', 'NIterói', 'Rio de Janeiro', '(21) 2610-8890')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Praça Edmundo Rego', 8, '24230-101', 'Grajaú', 'Rio de Janeiro', '(21) 2578-3202')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Lucídio Lago', 292, '20780-020', 'Méier', 'Rio de Janeiro', '(21) 2501-8154')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Barão do Bom Retiro', 1115, '20715-002', 'Engenho Novo', 'Rio de Janeiro', '(21) 2241-6770')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Conde de Bonfim', 812, '20530-002', 'Tijuca', 'Rio de Janeiro', '(21) 2570-9747')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'R. Hadock Lobo', 5, '20260-130', 'Estácio', 'Rio de Janeiro', '(21) 2293-4884')") 
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua São Francisco Xavier', 374, '20550-013', 'Maracanã', 'Rio de Janeiro', '(21) 2569-2039')") 
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Av. Nossa Senhora de Copacabana', 673, '22050-001', 'Copacabana', 'Rio de Janeiro', '(21) 2547-0613')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Visconde de Pirajá', 270, '22410-000', 'Ipanema', 'Rio de Janeiro', '(21) 2523-0332')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (2, 'Rua Bruno Giorgi', 114, '22775-054', 'Barra da Tijuca', 'Rio de Janeiro', '(21) 2578-0032')")

cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Ministro Ari Franco', 80, '21862-005', 'Bangu', 'Rio de Janeiro', '(21) 2401-9970')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Rio da Prata', 1370, '21820-091', 'Bangu', 'Rio de Janeiro', '(21) 3337-2498')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. das Américas', 3.501, '22631-003', 'Barra da Tijuca', 'Rio de Janeiro', '(21) 2420-3738')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Estr. Intendente. Magalhães', 1236, '21331-720', 'Bento Ribeiro', 'Rio de Janeiro', '(21) 2452-2593')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av.Teixeira de Castro', 90, '21040-010', 'Bonsucesso', 'Rio de Janeiro', '(21) 2564-3942')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Ernani Cardoso', 350, '21310-310', 'Campinho', 'Rio de Janeiro', '(21) 2452-2279')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Aurélio Figueiredo', 205, '23052-000', 'Campo Grande', 'Rio de Janeiro', '(21) 2413-3819')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Tenente José Dias', 460, '25010-305', 'Duque de Caxias', 'Rio de Janeiro', '(21) 2671-2907')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Estr. Adhemar Bebiano', 3.994, '20766-721', 'Engenho da Rainha', 'Rio de Janeiro', '(21) 3899-5746')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Adolfo Bergamini', 113, '20730-000', 'Engenho de Dentro', 'Rio de Janeiro', '(21) 3899-5370')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Monsenhor Félix', 1.213, '21235-111', 'Irajá', 'Rio de Janeiro', '(21) 2471-1891')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Dr. Curvelo Cavalcante', 758, '23815-290', 'Itaguaí', 'Rio de Janeiro', '(21) 2688-4312')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Estr. do Cafundá', 1.560, '22725-031', 'Jacarepaguá', 'Rio de Janeiro', '(21) 2423-1334')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Marechal Deodoro,360, Rua São João S/N e Rua Marques Paraná', 100, '24030-060', 'Niteroí', 'Rio de Janeiro', '(21) 2717-4918')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Mal. Floriano Peixoto', 1552, '26220-060', 'Nova Iguaçu', 'Rio de Janeiro', '(21) 2667-4218')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Cesário de Melo', 10809, '23585-127', 'Paciência', 'Rio de Janeiro', '(21) 2409-6145')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Brás de Pina', 201, '21070-031', 'Penha', 'Rio de Janeiro', '(21) 2560-8249')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Dom Hélder Camara', 8403, '20751-001', 'Piedade', 'Rio de Janeiro', '(21) 2229-0334')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Santa Cruz', 419, '21710-230', 'Realengo', 'Rio de Janeiro', '(21) 2401-9610')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Estr. da Água Branca', 2380, '21730-000', 'Realengo', 'Rio de Janeiro', '(21) 3337-2468')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Felipe Cardoso', 1470, '23520-570', 'Santa Cruz', 'Rio de Janeiro', '(21) 2418-4015')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Jornalista Roberto Marinho', 221, '24451-715', 'São Gonçalo', 'Rio de Janeiro', '(21) 2724-9804')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Av. Nossa Senhora das Graças', 222, '25515-001', 'São João de Meriti', 'Rio de Janeiro', '(21) 2756-8899')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Almirante Cochrane', 146, '20550-040', 'Tijuca', 'Rio de Janeiro', '(21) 2568-1042')")
cursor.execute("insert into Localizacao_Empresa(id_empresa, endereco, numero, cep, bairro, cidade, telefone ) values (3, 'Rua Maxwell', 520, '23052-000', 'Vila Isabel', 'Rio de Janeiro', '(21) 2570-0927')")
'''
# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')
#insert int Empresa values ("Prix");
#insert int Empresa values ("Guanabara");
conn.close()