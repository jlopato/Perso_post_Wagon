def square_digits(num):
    # outut == int mettre au carré chaque chiffre du nombre
    # i doit itérer le nombre donc le nombre doit être une string
    # puis à chaque valeur on applique le carré et puis on l'ajoute à la string
    # nombre = "nombre" après for i in nombre: i = i**2 nombre += "nombre"
    # puis return "".join(nombre)

    nombre = ""
    num = str(num)
    for n in num:
        n = str(int(n)**2)
        nombre += n
    nombre =int(nombre)

    return nombre

square_digits(9119)
