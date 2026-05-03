import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv("ventas.csv")
clientes = pd.read_csv("cliente.csv")
#  ANTES
print("\nANTES DE LIMPIEZA:")
print(ventas.head())
print(clientes.head())

#  VALORES NULOS
print("\nVALORES NULOS:")
clientes_sin_nulos = clientes.dropna()
print(clientes_sin_nulos.head())

#limpiesa
clientes["edad"] = clientes["edad"].fillna(0)

# eliminar duplicados
ventas = ventas.drop_duplicates()
clientes = clientes.drop_duplicates()

clientes["edad"]=pd.to_numeric(clientes["edad"],errors="coerce")
clientes["salario"]=pd.to_numeric(clientes["salario"],errors="coerce")
ventas["total"] = pd.to_numeric(ventas["total"], errors="coerce")

#limpiesa de texto

if "ciudad" in clientes.columns:
    clientes["ciudad"] = clientes["ciudad"].str.strip().str.title()

if "activo" in clientes.columns:
    clientes["activo"] = clientes["activo"].str.upper()


if "producto" in ventas.columns:
    ventas["producto"] = ventas["producto"].str.strip().str.title()

if "fecha_registro" in clientes.columns:
    clientes["fecha_registro"] = pd.to_datetime(clientes["fecha_registro"], errors="coerce")

if "fecha_venta" in ventas.columns:
    ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"], errors="coerce")


clientes = clientes.fillna(0)
ventas = ventas.fillna(0)


print("\nDESPUÉS DE LIMPIEZA:")
print(ventas.head())
print(clientes.head())

print("\nTIPOS DE DATOS:")
print(ventas.dtypes)
print(clientes.dtypes)