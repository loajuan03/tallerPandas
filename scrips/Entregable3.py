import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv("ventas.csv")
clientes = pd.read_csv("cliente.csv")

# PASO 1

print("\nUSO DE ILOC (por posición):")
print(ventas.iloc[:5])

print("\nUSO DE LOC (por condición):")
if "total" in ventas.columns:
    print(ventas.loc[ventas["total"] > 100])


# PASO 2:

print("\nVENTAS POR PRODUCTO:")
ventas_producto = ventas.groupby("categoria")["total"].sum()
print(ventas_producto)


# PASO 3: 


print("\nSPLIT Y COMBINE (get_group):")

grupo = ventas.groupby("producto")

primer_producto = ventas["producto"].iloc[0]

grupo_especifico = grupo.get_group(primer_producto)

print(f"\nDatos del producto: {primer_producto}")
print(grupo_especifico.head())


# PASO 4: 

print("\nMERGE:")

if "id_cliente" in ventas.columns and "id_cliente" in clientes.columns:
    data = pd.merge(ventas, clientes, on="id_cliente")
    print(data.head())
else:
    print("No se puede hacer merge (falta id_cliente)")


# PASO 5: 

print("\nCONCAT:")

df_total = pd.concat([ventas, clientes])
print(df_total.head())