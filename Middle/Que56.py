class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 合并区间
        if not intervals:return None
        intervals.sort(key = lambda x:x[0])
        merged = []
        merged.append(intervals[0])
        for j in range(1,len(intervals)):
            if intervals[j][0] <= merged[-1][1]:  #有重叠部分
                merged[-1][0] = min(intervals[j][0],merged[-1][0])
                merged[-1][1] = max(intervals[j][1],merged[-1][1])
            else:
                merged.append(intervals[j])
        return merged
