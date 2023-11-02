import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_int(level)
        y = generate_int(level)
        for n in range(3):
            result = int(input(f'{x} + {y} = '))
            if result == x + y:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f'{x} + {y} = {x + y}')
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            lvl = int(input('Level: '))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


def generate_int(number):
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    return random.randint(*ranges[number])


if __name__ == "__main__":
    main()

