from typing import List, Tuple

coin_values = [25, 10, 5, 1]
cached_values = {}


def find_min_coins(amount: int) -> Tuple[int, List]:
    if amount in cached_values:
        return cached_values[amount]
    if amount in coin_values:
        coin_counts = [1 if amount == i else 0 for i in coin_values]
        cached_values[amount] = (1, coin_counts)
        return cached_values[amount]
    values = [(find_min_coins(amount - i), i) for i in coin_values if amount > i]
    min_coins = min(values)
    coin_value_list = min_coins[0][1]
    current_coin_counts = [1 if min_coins[1] == i else 0 for i in coin_values]
    merged = [coin_value_list[i] + current_coin_counts[i] for i in range(len(coin_values))]
    # print(coin_value_list, current_coin_counts)

    cached_values[amount] = (min_coins[0][0] + 1, merged)
    return (min_coins[0][0] + 1, merged)


def string_concat(min_coins: Tuple):
    print(f'''
      Total Coins: {min_coins[0]}
     1 Cent Coins: {min_coins[1][3]}
     5 Cent Coins: {min_coins[1][2]}
    10 Cent Coins: {min_coins[1][1]}
    25 Cent Coins: {min_coins[1][0]}''')


string_concat(find_min_coins(63))