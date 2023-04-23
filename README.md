# Coin Change in Python
Convert an amount to half dollar, quarters, dimes, nickels, and pennies

## Requirements

You should install and run this project as Python `>= 3.11`. Please make sure you have the same version or higher installed on your machine.

## How to Run

```bash
python main.py
```

if you are using MacOS, you should run:

```bash
python3 main.py
```

## Example

When you run this tool, this is a possible output:

```sh
Please enter an amount between 0-99: 35
---------------------------------------
0 half dollar    (50¢)
1 quarters       (25¢)
1 dimes          (10¢)
0 nickles        (5¢)
0 pennies        (1¢)
---------------------------------------
```

The next screenshot is when the user types an invalid amount:

```sh
Please enter an amount between 0-99: 123
---------------------------------------
Ooops! The amount should be between [0-99]
---------------------------------------
```
