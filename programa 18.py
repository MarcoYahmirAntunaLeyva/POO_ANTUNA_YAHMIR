productos = {
    "Manzana" : 0.50,
    "Pera" : 0.75,
    "Uva" : 1.20,
    "Platano" : 0.80,
    "Naranja" : 0.60,
}

descuento = 0.1

for producto, precio in productos.items():
    precio_descuento = precio *(1 - descuento)
    productos[producto] = precio_descuento
    print(f"{producto}: {precio:.2f} -> {precio_descuento:.2f}")