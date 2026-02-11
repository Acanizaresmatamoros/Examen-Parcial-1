import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Tienda de Electrodomésticos - Examen", layout="wide")

productos = [
    {"Nombre": "Refrigeradora", "Precio": 15000, "Categoría": "Línea Blanca"},
    {"Nombre": "Lavadora", "Precio": 12000, "Categoría": "Línea Blanca"},
    {"Nombre": "Microondas", "Precio": 3500, "Categoría": "Cocina"},
    {"Nombre": "Licuadora", "Precio": 1200, "Categoría": "Cocina"},
    {"Nombre": "Aire acondicionado", "Precio": 18000, "Categoría": "Climatización"},
    {"Nombre": "Plancha", "Precio": 800, "Categoría": "Hogar"},
    {"Nombre": "Televisor", "Precio": 10500, "Categoría": "Electrónica"},
    {"Nombre": "Cafetera", "Precio": 2200, "Categoría": "Cocina"},
]

df_productos = pd.DataFrame(productos)

st.title("Tienda de Electrodomésticos (Examen I Parcial)")
st.markdown("---")

st.header("Catálogo de Productos")
filtro_precio = st.slider("Filtrar por precio máximo:", 0, 20000, 20000)
df_filtrado = df_productos[df_productos["Precio"] <= filtro_precio]
st.dataframe(df_filtrado, use_container_width=True)

st.header("Selección y Carrito")
col1, col2 = st.columns(2)

with col1:
    producto_nombre = st.selectbox("Seleccione un producto del catálogo:", df_filtrado["Nombre"])
    datos_prod = df_filtrado[df_filtrado["Nombre"] == producto_nombre].iloc[0]
    precio_unitario = datos_prod["Precio"]
    
    st.info(f"Precio Unitario: L. {precio_unitario:,.2f}")

with col2:
    cantidad = st.number_input("Cantidad:", min_value=1, value=1, step=1)
    subtotal_prod = precio_unitario * cantidad
    st.success(f"Subtotal del producto: L. {subtotal_prod:,.2f}")

st.markdown("---")
st.header("Datos del Cliente y Facturación")

with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        nombre_cliente = st.text_input("Nombre del Cliente:")
    with c2:
        rtn_identidad = st.text_input("RTN / Identidad:")
    with c3:
        fecha = st.date_input("Fecha de Facturación", date.today())

if st.button("Generar Factura"):
    if nombre_cliente and rtn_identidad:
        st.markdown("### --- FACTURA FINAL ---")
        
        isv = subtotal_prod * 0.15
        total_pagar = subtotal_prod + isv
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.write(f"**Cliente:** {nombre_cliente}")
            st.write(f"**ID/RTN:** {rtn_identidad}")
            st.write(f"**Fecha:** {fecha}")
        
        with col_f2:
            st.write(f"**Producto:** {producto_nombre}")
            st.write(f"**Cantidad:** {cantidad}")
            st.write(f"**Precio Unitario:** L. {precio_unitario:,.2f}")

        st.markdown("---")
        totales = {
            "Descripción": ["Subtotal General", "ISV (15%)", "TOTAL A PAGAR"],
            "Monto (L.)": [f"{subtotal_prod:,.2f}", f"{isv:,.2f}", f"{total_pagar:,.2f}"]
        }
        st.table(pd.DataFrame(totales))
    else:
        st.error("Por favor complete los datos del cliente para generar la factura.")
