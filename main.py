from tipo import Tipo
from lancamento import Lancamento
from relatorio import Relatorio
opcao = "Escolha uma opção: "


try:
    tipo = Tipo()
    lancamento = Lancamento()
    relatorio = Relatorio()
    

    #ramificação de escolhas
    print("""
        Escolha a opção desejada\n
         1 - Tipo\n
         2 - Vendas diarias\n 
         3 - Vendas do mês
         """)
    selection = int(input(opcao))

    #ramificação para tipos
    if selection == 1:
        print("""
        1 - Inserir um novo tipo\n
        2 - Atualizar um tipo \n
        3 - Deletar um tipo \n
        4 - Listar todos os tipos
        """)
        selectType = int(input(opcao))

        #decisão para definir oque deseja fazer com o tipo / inserir / deletar / atualizar / listar
        if selectType == 1: 
            print("Crir um novo tipo")
            tipo.tipo = input("Qual o tipo que deseja inserir: ")
            tipo.inserir(tipo)
            print("Inserido!")

        if selectType == 2: 
            print("Atualizar um tipo")
            tipo.id = input("Qual registro deseja alterar: ")
            tipo.tipo = input("Informe qual será o nome tipo do tipo: ")
            tipo.update(tipo)
            print("Atulaizado!")
            
        if selectType == 3: 
            print("Deletar um tipo")
            tipo.id = int(input("Informe qual registro deseja deletar: "))
            tipo.delete(tipo)
            print("Deletado!")

        if selectType == 4: 
            print("Lista os tipos")
            tipo.selectAll()

    #ramificação de escolha de vendas
    if selection == 2:
        print("""
        1 - Deseja inserir uma nova vendas diaria?\n
        2 - Deseja atualizar uma venda diaria? \n
        3 - Deseja Deletar uma venda diaria? \n
        4 - Listar todas as vendas diarias?
        """)
        selectSells = input(opcao)

        #decisão para definir oque fazer com as vendas, criar / atualizar / deletar / listar
        if selectSells == 1:
            print("Criar nova venda: ")
            lancamento.tipo = input("Informe o tipo: ")
            lancamento.data = input("Infome a data: ")
            lancamento.observacao = input("Informe uma observação: ")
            lancamento.valor = input("Informe o valor: ")
            lancamento.inserir(lancamento)
            print("Criado com sucesso!")

        if selectSells == 2:
            print("Atualizar uma venda: ")
            lancamento.id = input("Qual é o identificado que deseja alterar: ")
            lancamento.data = input("Infome a data: ")
            lancamento.observacao = input("Informe uma observação: ")
            lancamento.valor = input("Informe o valor: ")
            lancamento.update(lancamento)
            print("Atualizado com sucesso!")

        if selectSells == 3:
            print("Deletar uma venda: ")
            lancamento.id = input("Qual é o identificado que deseja deletar: ")
            lancamento.delete(lancamento)
            print("Deletado com sucesso!")

        if selectSells == 4:
            print("Lista todas as vendas: ")
            lancamento.selectAll()
    
    if selection == 3:
        print("Vendas do mês: ")
        relatorio.selectAll()

except (Exception) as e:
    print(f'Deu um erro: {e}')
