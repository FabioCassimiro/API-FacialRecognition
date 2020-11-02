import mysql.connector
import base64
import os

cnx = mysql.connector.connect(user="root", database="recognition_system")
consult = cnx.cursor()


def recognition_face(username):
        convert_to_image('./face/imagemBanco.jpeg',search_image(username))


def search_image(username):
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
        print("Error:",identifier)


def convert_to_image(url,base64image):

    with open(url, 'wb') as convert:
        convert.write(base64.b64decode((base64image)))
        convert.close()
