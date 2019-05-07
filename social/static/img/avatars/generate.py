from subprocess import run

COLORS = ("red", "green", "blue", "yellow")


def main(amount: int = 4, size: int = 400) -> None:
    """Generates a set of avatars from pure
    colors."""

    for color, opt in zip(COLORS, range(1, amount + 1)):
        run(["convert", f"xc:{color}[{size}x{size}!]", f"avatar_{opt}.png"])


if __name__ == "__main__":
    import sys

    main(*sys.argv[1:])
