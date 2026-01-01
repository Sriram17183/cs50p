import random

def main():
    level = get_level()
    score = 0

    # Ask 10 questions
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        counter = 3  # 3 attempts per problem

        while counter > 0:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == a + b:
                    score += 1
                    break
                else:
                    counter -= 1
                    print("EEE")
            except ValueError:
                counter -= 1
                print("EEE")

            if counter == 0:
                print(f"{a} + {b} = {a + b}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
