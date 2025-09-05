import numpy as np
import optuna


def backtest_strategy(short_window, long_window, data):
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

    df["Strategy_Return"] = df["Signal"].shift(1) * df["Return"]
    sharpe_ratio = (df["Strategy_Return"].mean() / df["Strategy_Return"].std()) * np.sqrt(252)
    return sharpe_ratio if not np.isnan(sharpe_ratio) else -np.inf


def optimize_sma(data, n_trials=30):
    def objective(trial):
        short_window = trial.suggest_int("short_window", 5, 30)
        long_window = trial.suggest_int("long_window", 31, 100)
        if short_window >= long_window:
            return -np.inf
        return backtest_strategy(short_window, long_window, data)

    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=n_trials)

    return study.best_params, study.best_value
