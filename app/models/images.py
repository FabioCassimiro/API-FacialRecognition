import base64


def image(byte_image, path_image):
    convert_to_image(adjust_bytes(byte_image),path_image)
    
# converte os bytes em imagem e salva no path especificado 
def convert_to_image(byte_image,path_image='"./face/image.jpeg'):
    with open(path_image,'wb') as image:
        image.write(base64.b64decode(byte_image))
        image.close()
        
# remove o cabeçalho do base64 enviado na requisição pelo JS
def adjust_bytes(byte_image):
    return byte_image.replace('data:image/png;base64,','')