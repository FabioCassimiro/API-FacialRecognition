import face_recognition as fr
from app.models.searchFaces import recognition_face
from app.models.images import image
from app.exception.loginException import FaceNotMatch
import os


url_data_image = "./face/"
url_image = "./faces_request/"

user_face = []
username = []


def facial_recognition(user, dataImage):
    try:
        filename = 'imageRequest.jpeg'
        image(
            dataImage,
            './faces_request/imageRequest.jpeg'
        )
        recognition_face(user)
        user_face.append(encode_image('imagemBanco.jpeg'))
        username.append(user)
        return compare_faces(filename)
    except Exception as identifier:
        print(identifier)


def save_image(data_image):
    file = data_image
    filepath = os.path.join(url_image, file.filename)
    file.save(filepath)
    return file.filename


def encode_image(file):
    image = fr.load_image_file(url_data_image + file)
    image_encoding = fr.face_encodings(image)[0]
    return image_encoding


def compare_faces(name):

    imagem_comparativa = fr.load_image_file(url_image + name)
    location = fr.face_locations(imagem_comparativa)
    encoding = fr.face_encodings(imagem_comparativa, location)

    for (direta,esquerda,cima,baixo), face_encoding in zip(location, encoding):
        comparation = fr.compare_faces(user_face, face_encoding, 0.6)
        if True in comparation:
            best_comparation = comparation.index(True)
            name = username[best_comparation]
            return True
        else:
            raise FaceNotMatch('Usuario nao reconhecido')
            return False
