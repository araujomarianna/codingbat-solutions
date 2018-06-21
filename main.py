from string_2.cat_dog import cat_dog
from warmup_1.sleep_in import sleep_in


def main():

    print("Testing sleep_in function: ")
    print("sleep_in(False, False) → {}".format(sleep_in(False, False)))
    print("sleep_in(True, False) → {}".format(sleep_in(True, False)))
    print("sleep_in(False, True) → {}".format(sleep_in(False, True)))

    print("\nTesting cat_dog function: ")
    print("cat_dog('catdog') → {}".format(cat_dog('catdog')))
    print("cat_dog('catcat') → {}".format(cat_dog('catcat')))
    print("cat_dog('1cat1cadodog') → {}".format(cat_dog('1cat1cadodog')))


if __name__ == '__main__':
    main()
