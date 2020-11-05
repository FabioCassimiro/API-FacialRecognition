from app import app
from app.exception.loginException import UserNotFound
from app.models.passwordEncoder import encoder
from app.models.EncodesFace import facial_recognition
import mysql.connector

cnx = mysql.connector.connect(
    host = app.config['HOST'],
    user = app.config['USERDB'],
    database = app.config['DATABASE'],
    password = app.config['PASSWORDDB']
)

consult = cnx.cursor()

# Valida as credenciais do usuario
def valid_user(credential):
    credentials = search_credentials(credential.get('username'))
    
    if credentials:
        if facial_recognition(credentials[0],credential['image']):
            if credentials[1] == encoder(credential.get('password')):
                return True
            else:
                return False
        else:
            return False  
    else:
        raise UserNotFound('Usuario nao cadastrado')
        return False

# Busca credenciais do usuario para as demais validações
def search_credentials(user):
    query = """SELECT username,password FROM USERS 
                WHERE USERNAME = %s"""

    try:
        consult.execute(
            query,
            (
                user,
            )
        )

        result = consult.fetchone()
        return result
    except (Exception) as ex:
        print(ex)
        return None
