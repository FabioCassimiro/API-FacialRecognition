import mysql.connector
import base64
import os

cnx = mysql.connector.connect(user="root", database="recognition_system")
consult = cnx.cursor()


def recognition_face(username):
    convertToImage(searchImage(username))


def searchImage(username):
    query = "SELECT IMAGE FROM IMAGES WHERE USERNAME = %s"

    try:
        consult.execute(
            query,
            (
                username,
            )
        )
        result = consult.fetchone()
        return result[0]
    except Exception as identifier:
        print(identifier)


def convertToImage(base64image):
    
    with open('./face/imagemBanco.jpeg', 'wb') as convert:
        convert.write(base64.b64decode((base64image)))
        convert.close()
