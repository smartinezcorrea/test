def main():
    print("Pilon")
    print("2darama ensayo")
    numero1= float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    multiplicacion = numero1 * numero2
    if multiplicacion > 10:
        print("La multiplicación es mayor que 10")
    else:
        print("La multiplicación es menor o igual a 10")
    print("La multiplicación es:", multiplicacion)

if __name__ == "__main__":
    main()