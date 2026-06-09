import matplotlib.pyplot as plt


def grafico_missao(dados):

    ciclos = list(range(len(dados["energia_gerada"])))

    plt.figure(figsize=(14, 10))

    # Energia
    plt.subplot(2, 2, 1)

    plt.plot(
        ciclos,
        dados["energia_gerada"],
        marker="o",
        label="Gerada"
    )

    plt.plot(
        ciclos,
        dados["energia_consumida"],
        marker="o",
        label="Consumida"
    )

    plt.title("Energia")
    plt.legend()
    plt.grid()

    # Temperatura
    plt.subplot(2, 2, 2)

    plt.plot(
        ciclos,
        dados["temperatura"],
        marker="o"
    )

    plt.title("Temperatura")
    plt.grid()

    # Radiação
    plt.subplot(2, 2, 3)

    plt.plot(
        ciclos,
        dados["historico_radiacao"],
        marker="o"
    )

    plt.title("Radiação")
    plt.grid()

    # Reserva de energia
    plt.subplot(2, 2, 4)

    plt.plot(
        ciclos,
        dados["historico_reserva"],
        marker="o"
    )

    plt.title("Reserva Energética")
    plt.grid()

    plt.tight_layout()
    plt.show()