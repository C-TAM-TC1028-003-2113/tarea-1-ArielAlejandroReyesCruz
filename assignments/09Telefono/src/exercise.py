def main():
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    tarifa = 0.80

    costoTotal = (mensajes * tarifa) + (megas * tarifa) + (minutos * tarifa)

    print("El costo mensual es:", costoTotal)


if __name__ == '__main__':
    main()
