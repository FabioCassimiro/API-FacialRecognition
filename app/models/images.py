import base64


def image(base64image, diretorio):
    convert_to_image(adjust_bytes(base64image),diretorio)

def convert_to_image(base64Image,diretorio='"./face/image.jpeg'):
    with open(diretorio,'wb') as image:
        image.write(base64.b64decode(base64Image))
        image.close()
        
    

def adjust_bytes(byte):
    return byte.replace('data:image/png;base64,','')