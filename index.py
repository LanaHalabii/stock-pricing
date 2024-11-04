def max_profit(prices):                                 #define function max_profit that takes as parameter prices
                                                
    profit = []                                         #define profit as an array where we will store the profits made
    for i in range(len(prices)):
        if i == 0:                                      #if the index is the first one then there will surely be no profit
            continue
        elif prices[i] > prices[i-1]:                   #if today's price is greater than yesterday, then we made a profit
            profit.append(prices[i] - prices [i-1])     #append the profit to the array
    
    print(max(profit))                                  #print the maximum profit made of all the profits
    
    return

array_prices=[10, 16, 19, 15, 21, 50, 9]
max_profit(array_prices)



