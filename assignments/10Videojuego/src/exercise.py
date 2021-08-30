def main():
    juegosNuevos = int(input("Dame la cantidad de juegos nuevos: "))
    juegosUsados = int(input("Dame la cantidad de juegos usados: "))

    precioTotal = (juegosNuevos * 1000) + (juegosUsados * 350)

    print("El total de la compra es:", precioTotal)


if __name__ == '__main__':
    main()
