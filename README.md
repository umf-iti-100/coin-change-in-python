# Coin Change in Python

Convert an amount to quarters, dimes, nickels, and pennies

[![GitHub Release](https://img.shields.io/github/release/umf-iti-100/coin-change-in-python.svg)](https://github.com/umf-iti-100/coin-change-in-python/releases/latest)
[![GitHub contributors](https://img.shields.io/github/contributors/umf-iti-100/coin-change-in-python.svg)](https://github.com/umf-iti-100/coin-change-in-python/graphs/contributors)
[![GitHub stars](https://img.shields.io/github/stars/umf-iti-100/coin-change-in-python.svg)](https://github.com/umf-iti-100/coin-change-in-python)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Requirements

You should install and run this project as Python `>= 3.11`. Please make sure you have the same version or higher installed on your machine.

## How to Run

Download this project on your computer. Then, open the terminal/console on your computer and navigate to where you downloaded it. Finally, type the following command:

```bash
python main.py
```

However, if you are using MacOS, you should type:

```bash
python3 main.py
```

## Example

When you run this tool, this is a possible output:

```sh
Please enter an amount between 0-99: 35
---------------------------------------
1 quarters       (25¢)
1 dimes          (10¢)
0 nickles        (5¢)
0 pennies        (1¢)
---------------------------------------
```

The next screenshot is when the user types an invalid amount:

```sh
Please enter an amount between 0-99: -1
---------------------------------------
Ooops! The amount is valid
---------------------------------------
```

## To-Do

These are the features planned for future versions:

- Add documentation for all functions
- Add unit tests
- Add support to `half a dollar (50¢)`
- Increase the valid range to `[0-500]`
- Add support to [python-string-utils](https://pypi.org/project/python-string-utils/) to validate the user's input

## Acknowledgment

I would like to thank Marwa and Justin for this idea

## Questions or Suggestions

Feel free to access the <a href="../../discussions">discussions tab</a> as you need

## Contribute

Contributions to this project are very welcome! We can't do this alone! Feel free to fork this project, work on it and then make a pull request.

## License

Licensed under the [MIT license](LICENSE).
