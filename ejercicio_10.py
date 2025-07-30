user_inventory = {}
def user_product():
    product_code = str(input("Ingrese el codigo del producto: "))
    if product_code in user_inventory:
        print("Codigo ya ingresado, vuelva a intentar")
        while True:
            product_code = str(input("Ingrese el codigo del producto: "))
            if product_code in user_inventory:
                print("Codigo ya ingresado, vuelva a intentar")
            else:
                break
    name_product = str(input("Nombre del producto: "))
    category_product = input("Categoría del prodcuto: ")
    size_product = input("Talla del producto: ")
    price_product = float(input("Ingrese el precio unitario del producto: "))
    if price_product < 0:
        print("El precio unitario debe ser mayor a Q0.00")
        while True:
            price_product = float(input("Ingrese el precio unitario del producto: "))
            if price_product < 0:
                print("El precio unitario debe ser mayor a Q0.00")
            else:
                break
    count_stock = int(input("Ingrese la cantidad de stock: "))
    if count_stock < 0:
        print("El stock debe ser mayor a 0")
        while True:
            count_stock = int(input("Ingrese la cantidad de stock: "))
            if count_stock < 0:
                print("El stock debe ser mayor a 0")
            else:
                break
    user_inventory[product_code] = {"nombre": name_product, "categoria": category_product,
                                    "talla": size_product, "precio": price_product, "stock": count_stock}

while True:
    print("Inventario de productos")
    print("1.- Agregar productos")
    print("2.- Visualizar producto")
    print("3.- Calcular total de inventario")
    print("4.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que desea ingresar: ")
    match menu_option:
        case "1":
            print("Agregar productos")
            user_product()
            print("")
        case "2":
            print("Lista de productos")
            code_product = str(input("Ingrese el codigo del producto a visualizar: "))
            if code_product in user_inventory:
                producto = user_inventory[code_product]
                print("Producto encontrado")
                print(f"Nombre del producto: {producto['nombre']}")
                print(f"Categoria del producto: {producto['categoria']}")
                print(f"Talla del producto: {producto['talla']}")
                print(f"Precio unitario del producto: {producto['precio']}")
                print(f"Stocks del producto: {producto['stock']}")
                print("")
            else:
                print("No se ha encontrado el producto")
        case "3":
            print("Total de inventario")
        case "4":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
