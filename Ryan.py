else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
elif opcao == '5':
    num = float(input("Digite o número para calcular a raiz quadrada: "))
    resultado = cmath.sqrt(num)  # Usando cmath.sqrt para raiz quadrada de números negativos
    print(f"Resultado: {resultado}")
elif opcao == '6':
    angulo = float(input("Digite o ângulo em graus: "))