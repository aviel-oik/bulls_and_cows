import random
from turtledemo.penrose import start


def generate_secret(length: int = 4, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None = None) -> str:
     secret = ""
     for i in range(length):
        if not allow_leading_zero and i == 0:
            secret += str(random.randint(0, 9))
        else:
            secret += str(random.randint(0, 9))
     if unique_digits:
        while not len(set(secret)) == len(secret):
            secret = ""
            for i in range(length):
                if not allow_leading_zero and i == 0:
                    secret += str(random.randint(0, 9))
                else:
                    secret += str(random.randint(0, 9))
     return secret



















