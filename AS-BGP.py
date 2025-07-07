x = input("\nIngresa AS BGP (0-65535):\n")

x = int(x)

if 0 <= x <= 65535:
    if 1 <= x <= 64495:
        print("El AS se encuentra en el rango público.")
    elif x == 0 or x == 65535:
        print("El AS está reservado y no se puede utilizar.")
    elif 64496 <= x <= 64511:
        print("El AS está reservado para motivos especiales.")
    elif 64512 <= x <= 65534:
        print("El AS es privado.")
else:
    print("El número ingresado está fuera del rango válido (0-65535).")
