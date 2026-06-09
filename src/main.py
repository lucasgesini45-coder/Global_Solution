from monitoramento import carregar_dados
from modulos.diagnostico import (
    analisar_missao,
    exibir_diagnostico)
from modulos.alertas import (
    criar_fila_alertas,
    exibir_alertas)
from modulos.recomendacoes import (
    exibir_recomendacoes)
from modulos.eventos import (
    exibir_eventos)
from modulos.hierarquia import (
    exibir_hierarquia)

from modulos.simulacao import (simular_missao)

from modulos.previsao import (prever_energia)

from modulos.tendencia import (analisar_tendencia)

from modulos.analise_matriz import (analisar_matriz)

from modulos.graficos import (grafico_missao)

from modulos.inconsistencias import (detectar_inconsistencias,relatorio_inconsistencias)


# =========================
# CARREGAR DADOS
# =========================

dados = carregar_dados("dados_missao.json")

pilha_eventos = dados["eventos"]

hierarquia = dados["hierarquia"]


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("\n" + "=" * 60)
    print("🚀 SISTEMA DE MONITORAMENTO ESPACIAL")
    print("=" * 60)

    print("1 - Painel Operacional")
    print("2 - Telemetria e Análises")
    print("3 - Eventos da Missão")
    print("4 - Simulação da Missão")
    print("5 - Dashboard Gráfico")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # ==========================================
    # PAINEL OPERACIONAL
    # ==========================================

    if opcao == "1":

        fila = criar_fila_alertas()
        status = analisar_missao(dados,fila)
        inconsistencias = detectar_inconsistencias(dados,fila)
        previsao = prever_energia(dados)
        tendencia = analisar_tendencia(dados)
        exibir_diagnostico(status,dados["reserva_energia"],previsao,tendencia)
        exibir_alertas(fila)
        relatorio_inconsistencias(inconsistencias)
        exibir_recomendacoes(dados,previsao)
        input("\nPressione ENTER para voltar ao menu...")

    # ==========================================
    # TELEMETRIA E ANÁLISES
    # ==========================================

    elif opcao == "2":
        analisar_matriz(dados)

        exibir_hierarquia(hierarquia)

        input("\nPressione ENTER para voltar ao menu...")

    # ==========================================
    # EVENTOS
    # ==========================================

    elif opcao == "3":

        exibir_eventos(pilha_eventos)

        input("\nPressione ENTER para voltar ao menu...")

    # ==========================================
    # SIMULAÇÃO
    # ==========================================

    elif opcao == "4":

        simular_missao(
            dados,
            5,
            criar_fila_alertas,
            analisar_missao,
            prever_energia,
            analisar_tendencia,
            exibir_diagnostico,
            exibir_alertas
        )

        input(
            "\nPressione ENTER para voltar ao menu..."
        )

    # ==========================================
    # DASHBOARD GRÁFICO
    # ==========================================

    elif opcao == "5":

        grafico_missao(
            dados
        )

    # ==========================================
    # SAIR
    # ==========================================

    elif opcao == "0":

        print("\n🛰 Encerrando sistema...")
        break

    else:

        print(
            "\n❌ Opção inválida."
        )

