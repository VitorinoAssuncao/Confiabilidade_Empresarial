import math

def round_up(value:float,decimals:int):
    multiplier = 10 ** decimals
    return math.ceil(value * multiplier) / multiplier

def round_down(value:float,decimals:int):
    multiplier = 10 ** decimals
    return math.floor(value * multiplier) / multiplier