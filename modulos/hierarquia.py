from tabulate import tabulate


def exibir_hierarquia(hierarquia):

    print("\n===== HIERARQUIA DA MISSÃO =====")

    tabela = []

    for setor, itens in hierarquia.items():

        for nome, status in itens.items():

            tabela.append([
                setor,
                nome,
                status
            ])

    print(tabulate(
        tabela,
        headers=["Setor", "Sistema", "Status"],
        tablefmt="fancy_grid"
    ))