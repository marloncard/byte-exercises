#!/usr/bin/env python3
"""
* Takes in a float as an argument
* Returns the number of American coins and bills needed to represent that float. (Round to the nearest penny)
"""


currency = {'hundred': 100,
            'fifty': 50,
            'ten': 10,
            'five': 5,
            'one': 1,
            'quarter': .25,
            'dime': .10,
            'nickel': .05,
            'penny': .01}

def currency_converter(amount):
# Iterate over currency dict
    for key, value in currency.items():
        # If amount divided by currency_item not < 0;
        if amount / value > 0:
            # Omit any zero results
            if amount // value > 0:
                # Print amount // currency_item => (print('{:.2f}'.format(amount)))
                print('{:.0f}'.format(amount // value) + ' ' + key)
                # amount = amount % currency_item
                amount = amount % value


if __name__ == "__main__":
    currency_converter(2345.18)