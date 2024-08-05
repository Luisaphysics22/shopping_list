import os

menu = """

=========== LISTA DE COMPRAS ===========
[i] Inserir um item
[d] Deletar um item
[l] Listar os itens
========================================

=> Selecione uma opção: """


lista_compras = []


while True:
    opcao = input(menu)
  
    if opcao == "i":
        # comando para limpar o terminal
        os.system('cls' if os.name == 'nt' else 'clear') 

        produto = input("Produto: ")
        lista_compras.append(produto)

    elif opcao == "l":
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(lista_compras) == 0:
            print("A lista de compras está vazia!")

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

    elif opcao == "d":

        try:
            apagar_indice = int(input("Escolha o item que deseja apagar: "))
            del lista_compras[apagar_indice]    
            print("Item removido com sucesso!!")
        except ValueError:
            print("Por favor digite um número inteiro.")
        except IndexError:
            print("O item informado não existe na lista. Por favor, tente novamente.")
        except Exception:
            print("Erro desconhecido.")

    else:
        print("Opção inválida!! Por favor escolha i, d, ou l.")
    




