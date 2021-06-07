#for crescente
for n in range(0,3):
    print(f"For crescente: {n}")

#for decrescente
for n in range(3,0, -1):
    print(f"For decrescente: {n}")

#for percorrendo letra a letra em uma string.
palavra = "devaria"
for letra in palavra:
    print(f"For letra a letra: {letra}")

#for percorrendo objetos em uma lista
def darBoasVindas(pessoa):
    print(f"Seja bem vindo {pessoa}")


pessoas =["Weslley", "Celso", "Renata"]
for pessoa in pessoas:
    darBoasVindas(pessoa)

#index dos elementos com função enumerate
pessoas =["Weslley", "Celso", "Renata"]
for i, p in enumerate(pessoas, start=0):
    print(f'Pessoa:{p} no index:{i}')

#While
n = 0
while (n < 3):
    print(f"Estrutura While:{n}")
    n += 1


