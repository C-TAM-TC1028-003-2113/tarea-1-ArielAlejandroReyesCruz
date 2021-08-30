def main():
    saldoMesAnterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    saldoSinIva = (saldoMesAnterior + ingresos - egresos - (cheques * 13))
    saldoConIva = saldoSinIva * 0.925

    print("El saldo final de la cuenta es:", saldoConIva)

if __name__ == '__main__':
    main()
