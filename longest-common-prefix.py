class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """
        :param strs: list[str]
        :return:
        """
        if len(strs) > 0:
            l_common_prefix = list(strs.pop(0))
        else:
            return ''
        for s_val in strs:
            l_s_val = list(s_val)
            i = 0
            l_common_prefix_tmp = []
            for c_l_s_val in l_s_val:
                if i < len(l_common_prefix) and c_l_s_val == l_common_prefix[i]:
                    l_common_prefix_tmp.append(c_l_s_val)
                else:
                    break
                i += 1
            l_common_prefix = l_common_prefix_tmp
        return ''.join(l_common_prefix)


s = Solution()
print('1: '+s.longestCommonPrefix(["flower","flow","flight"]))
print('2: '+s.longestCommonPrefix(["dog","racecar","car"]))
print('3: '+s.longestCommonPrefix([]))
