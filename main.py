# X0: Eth amount 
# Y0: USDC amount
# T: position Value

# X0 in [X1, X2]
# Y0 in [Y1, Y2]

# X1 * Y2 = L ** 2
# X2 * Y1 = L ** 2 
# X0 * Y0 = L ** 2

# upper_price = Y2 / X1
# lower_price = Y1 / X2
# current_price = Y0 / X0

# X0 = L / sqrt(current_price)
# Y0 = L * sqrt(current_price)

# X1 = L / sqrt(upper_price)
# Y1 = L * sqrt(lower_price)

# X2 = L / sqrt(lower_price)
# Y2 = L * sqrt(upper_price)

# (X0 - X1) * current_price + (Y0 - Y1) = T
# L * ((sqrt(upper_price) - sqrt(current_price)) * sqrt(current_price) / sqrt(upper_price) + sqrt(current_price) - sqrt(lower_price)) = T

import math
import argparse

def calculate_price(k, m, x):
    if x == 0:
        return "x cannot be zero, as it would cause division by zero."
    
    price = k / (x ** 2) - m / x
    return price

def calculate_amount(k, m, p):
    if p == 0:
        return "price cannot be zero, as it would cause division by zero."
    
    amount = (math.sqrt(m * m + 4 * p * k) - m) / (2 * p)
    return amount

def main():
    current_tick_t0 = 202695
    position_upper_tick = 202980
    position_lower_tick = 202440
    position_value_t0 = 100000
    current_tick_t1 = 202000
    
    lower_price = 1.0001 ** position_lower_tick
    current_price = 1.0001 ** current_tick_t0
    upper_price = 1.0001 ** position_upper_tick

    L = position_value_t0 / ((upper_price ** 0.5 - current_price ** 0.5) * current_price ** 0.5 / upper_price ** 0.5 + current_price ** 0.5 - lower_price ** 0.5) 
    
    X0 = L / current_price ** 0.5
    Y0 = L * current_price ** 0.5

    X1 = L / upper_price ** 0.5
    Y1 = L * lower_price ** 0.5

    X2 = L / lower_price ** 0.5
    Y2 = L * upper_price ** 0.5

    X = X0 - X1
    Y = Y0 - Y1

    print("L = ", L)
    print("ETH amount = ", X0)
    print("USDC amount = ", Y0)
    
if __name__ == "__main__":
    main()