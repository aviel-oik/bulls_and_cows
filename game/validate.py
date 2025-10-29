

def is_valid_guess(guess: str, length: int, unique_digits: bool = True) -> tuple[bool, str]:
    if not len(guess) == length:
        return False, f"Guess must be of length {length}"
    if not guess.isdigit():
        return False, f"Guess must be a number"
    if unique_digits:
        if not len(set(guess)) == len(guess):
            return False, f"Guess must be unique digits"
    return True, ""



def is_new_guess(guess: str, seen) -> bool:
    if guess in seen:
        return False
    return True