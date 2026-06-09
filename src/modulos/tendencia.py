def analisar_tendencia(dados):

    consumo = dados["energia_consumida"]

    if consumo[-1] > consumo[-2]:
        tendencia = "AUMENTO"

    elif consumo[-1] < consumo[-2]:
        tendencia = "REDUÇÃO"

    else:
        tendencia = "ESTÁVEL"

    # opcional: salvar histórico
    if "historico_tendencia" in dados:
        dados["historico_tendencia"].append(tendencia)

    return tendencia