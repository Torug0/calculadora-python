print("Calculadora Python")
try:
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))

    print(f"{number1}+{number2}={number1 + number2}")

except:
    print("Número inválido")