import os
lista_de_gastos = []

# TÍTULO
def cabecalho_projeto():
    print("💰 Sistema de Controle de Gastos Mensais (CLI)\n")
cabecalho_projeto()

# MENU PRINCIPAL
def exibir_opcoes():
    print("1- Adicionar gasto")
    print("2- Listar gastos")
    print("3- Total por categoria")
    print("4- Total geral")
    print("5- Categoria com maior gasto")
    print("6- Sair\n")         

# VOLTAR AO MENU
def voltar_menu():
    os.system("cls")
    cabecalho_projeto()
    exibir_opcoes()
    escolha_opcao()

# OPÇÕES
def escolha_opcao():
    opcao = int(input("\nDigite uma opção: "))
    
    try:
        if opcao == 1:
            adicionando_gastos()
        elif opcao == 2:
            listar_gastos()
        elif opcao == 3:
            total_categoria()
        elif opcao == 4:
            print("4- Total geral")
        elif opcao == 5:
            print("5- Categoria com maior gasto")
        elif opcao == 6:
            finalizar_app()
    except:
        opcao_invalida()  

# ADICIONAR GASTOS
def adicionando_gastos():
    valor = float(input("\nDigite o valor a ser adicionado: R$ "))
    categoria = input("Digite a categoria do item: ")
    descricao = input("Digite a descrição do item: ")
    
    gasto = {
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }

    lista_de_gastos.append(gasto)

    print("\n✅ Gasto adicionado com sucesso!")

    input("\nPressione ENTER para voltar ao menu...\n")
    voltar_menu()

# LISTAR GASTOS
def listar_gastos(): 
    if not lista_de_gastos:
        print("\n❌ Nenhum gasto cadastrado.")
    else:
        print("\n📋 Lista de Gastos:\n")
        for i, gasto in enumerate(lista_de_gastos, start=1):
            print(
                f"{i}. Valor: R$ {gasto['valor']:.2f} | "
                f"Categoria: {gasto['categoria']} | "
                f"Descrição: {gasto['descricao']}"
            )
    
    input("\nPressione ENTER para voltar ao menu...\n")
    voltar_menu()      

# TOTAL POR CATEGORIA
def total_categoria():
    ...

# OPÇÃO INVÁLIDA       
def opcao_invalida():
    print("❌ Opção inválida!\n")
    voltar_menu()

def exibir_subtitulos(texto):
    os.system("cls")
    print(texto)
    print()

def finalizar_app():
    exibir_subtitulos("👋 Saindo do sistema...")
    
voltar_menu()