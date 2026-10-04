class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        coins.sort()
        def backtrack(amount):

            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if amount in cache:
                return cache[amount]
            
            fewestNumberOfCoins = float("inf")

            for coin in coins:
                NumberOfCoins = backtrack(amount - coin)
                fewestNumberOfCoins = min(fewestNumberOfCoins,NumberOfCoins + 1)

            cache[amount] = fewestNumberOfCoins
            return cache[amount]

        res = backtrack(amount)

        return res if res != float("inf") else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         fewestNumberOfCoins = float("inf")
#         cache = set()
#         coins.sort()
#         def backtrack(state, currentSum):
#             nonlocal fewestNumberOfCoins
#             sumCoins = sum(currentSum)


#             if state < 0 or sumCoins > amount:
#                 return

#             if sumCoins == amount:
#                 fewestNumberOfCoins = min(fewestNumberOfCoins, len(currentSum))
#                 return
 
#             currentSum.append(coins[state])
#             cache.add((sumCoins,len(currentSum)))

#             if ((sumCoins + coins[state]),len(currentSum)+1) not in cache:
#                 backtrack(state, currentSum)
#             currentSum.pop()
#             if state != 0 and ((sumCoins + coins[state-1]),len(currentSum)+1) not in cache:
#                 backtrack(state - 1, currentSum)

#         backtrack(len(coins)-1, [])

#         return fewestNumberOfCoins if fewestNumberOfCoins != float("inf") else -1
