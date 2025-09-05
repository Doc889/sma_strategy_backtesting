# SMA strategy

Данный проект представляет из себя backtesting стратегии входа в сделку на основе двух скользящих средних (SMA) на таймфрейме - 1 д.

Реализованный функционал:
1. Загрука исторических данные по тикеру.
2. Оптимизирование параметров короткой и длинной SMA.
3. Backtest и рассчет Sharpe Ratio.
4. Визуализизация стратегии с отображением точек входа и выхода.

## Демонстрация
**Результаты:**
<img width="2762" height="1097" alt="image" src="https://github.com/user-attachments/assets/f3e2d715-4986-4ca1-a89b-1fc3dcaf8ff9" />

<img width="2531" height="1515" alt="image" src="https://github.com/user-attachments/assets/18d32602-cdbe-433d-ae55-7d460b943db8" />


## Стек технологий
- Python, optuna
- NumPy, pandas, yfinance
- Matplotlib

## Структура проекта
```
backtest_and_optimization.py - функциии бэктеста и оптимизации
visualization.py - функция визуализации стратегии
main.py - главный скрипт для запуска
requirements.txt - зависимости
```

##  Установка и запуск

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Doc889/sma_strategy_backtesting.git
    cd sma_strategy_backtesting
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Запустите проект:
    ```bash
    python main.py
    ```
4. Введите необходимый тикер в терминале.

## Будущее развитие проекта
- Выбор биржи для торговли.
- Рассчет комиссий за перенос позиции, в зависимости от выбранной платформы.
- Реализация функций открытия и закрытия позиций.
- Интеграция с мессенджером для уведомлений.
