import game.secret
import game.logic
import game.io
import game.validate


def main():
    length = input("How long would you like to play? ")
    play(int(length))
    pass


def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret = game.secret.generate_secret(length, unique_digits, allow_leading_zero)
    state = game.logic.init_state(secret, length, max_tries, unique_digits, allow_leading_zero)
    while max_tries > 0:
        guess = game.io.prompt_guess(length)
        valid = game.validate.is_valid_guess(guess, length, unique_digits)
        if not valid[0]:
            print(valid[1])
            continue
        if not game.validate.is_new_guess(guess, state["seen"]):
            print("you need to enter a new guess")
            continue
        if max_tries is not None:
            max_tries -= 1
        bulls, cows = game.logic.apply_guess(state, guess)
        game.io.print_feedback(guess, bulls, cows)
        game.io.print_status(state)
        won = False
        if state["secret"] == guess:
            won = True
            game.io.print_result(state, won)
            break
        game.io.print_result(state, won)



if __name__ == "__main__":
    main()



