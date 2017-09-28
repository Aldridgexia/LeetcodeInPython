class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Variable a tells you the number of ways to reach the current step, and b tells you the number of ways to reach the next step
        """

        a,b = 1,1
        for _ in range(n):
            a,b = b,a + b
        return a
