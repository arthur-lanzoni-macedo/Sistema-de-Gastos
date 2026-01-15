# TÍTULO
def cabecalho_projeto():
    print("𝒮𝒾𝓈𝓉𝑒𝓂𝒶 𝒹𝑒 𝒞𝑜𝓃𝓉𝓇𝑜𝓁𝑒 𝒹𝑒 𝒢𝒶𝓈𝓉𝑜𝓈 𝑀𝑒𝓃𝓈𝒶𝒾𝓈 (𝒞𝐿𝐼)\n")
cabecalho_projeto()

# VOLTAR AO MENU
def voltar_menu():
    menu()

# ADICIONAR GASTOS

def adicionando_gastos():
    valor = float(input("\nDigite o valor a ser adicionado: R$ "))
    categoria = input("Digite a categoria do item: ")
    descricao = input("Digite a descrição do item: ")

    lista_de_gastos = []
    gasto = {
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }

    lista_de_gastos.append(gasto)

    print("\n✅ Gasto adicionado com sucesso!")
    print(
        f"💰 Valor: R$ {gasto['valor']:.2f} | "
        f"📂 Categoria: {gasto['categoria']} | "
        f"📝 Descrição: {gasto['descricao']}"
    )

    input("\nPressione ENTER para voltar ao menu...\n")
    return voltar_menu()


# MENU PRINCIPAL
def menu():
    while True:
        print("1- Adicionar gasto")
        print("2- Listar gastos")
        print("3- Total por categoria")
        print("4- Total geral")
        print("5- Categoria com maior gasto")
        print("6- Sair")

        opcao = int(input("\nDigite uma opção: "))

        if opcao == 1:
            adicionando_gastos()
        elif opcao == 2:
            ...
        elif opcao == 3:
            ...
        elif opcao == 4:
            ...
        elif opcao == 5:
            ...
        elif opcao == 6:
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida!\n")
menu()