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