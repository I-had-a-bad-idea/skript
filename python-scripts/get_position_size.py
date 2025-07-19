#!/usr/bin/env python3

# get_position_size.py
# Calculates the position size of a trade.
#
# Billy Wilson Arante <arantebillywilson@gmail.com>
# Mon 01 Jun 2020 01:42:45 PM PST 

import sys

def main(portfolio_size):
    position_size = float(portfolio_size) * 0.01 / 0.05
    print('{:,.2f}'.format(position_size))


if __name__ == '__main__':
    portfolio_size = sys.argv[1]
    main(portfolio_size)
