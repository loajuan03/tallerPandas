import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Leer archivos con usecols
ventas = pd.read_csv("ventas.csv", usecols=["id_venta", "producto", "total"])
clientes = pd.read_csv("cliente.csv", usecols=["id_cliente", "salario"])

print("SHAPE VENTAS:", ventas.shape)
print("SHAPE CLIENTES:", clientes.shape)

print("\nINFO VENTAS")
ventas.info()

print("\nINFO CLIENTES")
clientes.info()

print("\nDESCRIBE VENTAS")
print(ventas.describe())

# Notación punto
print("\nNotación punto:")
print(ventas.total.head())

# Indexación
if "id_venta" in ventas.columns:
    ventas = ventas.set_index("id_venta")
    print("\nNuevo index:")
    print(ventas.index)
