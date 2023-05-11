print("Calculadora Python")
try:
    operation = input("Digite a operação que deseja realizar ('+' ou '-'): ")
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    if operation == "+":
        print(f"{number1}+{number2}={number1 + number2}")
    elif operation == "-":
        print(f"{number1}+{number2}={number1 + number2}")
    else:
        print("Operação Inválida, digite um operador válido.")
except:
    print("Número inválido")