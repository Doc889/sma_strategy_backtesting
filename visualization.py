import matplotlib.pyplot as plt


def plot_strategy(df, ticker, short_window, long_window):
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df["Close"], label="Цена", color="black")
    plt.plot(df.index, df["SMA_short"], label=f"SMA {long_window}", color="blue")
    plt.plot(df.index, df["SMA_long"], label=f"SMA {short_window}", color="red")

    # Покупки и продажи
    plt.scatter(df.index[df["Signal"] == 1], df["Close"][df["Signal"] == 1], marker="^", color="green",
                label="Buy",
                s=100)
    plt.scatter(df.index[df["Signal"] == -1], df["Close"][df["Signal"] == -1], marker="v", color="red",
                label="Sell", s=100)

    plt.title(f"Стратегия двух скользящих средних - {ticker}")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    plt.show()