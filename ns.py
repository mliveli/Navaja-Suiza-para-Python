def imprimir_ln(parametro):
    """
    Recibe un unico parametro.
    Imprime el parametro proporcionado con un salto de linea inicial y final
    print("\n", parametro, "\n")"""
    print("\n", parametro, "\n")


def imprimir(parametro):
    """
    Recibe un unico parametro.
    Imprime el parametro proporcionado"""
    print(parametro)


def imprimir_ln_separador(parametro):
    """
    Recibe un unico parametro.
    Imprime el parametro proporcionado con un salto de linea inicial y final incluyendo
    asteriscos como separadores.
    print("\n*********************************\n",parametro,"\n*********************************\n")"""
    print(
        "\n*********************************\n",
        parametro,
        "\n*********************************\n",
    )


def imprimir_flecha(parametro):
    """Recibe un unico parametro.
    Imprime el parametro proporcionado con un salto de linea inicial y una flecha antes del parametro.
    print("\n-----> ", parametro)
    """
    print("\n-----> ", parametro)


def imprimir_mi_separador(parametro, separador):
    """
    Recibe un 2 parametros.
    Imprime el parametro proporcionado con un salto de linea inicial y final incluyendo
    20 separadores proporcionados como segundo parametro.
    print("\n", separador * 20, "\n", parametro, "\n", separador * 20, "\n")"""
    print(
        "\n",
        separador * 20,
        "\n",
        parametro,
        "\n",
        separador * 20,
        "\n",
    )
