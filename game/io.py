

def prompt_guess(length: int) -> str:
    return input("Please enter a guess: ")



def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"in {guess} you have {bulls} bulls and {cows} cows")



def print_status(state: dict) -> None:
    print(f"You have {str(state["max_tries"] - state["tries_used"])} tries left")



def print_result(state: dict, won: bool) -> None:
    if won:
        print("You won!")




