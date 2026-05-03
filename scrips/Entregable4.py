import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
ventas = pd.read_csv("ventas.csv")
clientes = pd.read_csv("cliente.csv")

# -------------------------------
# GRÁFICO 1: Ventas por categoría (o producto)
# -------------------------------

if "categoria" in ventas.columns:
    ventas.groupby("categoria")["total"].sum().plot(kind="bar")
    plt.title("Ventas por categoría")
else:
    ventas.groupby("producto")["total"].sum().plot(kind="bar")
    plt.title("Ventas por producto")

plt.savefig("grafico1.png")
plt.clf()

# -------------------------------
# GRÁFICO 2: Método de pago
# -------------------------------

if "metodo_pago" in ventas.columns:
    sns.countplot(data=ventas, x="metodo_pago")
    plt.title("Método de pago")
    plt.savefig("grafico2.png")
    plt.clf()
else:
    print("No existe la columna metodo_pago")

# -------------------------------
# GRÁFICO 3: Relación salario vs puntaje
# -------------------------------

if "salario" in clientes.columns and "puntaje" in clientes.columns:
    sns.scatterplot(data=clientes, x="salario", y="puntaje")
    plt.title("Relación salario vs puntaje")
    plt.savefig("grafico3.png")
    plt.clf()
else:
    print("No existen columnas salario/puntaje")