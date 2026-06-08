def prever_energia(dados):

    consumo = dados["energia_consumida"]

    media = sum(consumo[-3:]) / 3
    previsao = dados["reserva_energia"] - (media / 10)

    # opcional: armazenar histórico
    if "historico_previsao" in dados:
        dados["historico_previsao"].append(previsao)

    return previsao