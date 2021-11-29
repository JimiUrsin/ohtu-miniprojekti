from cli import CLI
from entities.recommendation import Recommendation


def main():
    print("Hello world!")
    service = None
    UI = CLI(service)
    UI.start()


if __name__ == '__main__':
    main()
