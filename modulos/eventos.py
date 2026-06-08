from tabulate import tabulate


def exibir_eventos(eventos):

    print("\n===== EVENTOS CRÍTICOS =====")

    tabela = []

    for i, evento in enumerate(list(eventos)[-8:][::-1], start=1):
        tabela.append([i, evento])

    print(tabulate(
        tabela,
        headers=["#", "Evento"],
        tablefmt="fancy_grid"
    ))