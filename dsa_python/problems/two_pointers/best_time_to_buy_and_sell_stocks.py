def best_time_to_sell(prices):
    if len(prices) <2:
        return 0
    low = prices[0]
    max_profit = 0
    for i in prices:
        if low > i:
            low = i
        elif i-low > max_profit:
            max_profit = i-low
    return max_profit
if __name__ == "__main__":
    prices=[7,5,3,5,6,4]
    print(best_time_to_sell(prices))
