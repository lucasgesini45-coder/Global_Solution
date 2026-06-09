from collections import deque

def criar_fila_alertas():
    return deque()


def exibir_alertas(fila_alertas):

    print("\n===== ALERTAS =====")

    if not fila_alertas:
        print("Nenhum alerta.")
        return

    for nivel, msg in fila_alertas:
        print(f"[{nivel}] {msg}")