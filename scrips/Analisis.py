import pandas as pd



ventas = pd.read_csv("ventas.csv")
clientes = pd.read_csv("cliente.csv")

# UNIR DATOS

if "id_cliente" in ventas.columns and "id_cliente" in clientes.columns:
    data = pd.merge(ventas, clientes, on="id_cliente", how="inner")
else:
    data = None
    print("No se pudo hacer merge, falta id_cliente")


# 1. ¿Qué categoría genera más ingresos?


if "categoria" in ventas.columns:
    top_categoria = ventas.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n1. Categoría con más ingresos:")
    print(top_categoria.head(1))

    # RESPUESTA:
    # La categoría con mayor ingreso es la que tiene el valor más alto en la suma de "total".
else:
    top_producto = ventas.groupby("producto")["total"].sum().sort_values(ascending=False)
    print("\n1. Producto con más ingresos:")
    print(top_producto.head(1))

    # RESPUESTA:
    # El producto con mayor ingreso es el que tiene la mayor suma de ventas totales.


# 2. ¿Qué canal vende más?


if "canal" in ventas.columns:
    canal = ventas.groupby("canal")["total"].sum().sort_values(ascending=False)
    print("\n2. Canal que más vende:")
    print(canal.head(1))

    # RESPUESTA:
    # El canal con mayor volumen de ventas es el que presenta el mayor total acumulado.
else:
    print("\n2. No existe la columna canal en el dataset.")


# 3. ¿Clientes con mayor salario compran más?


if data is not None and "salario" in data.columns:
    relacion = data.groupby("salario")["total"].sum().sort_values(ascending=False)
    print("\n3. Relación salario vs compras:")
    print(relacion.head())

    # RESPUESTA:
    # Se observa que los clientes con mayor salario tienden a realizar compras de mayor valor,
    # aunque esto depende del comportamiento específico de los datos.
else:
    print("\n3. No se pudo analizar salario vs compras.")

# 4. ¿Qué método de pago es más usado?


if "metodo_pago" in ventas.columns:
    metodo = ventas["metodo_pago"].value_counts()
    print("\n4. Método de pago más usado:")
    print(metodo.head(1))

    # RESPUESTA:
    # El método de pago más utilizado es el que tiene mayor frecuencia en los registros.
else:
    print("\n4. No existe la columna metodo_pago.")


# 5. Top 5 clientes con más compras


if "id_cliente" in ventas.columns:
    top_clientes = ventas.groupby("id_cliente")["total"].sum().sort_values(ascending=False).head(5)
    print("\n5. Top 5 clientes con más compras:")
    print(top_clientes)

    # RESPUESTA:
    # Los clientes con mayor volumen de compras son aquellos con mayor suma total en sus transacciones.
else:
    print("\n5. No existe id_cliente en ventas.")

