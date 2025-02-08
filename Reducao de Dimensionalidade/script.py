import PIL
from PIL import Image

with Image.open('doctor.jpg') as imagem:
    nova_imagem = imagem.convert("L")
    #nova_imagem.show()
    #nova_imagem = imagem.save(r'"c:\Users\R3STL3S\neDrive\Documentos\Python\Projetos de ML\Reducao de Dimensionalidade\doctor_gs.jpg"')
    nova_imagem.save("doctor_gs.jpeg")
    
    #processo de tornar preto e branco
    #definicao do limite
    limite = 100
    nova_imagem = nova_imagem.point(lambda x: 255 if x > limite else 0)
    nova_imagem.save("doctor_bw.jpeg")