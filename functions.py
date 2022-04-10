def distancia(de, valor, para):
    if (de == 1):
        if (para == 1):
            return valor
        elif (para == 2):
            return valor / 100
        elif (para == 3):
            return valor / (100 * 1000)
    if (de == 2):
        if (para == 1):
            return valor * 100
        elif (para == 2):
            return valor
        elif (para == 3):
            return valor / 1000
    if (de == 3):
        if (para == 1):
            return valor * (100 * 1000)
        elif (para == 2):
            return valor * 1000
        elif (para == 3):
            return valor

def tempo(de, valor, para):
    if (de == 1):
        if (para == 1):
            return valor
        elif (para == 2):
            return valor / 60
        elif (para == 3):
            return valor / (60 * 60)
    if (de == 2):
        if (para == 1):
            return valor * 60
        elif (para == 2):
            return valor
        elif (para == 3):
            return valor / 60
    if (de == 3):
        if (para == 1):
            return valor * (60 * 60)
        elif (para == 2):
            return valor * 60
        elif (para == 3):
            return valor

def velocidade(de, valor, para):
    if (de == 1):
        if (para == 1):
            return valor
        elif (para == 2):
            return valor * 3.6
    if (de == 2):
        if (para == 1):
            return valor / 3.6
        elif (para == 2):
            return valor

def temperatura(de, valor, para):
    if (de == 1):
        if (para == 1):
            return valor
        elif (para == 2):
            return valor - 273.15
        elif (para == 3):
            return ((valor - 273.15) * 1.8) + 32
    if (de == 2):
        if (para == 1):
            return valor + 273.15
        elif (para == 2):
            return valor
        elif (para == 3):
            return (valor * 1.8) + 32
    if (de == 3):
        if (para == 1):
            return valor * (60 * 60)
        elif (para == 2):
            return (valor - 32) / 1.8
        elif (para == 3):
            return valor
