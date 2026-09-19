class Solution:
    def climbStairs(self, n: int) -> int:
        
        # top down
        # def climb(n,cache):
        #     if n == 0: return 1
        #     if n < 0: return 0
        #     if n in cache: return cache[n]

        #     cache[n] = climb(n-1,cache) + climb(n-2,cache)
        #     return cache[n]
        
        # return climb(n,{})

        # bottom up
        if n < 2: return 1
        if n == 2: return 2
        cache = [0 for num in range(n+1)]
        cache[0] = 1
        cache[1] = 1
        cache[2] = 2
        i = 3
        while i < n+1:
            cache[i]= cache[i-1] + cache[i-2]
            i += 1

        return cache[n]