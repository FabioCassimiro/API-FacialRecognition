from app.exception.loginException import UserNotFound
from app.models.passwordEncoder import encoder
from app.models.EncodesFace import facial_recognition
import mysql.connector

cnx = mysql.connector.connect(user="root", database="recognition_system")
consult = cnx.cursor()


def valid_user(credential):
    credentials = search_username(credential.get('username'))
    
    if credentials:
        if facial_recognition(credentials[0],credential['image']):
            if credentials[1] == encoder(credential.get('password')):
                return {"authenticated": True}
            else:
                return {"authenticated": False}
        else:
            return {"authenticated": False}    
    else:
        raise UserNotFound('Usuario nao cadastrado')
        return {"authenticated": False}


def search_username(user):
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
