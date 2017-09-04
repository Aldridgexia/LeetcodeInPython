class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        max_idx = 0
        max_val = s[0]
        for i, val in enumerate(s):
            if val >= max_val:
                max_idx = i
                max_val = val
        if len(s) == 1:
            return int(s)
        elif max_idx != 0 and max_val != s[0]:
            return int(s[max_idx] + s[1:max_idx] + s[0] + s[max_idx + 1:])
        else:
            return int(s[0]) * 10**(len(s) - 1) + self.maximumSwap(s[1:])
