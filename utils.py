from math import sqrt, acos, degrees, cos, sin, radians

class Vector():
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y

def distance(_v1: Vector, _v2: Vector):
    v_x = _v1.x - _v2.x
    v_y = _v1.y - _v2.y
    
    return Vector(v_x, v_y)

def dir(_v1: Vector, _v2: Vector):
    vx1 = _v1.x
    vy1 = _v1.y
    vx2 = _v2.x
    vy2 = _v2.y
    
    v_x = vx1 - vx2
    v_y = vy1 - vy2

    # Calcular a magnitude do vetor
    magnitude = sqrt(v_x**2 + v_y**2)

    # Normalizar o vetor
    if (magnitude != 0):
        v_x_normalized = v_x / magnitude
        v_y_normalized = v_y / magnitude
    else:
        return Vector(0, 0)

    return Vector(v_x_normalized, v_y_normalized)

