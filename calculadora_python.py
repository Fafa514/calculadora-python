def mostrar_menu():
    print("\n=== CALCULADORA PYTHON ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida!"
    return a / b

def calculadora():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '0':
            print("Saindo da calculadora... Até mais!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == '1':
            resultado = somar(num1, num2)
            operacao = "Soma"
        elif opcao == '2':
            resultado = subtrair(num1, num2)
            operacao = "Subtração"
        elif opcao == '3':
            resultado = multiplicar(num1, num2)
            operacao = "Multiplicação"
        elif opcao == '4':
            resultado = dividir(num1, num2)
            operacao = "Divisão"

        print(f"\nResultado da {operacao}: {resultado}")

if __name__ == "__main__":
    calculadora()
