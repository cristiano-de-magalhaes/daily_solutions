#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# =========================
# Exemplo de dados
# =========================
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)

# =========================
# Padronização
# PCA é sensível à escala
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# PCA
# =========================
pca = PCA()
pca.fit(X_scaled)

# Variância explicada acumulada
cum_var = np.cumsum(pca.explained_variance_ratio_)

# =========================
# Encontrar ponto ideal
# Exemplo: 95% da variância
# =========================
n_components_95 = np.argmax(cum_var >= 0.95) + 1

print(f"Número de componentes para 95% da variância: {n_components_95}")

# =========================
# Gráfico Elbow
# =========================
plt.figure(figsize=(10, 6))

plt.plot(
    range(1, len(cum_var) + 1),
    cum_var,
    marker='o'
)

plt.axhline(
    y=0.95,
    color='r',
    linestyle='--',
    label='95% variância'
)

plt.axvline(
    x=n_components_95,
    color='g',
    linestyle='--',
    label=f'{n_components_95} componentes'
)

plt.xlabel('Número de Componentes')
plt.ylabel('Variância Explicada Acumulada')
plt.title('PCA - Elbow Method')
plt.grid(True)
plt.legend()

plt.show()
# %%
