'''
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create 2 pointers left and right, left starts 0 and right starts 1
        l, r = 0, 1
        # create a variable to max profit
        maxP = 0
        # create while loop that goes through the length of prices
        while r < len(prices):
            #if left is less than right
            if prices[l] < prices[r]:
                
                # calculate profit where profit = right - left
                profit = prices[r] - prices[l]
                # use max function to pick the max of profit and max profit
                maxP = max(maxP, profit)
            # else left takes the place of right
            else:
                l = r
            # right moves up one value
            r += 1
        # return the max profit
        return maxP
    
    
print(Solution().maxProfit(prices = [7,1,5,3,6,4]))