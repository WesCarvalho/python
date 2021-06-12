if __name__ == '__main__':

    #Produtos do mercado
    produtosMercado = ["Pão", "Arroz", "Feijão", "Batata"]

    #produtos requisitados pelo usuario
    produtosRequisitados = []
    while True:
        produto = input("Digite um produto para adicionar na lista ('sair' para encerrar):")
        if produto == "sair":
            break

        produtosRequisitados.append(produto)

    #Salva os produtos indisponiveis e os disponiveis
    produtosIndisponiveis =[]
    produtosDisponiveis =[]

    for p in produtosRequisitados:
        if not p in produtosMercado:
            produtosIndisponiveis.append(p)
        else:
            produtosDisponiveis.append(p)

    print(f"Estes produtos estão disponiveis: {produtosDisponiveis}")
    print(f"Estes produtos estão indisponíveis: {produtosIndisponiveis}")

    #Ordena os produtos do mercado por ordem alfabetica.
    produtosMercado.sort()
    print(f"Confira nossa lista de produtos: {produtosMercado}")