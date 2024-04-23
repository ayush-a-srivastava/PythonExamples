import argparse

def StringConversion(name, to_upper, to_lower):
    if to_upper:
        print(name.upper())
    elif to_lower:
        print(name.lower())

def commandToConvert():
    parser = argparse.ArgumentParser(description="Convert string to UpperCase and LowerCase")
    parser.add_argument("-n", "--name", metavar="name", help="String to Convert")
    parser.add_argument("-u", "--to_upper", action="store_true", help="Convert string to UpperCase")
    parser.add_argument("-l", "--to_lower", action="store_true", help="Convert string to lowercase")
    args = parser.parse_args()

    if not args.name:
        print("Please provide a string to convert.")

    StringConversion(args.name, args.to_upper, args.to_lower)


if __name__ == "__main__":
    convert = True
    while convert:
        commandToConvert()
        choice = input("\nWant to convert again? Press Y for Yes or Q for Quit: ")
        if choice.lower() != "y":
            convert = False

