import math
print("Calculadora")
print("Operações disponíveis:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Raiz Quadrada")
print("6. Seno")
print("7. Cosseno")



elif opcao == '2':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif opcao == '3':
    num1 = float(input("Digite o primeiro número: "))

#Ryan
else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
elif opcao == '5':
    num = float(input("Digite o número para calcular a raiz quadrada: "))
    resultado = math.sqrt(num) 
    print(f"Resultado: {resultado}")
elif opcao == '6':
    angulo = float(input("Digite o ângulo em graus: "))




resultado = math.sin(math.radians(angulo))  # Convertendo o ângulo de graus para radianos
    print(f"Seno: {resultado:.2f}")
elif opcao == '7':
    angulo = float(input("Digite o ângulo em graus: "))
    resultado = math.cos(math.radians(angulo))  # Convertendo o ângulo de graus para radianos
    print(f"Cosseno: {resultado:.2f}")
elif opcao == '8':
    angulo = float(input("Digite o ângulo em graus: "))
    resultado = math.tan(math.radians(angulo))  # Convertendo o ângulo de graus para radianos
    print(f"Tangente:{resultado:.2f}")
else:
    print("Opção inválida!")
