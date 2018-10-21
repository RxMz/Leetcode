class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tracker = {}
        start, end, maxlen = 0, 0, 0
        while start < len(s) and end < len(s):
            if s[end] not in tracker:
                tracker[s[end]] = 1
                maxlen = max(maxlen, len(tracker))
                end+=1
            else:
                tracker.pop(s[start], None)
                start+=1
        return maxlen
        