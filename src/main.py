# Generate a function that accepts an integer parameter and squares it;
# annotate the function incorrectly (for static typing demonstration).

def parse_int_from_input(prompt: str = "Enter a number: ") -> int:
    user_input = input(prompt)
    try:
        return int(user_input)
    except ValueError:
        raise ValueError(f"Invalid integer: {user_input}")

# Incorrect annotation intentionally: return type should be int.
def square(x: int) -> str:
    return x ** 2

def main():
    try:
        value = parse_int_from_input()
        result = square(value)
        print(f"The square of {value} is {result}")
    except ValueError as err:
        print(err)

if __name__ ==  "__main__":
    main()