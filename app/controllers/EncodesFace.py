import face_recognition as fr

url_image = "C:\\Users\\WINDOWS\\Downloads\\recognition\\face\\"

imagem_banco = fr.load_image_file(url_image + "teste.jpeg")
imagem_banco_encoding = fr.face_encodings(imagem_banco)[0]

imagem_banco_2 = fr.load_image_file(url_image + "teste1.jpeg")
imagem_banco_2_encoding = fr.face_encodings(imagem_banco_2)[0]

imagem_banco_3 = fr.load_image_file(url_image + "teste2.jpeg")
imagem_banco_3_encoding = fr.face_encodings(imagem_banco_3)[0]



rosto_conhecidos = [
    imagem_banco_encoding,
    imagem_banco_2_encoding,
    imagem_banco_3_encoding
]

nomes_rostos_conhecidos = [
    "Daniel",
    "Walisson",
    "Daniele"
]


imagem_comparativa = fr.load_image_file(url_image + "Daniele.jpeg")
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