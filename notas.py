notas = ["6","7","8"]
suma = 1
media = 0

def calcular_media(notas):
    for nota in notas:
        suma = suma + nota
        media = suma / 3
    return media

print(f"Las notas son",media)

