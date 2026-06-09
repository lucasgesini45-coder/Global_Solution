def detectar_inconsistencias(dados, fila_alertas):

    inconsistencias = []

    comunicacao_status = dados["modulos"]["comunicacao"]
    qualidade_comunicacao = dados["qualidade_comunicacao"]

    energia = dados["reserva_energia"]
    radiacao = dados["radiacao"]

    if comunicacao_status == 0 and qualidade_comunicacao > 70:

        inconsistencias.append(
            ("CRÍTICO",
             "Comunicação desligada com sinal alto")
        )

    if energia > 100 or energia < 0:

        inconsistencias.append(
            ("CRÍTICO",
             "Energia fora dos limites")
        )

    if radiacao > 85 and dados["modulos"]["suporte_vida"]:

        inconsistencias.append(
            ("ALERTA",
             "Radiação extrema sem proteção")
        )

    for nivel, msg in inconsistencias:
        fila_alertas.append((nivel, msg))

    return inconsistencias


def relatorio_inconsistencias(inconsistencias):

    print("\n===== INCONSISTÊNCIAS =====")

    if not inconsistencias:

        print("Nenhuma inconsistência detectada.")
        return

    for nivel, msg in inconsistencias:

        print(f"[{nivel}] {msg}")

def detectar_inconsistencias(dados, fila_alertas):

    inconsistencias = []

    comunicacao_status = dados["modulos"]["comunicacao"]
    qualidade_comunicacao = dados["qualidade_comunicacao"]

    energia = dados["reserva_energia"]
    radiacao = dados["radiacao"]

    if comunicacao_status == 0 and qualidade_comunicacao > 70:

        inconsistencias.append(
            ("CRÍTICO",
             "Comunicação desligada com sinal alto")
        )

    if energia > 100 or energia < 0:

        inconsistencias.append(
            ("CRÍTICO",
             "Energia fora dos limites")
        )

    if radiacao > 85 and dados["modulos"]["suporte_vida"]:

        inconsistencias.append(
            ("ALERTA",
             "Radiação extrema sem proteção")
        )

    for nivel, msg in inconsistencias:
        fila_alertas.append((nivel, msg))

    return inconsistencias


def relatorio_inconsistencias(inconsistencias):

    print("\n===== INCONSISTÊNCIAS =====")

    if not inconsistencias:

        print("Nenhuma inconsistência detectada.")
        return

    for nivel, msg in inconsistencias:

        print(f"[{nivel}] {msg}")