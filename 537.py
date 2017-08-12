class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r1, i1 = a.split('+')
        r1, i1 = int(r1), int(i1[:-1])
        r2, i2 = b.split('+')
        r2, i2 = int(r2), int(i2[:-1])
        
        r3 = r1 * r2 - i1 * i2
        i3 = r1 * i2 + r2 * i1
        
        result = str(r3) + '+' + str(i3) + 'i'
        return result
