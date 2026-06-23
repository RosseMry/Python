from typing import List, Union

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    #validation of longitud
    if len(height) != len(weight):
        raise ValueError("The lists should have the same longitud.")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or isinstance(h, bool):
            raise TypeError(f"The height '{h}'  is not a valid number.\n")
        if not isinstance(w, (int,float)) or isinstance(w, bool):
            raise TypeError(f"The weight '{w}' is not a valid number.\n")

    #list comprehesion
    bmi : list[int | float]
    bmi = [ w / (h **2) for w,h in zip(weight, height)]
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    #validation of limit
    if limit <= 0:
        raise ValueError("Limit should be a number above 0")

    for b in bmi:
        if not isinstance(b, (int,float)) or isinstance(h, bool):
            raise TypeError(f"The value {b} should be a number\n")

    return [b > limit for b in bmi]