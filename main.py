import yfinance as yf
import numpy as np

from backtest_and_optimization import optimize_sma
from visualization import plot_strategy


def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)
    data["Return"] = data["Close"].pct_change()
    return data


def apply_strategy(data, short_window, long_window):
    df = data.copy()
    df["SMA_short"] = df["Close"].rolling(short_window).mean()
    df["SMA_long"] = df["Close"].rolling(long_window).mean()
    df["Signal"] = np.where(
        (df["SMA_short"] > df["SMA_long"]) & (df["SMA_short"].shift(1) <= df["SMA_long"].shift(1)),
        1,
        np.where(
            (df["SMA_short"] < df["SMA_long"]) & (df["SMA_short"].shift(1) >= df["SMA_long"].shift(1)),
            -1,
            0
        )
    )
    return df


if __name__ == "__main__":
    ticker = str(input('Введите тикер: '))  # можно изменить
    start = "2020-01-01"
    end = "2023-01-01"

    print(f"Загружаем данные для {ticker}...")
    data = load_data(ticker, start, end)

    print("Оптимизируем параметры SMA...")
    best_params, best_sharpe = optimize_sma(data, n_trials=50)
    print(f"Лучшие параметры: {best_params}")
    print(f"Sharpe Ratio: {best_sharpe:.2f}")

    df_strategy = apply_strategy(data, best_params["short_window"], best_params["long_window"])

    print("Визуализируем стратегию...")
    plot_strategy(df_strategy, ticker, best_params["short_window"], best_params["long_window"])
