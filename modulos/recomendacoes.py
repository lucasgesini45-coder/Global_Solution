from tabulate import tabulate

def exibir_recomendacoes(dados, previsao):

    recomendacoes = []

    if previsao < 25:
        recomendacoes += [
            "Desligar sistemas não essenciais",
            "Priorizar suporte à vida",
            "Economizar energia"
        ]

    if dados["radiacao"] > 80:
        recomendacoes.append("Ativar proteção contra radiação")

    if dados["qualidade_comunicacao"] < 50:
        recomendacoes.append("Utilizar canal de emergência")

    print("\n===== RECOMENDAÇÕES =====")

    if not recomendacoes:
        print("Nenhuma ação necessária.")
        return

    tabela = [[i + 1, r] for i, r in enumerate(recomendacoes)]

    print(tabulate(tabela, headers=["#", "Ação"], tablefmt="fancy_grid"))