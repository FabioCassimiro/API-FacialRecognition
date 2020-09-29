import face_recognition as fr

url_image = ".\\face\\"


def adiciona_rostos_conhecidos(arquivo):
    imagem_banco = fr.load_image_file(url_image + arquivo)
    imagem_banco_encoding = fr.face_encodings(imagem_banco)[0]
    return imagem_banco_encoding



rosto_conhecidos = [
    adiciona_rostos_conhecidos("teste.jpeg"),
    adiciona_rostos_conhecidos("teste1.jpeg"),
    adiciona_rostos_conhecidos("teste2.jpeg")
]

nomes_rostos_conhecidos = [
    "Daniel",
    "Walisson",
    "Daniele"
]


imagem_comparativa = fr.load_image_file(url_image + "Daniel.jpeg")
local_rosto = fr.face_locations(imagem_comparativa)
rosto_codificado = fr.face_encodings(imagem_comparativa,local_rosto)



for (top, right, bottom, left), face_encoding in zip(local_rosto, rosto_codificado):
    
    comparacao = fr.compare_faces(rosto_conhecidos, face_encoding,0.7)

    name = "Desconhecido"
    if True in comparacao:
        melhor_comparacao = comparacao.index(True)
        name = nomes_rostos_conhecidos[melhor_comparacao]
        print(name)
    else:
        print("Não achei")