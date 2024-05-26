#Ellen
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
#Andressa
print("8. Tangente")

opcao = input("Escolha uma operação (1/2/3/4/5/6/7/8): ")

if opcao == '1':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2

    print(f"Resultado: {resultado}")
#Luana
elif opcao == '2':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif opcao == '3':
    num1 = float(input("Digite o primeiro número: "))
#Matheus
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif opcao == '4':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print("Erro: Divisão por zero!")

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

    #Gabriel
    resultado = math.sin(math.radians(angulo))  # Convertendo o ângulo de graus para Radianos
    print(f"Seno: {resultado:.2f}")
    
elif opcao == '7':
    angulo = float(input("Digite o ângulo em graus: "))
    resultado = math.cos(math.radians(angulo))  # Convertendo o ângulo de graus para Radianos
    print(f"Cosseno: {resultado:.2f}")

elif opcao == '8':
    angulo = float(input("Digite o ângulo em graus: "))
    resultado = math.tan(math.radians(angulo))  # Convertendo o ângulo de graus para Radianos
    print(f"Tangente:{resultado:.2f}")
else:
    print("Opção inválida!")
