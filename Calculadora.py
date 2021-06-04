def realizarCalculo(n1, n2, operador):
    if operador == "+":
        resultado = n1 + n2
    elif operador == "-":
        resultado = n1 - n2
    elif operador == "*":
        resultado = n1 * n2
    elif operador == "/":
        resultado = n1 / n2
    elif operador == "%":
        resultado = n1 % n2
    else:
        resultado = 0
    return resultado


n1 = float(input('Digite o primeiro numero:'))
operador = input("Digite o operador(+,-,*,/,%):")
n2 = float(input('Digite o segundo numero:'))

calculo = realizarCalculo(n1, n2, operador)
print(f'O resultado do calculo é {calculo}')






