def main(*args):
    if not args:
        return 0
    return sum(args) / len(args)

if __name__ == "__main__":
    numbers = [13, 26, 39, 52, 65]
    average = main(*numbers)
    print({average})
