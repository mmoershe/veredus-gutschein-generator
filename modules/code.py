from modules.counter import counter

import random 


def generate_code() -> str:
    code_content: list = ["ABCDEFGHJKLMNPQRSTUVWXYZ"]
    # ALTERNATIVE: ["ABCDEFGHJKLMNPQRSTUVWXYZ23456789"]
    first_half: str = "".join([random.choice(code_content[0]) for _ in range(4)])
    counter_value: int = counter()
    second_half: str = "X" + str(counter_value).zfill(3)
    return first_half + second_half
