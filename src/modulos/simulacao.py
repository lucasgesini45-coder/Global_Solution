import random
import time


# =========================
# ATUALIZAÇÃO DOS DADOS
# =========================
def atualizar_dados(dados):

    dados["reserva_energia"] += random.randint(-3, 3)
    dados["radiacao"] += random.randint(-2, 2)
    dados["qualidade_comunicacao"] += random.randint(-5, 5)

    dados["reserva_energia"] = max(0, min(100, dados["reserva_energia"]))
    dados["radiacao"] = max(0, min(100, dados["radiacao"]))
    dados["qualidade_comunicacao"] = max(0, min(100, dados["qualidade_comunicacao"]))


# =========================
# SIMULAÇÃO DA MISSÃO
# =========================
def simular_missao(
    dados,
    ciclos,
    criar_fila_alertas,
    analisar_missao,
    prever_energia,
    analisar_tendencia,
    exibir_diagnostico,
    exibir_alertas
):

    for ciclo in range(1, ciclos + 1):

        print(f"\n🚀 CICLO {ciclo}")

        # atualiza os dados a cada ciclo
        atualizar_dados(dados)

        # cria fila de alertas
        fila = criar_fila_alertas()

        # análise do sistema
        status = analisar_missao(dados, fila)
        previsao = prever_energia(dados)
        tendencia = analisar_tendencia(dados)

        # saída
        exibir_diagnostico(
            status,
            dados["reserva_energia"],
            previsao,
            tendencia
        )

        exibir_alertas(fila)

        time.sleep(1)