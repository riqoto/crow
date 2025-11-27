from file import File


def main():
    print("Hello from stat!")


if __name__ == "__main__":
    f = File("/home/bhh/Belgeler/python/stat/stat/data.csv")
    print(f.Validate())
    main()
