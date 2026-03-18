"""Simple hello world program for learners."""


def get_greeting() -> str:
    """Return the greeting message."""
    return "Hello, World!"


def main() -> None:
    """Entry point: print greeting to console."""
    message = get_greeting()
    print(message)


if __name__ == "__main__":
    main()