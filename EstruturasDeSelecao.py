listaConvidados = ['Weslley', 'Ana', 'Joao']

nome = input("Informe o nome:")
idade = int(input("Informe a idade:"))

estaConvidado = nome in listaConvidados
maiorIdade = idade >= 18

if estaConvidado:
    if maiorIdade:
        print("Bem vindo À festa!")
    else:
        print("Você está na lista, porem é menor de idade.")
else:
    print("Desculpe, mas você não foi convidado.")
