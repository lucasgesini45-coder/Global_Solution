from tabulate import tabulate

def analisar_matriz(dados):

    energia_gerada = dados["energia_gerada"]
    energia_consumida = dados["energia_consumida"]
    temperatura = dados["temperatura"]

    variacao_energia = energia_gerada[-1] - energia_consumida[-1]
    media_temperatura = sum(temperatura) / len(temperatura)

    tabela = [
        ["Variação de Energia", variacao_energia],
        ["Média Temperatura", f"{media_temperatura:.1f} °C"]
    ]

    print("\n===== MATRIZ DE TELEMETRIA =====")

    print(tabulate(tabela, headers=["Indicador", "Valor"], tablefmt="fancy_grid"))

    return variacao_energia, media_temperatura