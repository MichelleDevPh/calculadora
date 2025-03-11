#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    else:
        return 0

# Exemplo de uso
if __name__ == "__main__":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = int(input("Escolha a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

    resultado = calculadora(n1, n2, op)
    print(f"Resultado: {resultado}")