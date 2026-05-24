def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def menu():
    print("\n=== Calculadora Matemática ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                print("Resultado:", soma(a, b))
            elif opcao == "2":
                print("Resultado:", subtracao(a, b))
            elif opcao == "3":
                print("Resultado:", multiplicacao(a, b))
            elif opcao == "4":
                print("Resultado:", divisao(a, b))

        except ValueError:
            print("Erro: digite apenas números válidos!")
    else:
        print("Opção inválida!")
