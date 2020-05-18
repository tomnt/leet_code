"""
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/
Runtime: 32 ms, faster than 80.56% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Restore IP Addresses.

https://leetcode.com/interview/2/
Success
Runtime: 72 ms
Memory Usage: 13.8 MB
"""


class Solution:

    def restoreIpAddresses(self, s: str) -> list:
        """
        :param str s:
        :return List[str]:
        """
        n = len(list(s))
        list_ip = []
        for d1 in range(1, 4):
            for d2 in range(1, 4):
                for d3 in range(1, 4):
                    for d4 in range(1, 4):
                        if n == d1 + d2 + d3 + d4:
                            block1 = s[0:d1]
                            block2 = s[d1:d1 + d2]
                            block3 = s[d1 + d2: d1 + d2 + d3]
                            block4 = s[d1 + d2 + d3: d1 + d2 + d3 + d4]
                            if self.in_range(block1)\
                                and self.in_range(block2)\
                                and self.in_range(block3)\
                                and self.in_range(block4):
                                    list_ip.append(block1+'.'+block2+'.'+block3+'.'+block4)
        return list_ip

    @staticmethod
    def in_range(block: str):
        if len(block) > 1 and block[0] == '0':
            return False
        return 0 <= int(block) <= 255


s = Solution()
# print('Example : Expected: ["255.255.11.135", "255.255.111.35"], Actual:', s.restoreIpAddresses("25525511135"))
print('Example : Expected: ["0.10.0.10","0.100.1.0"], Actual:', s.restoreIpAddresses("010010"))
