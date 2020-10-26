import face_recognition as fr
from app.models.searchFaces import recognition_face 


url_data_image = ".\\face\\"
url_image = ".\\faces_request\\"

rosto_usuario = []
nome_usuario = []

def facial_recognition(user,filename):
    try:
        recognition_face(user)
        rosto_usuario.append(adiciona_rostos_conhecidos('imagemBanco.jpeg'))
        nome_usuario.append(user)
        return compara(filename)
    except Exception as identifier:
        print(identifier)


def adiciona_rostos_conhecidos(arquivo):
    imagem_banco = fr.load_image_file(url_data_image + arquivo)
    imagem_banco_encoding = fr.face_encodings(imagem_banco)[0]
    return imagem_banco_encoding

def compara(name):

    imagem_comparativa = fr.load_image_file(url_image + name)
    local_rosto = fr.face_locations(imagem_comparativa)
    rosto_codificado = fr.face_encodings(imagem_comparativa,local_rosto)



    for (top, right, bottom, left), face_encoding in zip(local_rosto, rosto_codificado):
        
        comparacao = fr.compare_faces(rosto_usuario, face_encoding,0.5)

        name = "Desconhecido"
        if True in comparacao:
            melhor_comparacao = comparacao.index(True)
            name = nome_usuario[melhor_comparacao]
            return {'authenticated-face': True}
        else:
            return {'authenticated-face': False}
