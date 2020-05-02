class Solution:
    # 滑动窗口 ，使用hashset
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = []
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            if s[i] in lookup:
                index = lookup.index(s[i])
                lookup.append(s[i])
                lookup = lookup[index+1:]
                cur_len = len(lookup)
            else:
                lookup.append(s[i])
                cur_len += 1
            if cur_len > max_len:max_len = cur_len
        return max_len

test_unit = Solution()
test = ['p', 'w', 'w', 'k', 'e','w']
result = test_unit.lengthOfLongestSubstring(test)
print(result)



