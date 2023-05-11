print("Calculadora Python")

operation = input("Digite a operação que deseja realizar ('+', '-' ou '*'): ")

if(operation != "+" or operation != "-" or operation != "*"):
    print("Operação Inválida, digite um operador válido.")
else: 
    try:
        number1 = int(input("Digite o primeiro número: "))
        number2 = int(input("Digite o segundo número: "))

        if operation == "+":
            print(f"{number1}+{number2}={number1 + number2}")
        elif operation == "-":
            print(f"{number1}-{number2}={number1 - number2}")
        elif operation == "*":
            print(f"{number1}*{number2}={number1 * number2}")
    except:
        print("Número inválido")