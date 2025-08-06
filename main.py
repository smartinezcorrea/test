def main():
    print("Pilon")
    numero1= float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    suma = numero1 + numero2
    if suma > 10:
        print("La suma es mayor que 10")
    else:
        print("La suma es menor o igual a 10")
    print("La suma es:", suma)

if __name__ == "__main__":
    main()