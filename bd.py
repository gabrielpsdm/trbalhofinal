def validarlogin(cursor, nome, senha):
    # Executar o SQL
    cursor.execute(f'select idfuncionarios from funcionarios WHERE nome = "{nome} " and senha = "{senha}"')

    # Recuperando o retorno do BD
    funcionarios = cursor.fetchone()

    cursor.close()

    # Retornar os dados
    return funcionarios

def incluir_anuncio(cursor,conn,nomecar,marcacar,anocar,corcar,precocar):
    cursor.execute(f'INSERT into concessionaria.carros (nome,marca,ano,cor,preco) VALUES ("{nomecar}","{marcacar}","{anocar}","{corcar}","{precocar}")')
    conn.commit()

def excluir_anuncio(cursor,conn,carroid):
    cursor.execute(f'DELETE FROM concessionaria.carros WHERE idcarros = "{carroid}"')
    conn.commit()

def incluir_usuario(cursor, conn, login, senha):
    cursor.execute(f'INSERT into concessionaria.funcionarios (nome,senha) VALUES ("{login}","{senha}")')
    conn.commit()

def excluir_user(cursor,conn,funcid):
    cursor.execute(f'DELETE FROM concessionaria.funcionarios WHERE idfuncionarios = "{funcid}"')
    conn.commit()


def consultar_carros(cursor, buscando):
    cursor.execute(f'SELECT nome FROM carros WHERE nome = "{buscando}" or marca = "{buscando}"')
    consulta = cursor.fetchall()
    cursor.close()
    return consulta
def get_carros(cursor):

    # Executar o SQL
    cursor.execute(f'SELECT carros.nome,carros.marca,carros.ano,carros.cor,carros.preco FROM carros')

    # Recuperando o retorno do BD
    carros = cursor.fetchall()

    # Retornar os dados
    return carros