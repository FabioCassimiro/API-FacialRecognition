from app.models.images import image
from app.models.searchFaces import recognition_face
from app.exception.loginException import FaceNotMatch
import face_recognition as fr
import os

url_data_image = "./face/"
url_image = "./faces_request/"

user_face = []

# Valida o reconecimento facial
def facial_recognition(user, dataImage):
    try:
        filename = 'imageRequest.jpeg'
        image(
            dataImage,
            './faces_request/imageRequest.jpeg'
        )
        recognition_face(user)
        user_face.append(encode_image('imagemBanco.jpeg'))
        return compare_faces(filename)
    except Exception as identifier:
        print(identifier)

# codifica imagem
def encode_image(file):
    image = fr.load_image_file(url_data_image + file)
    image_encoding = fr.face_encodings(image)[0]
    return image_encoding

# faz a comparação dos rostos
def compare_faces(name):

    imagem_comparativa = fr.load_image_file(url_image + name)
    location = fr.face_locations(imagem_comparativa)
    encoding = fr.face_encodings(imagem_comparativa, location)

    for (direta,esquerda,cima,baixo), face_encoding in zip(location, encoding):
        comparation = fr.compare_faces(user_face, face_encoding, 0.6)
        return comparation

