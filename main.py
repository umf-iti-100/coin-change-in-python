def askInteger(msg):

    value = input(msg)

    value = int(value)

    return value


def toCents(value):

    return "(" + str(value) + u"\u00A2"+")"


def convertToCoins(amount):

    if amount < 0 or amount > 99:
        raise ValueError("amount should be between [0-99]")

    half = amount // 50
    amount %= 50

    quarters = amount // 25
    amount %= 25

    dimes = amount // 10
    amount %= 10

    nickles = amount // 5
    amount %= 5

    pennies = amount % 5

    return (half, quarters, dimes, nickles, pennies)


def main():

    amount = askInteger("Please enter an amount between 0-99: ")

    (half, quarters, dimes, nickles, pennies) = convertToCoins(amount)

    print("---------------------------------------")
    print(half, "half dollar", "\t", toCents(50))
    print(quarters, "quarters", "\t", toCents(25))
    print(dimes, "dimes", "\t", toCents(10))
    print(nickles, "nickles", "\t", toCents(5))
    print(pennies, "pennies", "\t", toCents(1))
    print("---------------------------------------")

if __name__ == "__main__":
    main()
