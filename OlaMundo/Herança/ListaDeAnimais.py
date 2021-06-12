from Herança.classes.Ave import Ave
from Herança.classes.Mamifero import Mamifero
from Herança.classes.Peixe import Peixe
from Herança.classes.Reptil import Reptil

if __name__ == '__main__':

    # Criar a lista de animais disponiveis no banco de dados
    listaAnimais = [
        Mamifero('Leão', 4, False, False),
        Peixe("Tubarão", 2, True, True),
        Reptil("Serpente", 8.0, True, 0),
        Ave("Gavião", 500, True, True)
    ]
    # Receber o nome do animal solicitado pelo usuário
    nomeAnimal = input("Digite o nome de um animal vertebrado:")

    animalEncontrado = list(filter(lambda a: a.nome == nomeAnimal, listaAnimais))

    if len(animalEncontrado) == 0:
        print("Animal não encontrado.")
    else:
        if isinstance(animalEncontrado[0], Mamifero):
            print(f"Animal {animalEncontrado[0].nome} encontrado do tipo mamifero e tem {animalEncontrado[0].qtdMamas} mamas.")
        elif isinstance(animalEncontrado[0], Peixe):
            print(f"Animal {animalEncontrado[0].nome} encontrado do tipo Peixe e tem {animalEncontrado[0].qtdNadadeiras} nadadeiras.")
        elif isinstance(animalEncontrado[0].nome, Reptil):
            print(f"Animal {animalEncontrado[0].nome} encontrado do tipo Reptil e tem  temperatura corporal = {animalEncontrado[0].temperaturaCorporal}")
        elif isinstance(animalEncontrado[0], Ave):
            print(f"Animal {animalEncontrado[0].nome} encontrado do tipo Ave e tem {animalEncontrado[0].qtdPenas} penas.")
        else:
            print("Ocorreu um erro ao localizar o animal.")