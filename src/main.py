from cli import CLI


def main():
    print("Hello world!")
    service = None
    UI = CLI(service)
    UI.start()


if __name__ == '__main__':
    main()
