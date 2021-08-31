import math
def main():
    palabras = int(input("Dame el número de palabras: "))

    numPaginas = math.ceil(palabras/475)
    costo = (numPaginas*60)*0.90

    print("El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
