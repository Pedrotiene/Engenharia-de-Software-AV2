from conexao import Database


db = Database()

cursor = db.get_cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS atletas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    ra TEXT NOT NULL,
    curso TEXT NOT NULL,
    telefone TEXT NOT NULL

)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS documentos (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_arquivo TEXT NOT NULL,
    atleta_id INTEGER,

    FOREIGN KEY(atleta_id)
    REFERENCES atletas(id)

)
""")


db.get_connection().commit()

print("Tabelas criadas com sucesso!")