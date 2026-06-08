from tabulate import tabulate


def analisar_missao(dados, fila_alertas):

    energia = dados["reserva_energia"]
    radiacao = dados["radiacao"]
    comunicacao = dados["qualidade_comunicacao"]

    status = "NORMAL"

    if energia < 35 and comunicacao < 50 and radiacao > 70:
        status = "EMERGÊNCIA TOTAL"
        fila_alertas.append(("CRÍTICO", "Colapso múltiplo"))

    elif energia < 35 and comunicacao < 50:
        status = "CRÍTICO"
        fila_alertas.append(("CRÍTICO", "Energia e comunicação baixas"))

    elif radiacao > 80:
        status = "ALERTA"
        fila_alertas.append(("ALERTA", "Radiação elevada"))

    # Verificação dos módulos críticos
    for modulo, estado in dados["modulos"].items():

        if not estado:

            fila_alertas.append(
                ("CRÍTICO", f"Módulo {modulo} inoperante")
            )

            status = "CRÍTICO"

    return status


def exibir_diagnostico(status, reserva, previsao, tendencia):

    tabela = [
        ["Status", status],
        ["Reserva", f"{reserva}%"],
        ["Previsão", f"{previsao:.1f}%"],
        ["Tendência", tendencia]
    ]

    print("\n===== DIAGNÓSTICO =====")

    print(tabulate(
        tabela,
        headers=["Métrica", "Valor"],
        tablefmt="fancy_grid"
    ))
