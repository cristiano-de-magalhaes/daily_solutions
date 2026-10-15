## imports
import pandas as pd
import numpy as np

# Dados de exemplo
df = pd.DataFrame({
    'price':   [100, 102, 98, 150, 103, 99, 101, 200, 97, 104],
    'volume':  [1000, 1200, 900, 50000, 1100, 950, 1050, 80000, 880, 1150],
    'returns': [0.01, 0.02, -0.01, 0.50, 0.03, -0.02, 0.01, 0.97, -0.03, 0.02]
})

FEATURES = ['price', 'volume', 'returns']

##############################################################################

## 1. Standard Scaler

def standard_scaler(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    df[cols] = (df[cols] - df[cols].mean()) / df[cols].std()
    return df

df_standard = df.pipe(standard_scaler, cols=FEATURES)

##############################################################################

## 2. Robust Scaler


def robust_scaler(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    median = df[cols].median()
    iqr    = df[cols].quantile(0.75) - df[cols].quantile(0.25)
    df[cols] = (df[cols] - median) / iqr
    return df

df_robust = df.pipe(robust_scaler, cols=FEATURES)

##############################################################################

## 3. MinMax Scaler


def minmax_scaler(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    min_ = df[cols].min()
    max_ = df[cols].max()
    df[cols] = (df[cols] - min_) / (max_ - min_)
    return df

df_minmax = df.pipe(minmax_scaler, cols=FEATURES)

##############################################################################

## 4. Log-retornos


def log_returns(df: pd.DataFrame, price_col: str = 'price') -> pd.DataFrame:
    df = df.copy()
    df[f'{price_col}_log_return'] = np.log(df[price_col] / df[price_col].shift(1))
    return df

df_logret = df.pipe(log_returns, price_col='price')

##############################################################################

## 5. Rolling Z-score (janela deslizante)


def rolling_zscore(df: pd.DataFrame, cols: list, window: int = 5) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        rolling_mean = df[col].rolling(window).mean()
        rolling_std  = df[col].rolling(window).std()
        df[f'{col}_rolling_z'] = (df[col] - rolling_mean) / rolling_std
    return df

df_rolling = df.pipe(rolling_zscore, cols=FEATURES, window=5)

##############################################################################

## 6. Winsorização + Robust Scaler


def winsorize(df: pd.DataFrame, cols: list, lower: float = 0.01, upper: float = 0.99) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        low  = df[col].quantile(lower)
        high = df[col].quantile(upper)
        df[col] = df[col].clip(low, high)
    return df

df_winsorized_robust = (
    df
    .pipe(winsorize,     cols=FEATURES, lower=0.01, upper=0.99)
    .pipe(robust_scaler, cols=FEATURES)
)

##############################################################################

## 7. Quantile Transformer


from scipy.stats import rankdata, norm

def quantile_transformer(df: pd.DataFrame, cols: list, output_dist: str = 'normal') -> pd.DataFrame:
    """
    output_dist: 'normal' ou 'uniform'
    """
    df = df.copy()
    n = len(df)
    for col in cols:
        ranks = rankdata(df[col]) / (n + 1)   # evita 0 e 1 exatos
        if output_dist == 'normal':
            df[col] = norm.ppf(ranks)
        else:
            df[col] = ranks                    # distribuição uniforme [0, 1]
    return df

df_quantile = df.pipe(quantile_transformer, cols=FEATURES, output_dist='normal')

##############################################################################

## Pipeline completo recomendado para finanças

# Encadeando as etapas mais robustas em sequência:

df_final = (
    df
    .pipe(log_returns,          price_col='price')
    .pipe(winsorize,            cols=FEATURES, lower=0.01, upper=0.99)
    .pipe(rolling_zscore,       cols=FEATURES, window=20)
    .pipe(quantile_transformer, cols=FEATURES, output_dist='normal')
)

##############################################################################

# A beleza do `.pipe()` é exatamente essa legibilidade — cada etapa é uma função pura que recebe e devolve um DataFrame, e o encadeamento deixa clara a ordem das transformações. Qualquer etapa pode ser removida, reordenada ou testada isoladamente sem quebrar o resto do pipeline.