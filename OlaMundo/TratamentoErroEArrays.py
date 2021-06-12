if __name__ == '__main__':
    #tratamento de exceção
    try:
        print("iniciando calculo")
        n = 6 / 0
        print(n)
    except Exception as e:
        print("Ocorreu um erro. Favor tentar novamente.")

    #funções anonimas
    notasDosAlunos = [50, 95, 75, 80, 85, 58, 92]
    mediaDasNotas = lambda notas: sum(notas) / len(notas)
    print(f"A media das notas dos alunos é: {mediaDasNotas(notasDosAlunos)}")

    notasFiltradas = list(filter(lambda nota: nota > 80, notasDosAlunos))
    print(notasFiltradas)