from app import app
from app.models.images import convert_to_image
import mysql.connector

cnx = mysql.connector.connect(
    host = app.config['HOST'],
    user = app.config['USERDB'],
    database = app.config['DATABASE'],
    password = app.config['PASSWORDDB']
)

consult = cnx.cursor()

# Resposavel por buscar imagem do usuario no banco de dados e salvar
# no caminho especificado 

def recognition_face(username):
        convert_to_image(search_image(username),'./face/imagemBanco.jpeg')

# busca os bytes da imagem salva no banco de dados do respectivo usuario.
def search_image(username):
    query = "SELECT IMAGE FROM IMAGES WHERE USERNAME = %s"

    try:
        consult.execute(
            query,
            (
                username,
            )
        )
        image_user = consult.fetchone()
        return image_user[0]
    except Exception as error:
        print("Error: ", error)
