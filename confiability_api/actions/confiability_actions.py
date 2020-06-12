from tool_round import round_up
from tool_round import round_down

_default_addition = 0.02
_default_decrease = 0.04

def addition(confidence:float):
    confidence = confidence + (confidence * _default_addition)
    return confidence

def decrease(confidence:float):
    confidence = confidence - (confidence * _default_decrease)
    return confidence

def calculate_actual_confidence(confidence:int,positive_values:int,negative_values:int):
    temp_confidence = confidence
    if positive_values > 0:
        for i in range(0,positive_values):            
            temp_confidence = round_down(addition(temp_confidence),0)
    if negative_values  > 0:
        for i in range(0,negative_values):
            temp_confidence = round_up(decrease(temp_confidence),0)
    return temp_confidence