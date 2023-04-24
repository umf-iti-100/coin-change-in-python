def askInteger(msg):

    value = input(msg)

    value = int(value)

    return value


def toCents(value):

    return "(" + str(value) + u"\u00A2"+")"


def printLine():

    print("---------------------------------------")


def convertToCoins(amount):

    if amount < 0 or amount > 99:
        raise ValueError("The amount is valid")

    quarters = amount // 25
    amount %= 25

    dimes = amount // 10
    amount %= 10

    nickels = amount // 5
    amount %= 5

    pennies = amount % 5

    return (quarters, dimes, nickels, pennies)


def main():

    amount = askInteger("Please enter an amount between 0-99: ")

    while amount != -1:

        (quarters, dimes, nickels, pennies) = convertToCoins(amount)

        printLine()
        print(quarters, "quarters", "\t", toCents(25))
        print(dimes, "dimes", "\t", toCents(10))
        print(nickels, "nickels", "\t", toCents(5))
        print(pennies, "pennies", "\t", toCents(1))
        printLine()

        amount = askInteger("Please enter an amount between 0-99: ")

    print("Thank you")

if __name__ == "__main__":

    try:
        main()
    except ValueError as error:
        printLine()
        print("Ooops!", error)
        printLine()
