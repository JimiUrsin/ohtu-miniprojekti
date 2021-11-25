from cli import CLI


def main():
    print("Hello world!")
    repository = None
    UI = CLI(repository)
    UI.start()


if __name__ == '__main__':
    main()
