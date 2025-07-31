user_inventory = {}
def user_product():
    count_products = int(input("Ingrese la cantidad de productos a ingresar: "))
    for i in range(count_products):
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
        print()

def visualizar_productos(code_product):
    if code_product in user_inventory:
        producto = user_inventory[code_product]
        print("Producto encontrado")
        print(f"Nombre del producto: {producto['nombre']}")
        print(f"Categoria del producto: {producto['categoria']}")
        print(f"Talla del producto: {producto['talla']}")
        print(f"Precio unitario del producto: {producto['precio']}")
        print(f"Stocks del producto: {producto['stock']}")
    else:
        print("No se ha encontrado el producto")

while True:
    print("Inventario de productos")
    print("1.- Agregar productos")
    print("2.- Visualizar producto")
    print("3.- Calcular total de inventario")
    print("4.- Productos por categoria")
    print("5.- Salir del programa")
    menu_option = input("Ingrese el número de la opción que desea ingresar: ")
    match menu_option:
        case "1":
            print("Agregar productos")
            user_product()
            print()
        case "2":
            print("Lista de productos")
            code_product = str(input("Ingrese el codigo del producto a visualizar: "))
            visualizar_productos(code_product)
            print()
        case "3":
            print("Total de inventario")
            total_price = 0
            for precio in user_inventory.values():
                total_price = total_price + precio['precio'] * precio['stock']
            print(f"El precio total del inventario es de: {total_price}")
        case "4":
            categorias1 = {}
            for cate, catego in user_inventory.items():
                categorias2 = catego.get('categoria')
                if categorias2:
                    if categorias2 in categorias1:
                        categorias1[categorias2] += 1
                    else:
                        categorias1[categorias2] = 1
            print("Cantidad de productos por categoria")
            for categoria3, dicc in categorias1.items():
                print(f"{categoria3}:{dicc}")
        case "5":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
