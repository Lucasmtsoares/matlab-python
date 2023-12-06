import math

def catersianaTo_polar(x, y):
    raio = math.sqrt(x**2 + y**2)
    rad = math.atan2(y,x)
    graus = math.degrees(rad)

    print(f'raio: {raio}')
    print(f'Angulo em rad: {rad}')
    print(f'Angulo em graus: {graus}')

def polarTo_cartesiana(r, angulo_rad):
    x = r * math.cos(angulo_rad)
    y = r * math.sin(angulo_rad)

    print(f'coordenas catersianas: (x,y) - ({x}, {y})')



