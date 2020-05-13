"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
Time Limit Exceeded
"""


class Solution:
    def networkDelayTime(self, times: list, N: int, K: int) -> int:
        """
        :param times: times: List[List[int]]
        :param N: int Number of network nodes
        :param K: int Initial node
        """
        dict_time = Solution.__get_dict_time(times, K)
        while True:
            len_dict_time_before = len(dict_time)
            dict_time_next = self.__get_dict_time_next_level(dict_time, times, K)
            dict_time.update(dict_time_next)
            len_dict_time_after = len(dict_time)
            if len_dict_time_before != len_dict_time_after:
                break
        return max(Solution.__get_list(dict_time))

    @staticmethod
    def __get_list(dict_values: dict)->list:
        list_time = []
        for k in dict_values:
            list_time.append(dict_values[k])
        return list_time

    @staticmethod
    def __get_dict_time_next_level(dict_time: dict, times: list, K: int) -> dict:
        dict_time_add = {}
        for key in dict_time:
            last_node = Solution.__get_last_node(key)
            dict_time_last_node = Solution.__get_dict_time(times, last_node)
            if len(dict_time_last_node) > 0:
                for key_last_node in dict_time_last_node:
                    dict_time_add[key + '.' + str(Solution.__get_last_node(key_last_node))] = dict_time[key] + \
                                                                                              dict_time_last_node[
                                                                                                  key_last_node]
        return dict_time_add

    @staticmethod
    def __get_last_node(key: str) -> int:
        return int(Solution.__get_dict(key.split('.'))[len(key.split('.')) - 1])

    @staticmethod
    def __get_dict_time(times: list, K: int) -> dict:
        # print('BBB',times, K)
        dict_time = {}
        for node in times:
            dict_node = Solution.__get_dict(node)
            if dict_node[0] == K:  # 0: 'source'
                dict_time[str(K) + '.' + str(dict_node[1])] = dict_node[2]  # 1: target, 2: time
        return dict_time

    @staticmethod
    def __get_dict(list_value: list) -> dict:
        dict_l = {}
        for k, value in enumerate(list_value):
            dict_l[k] = value
        return dict_l


s = Solution()
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2))
