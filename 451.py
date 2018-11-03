class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_freq = {}
        for i in s:
            if i not in dict_freq:
                dict_freq[i] = 1
            else:
                dict_freq[i]+=1
        list_freq = []
        for i in dict_freq:
            list_freq.append((i, dict_freq[i]))
        print(list_freq)
        list_freq.sort(key=lambda tup: tup[1])
        list_freq = list_freq[::-1]
        print(list_freq)
        to_ret = ""
        for i in list_freq:
            to_ret= to_ret + i[0]*i[1]
        return to_ret
        