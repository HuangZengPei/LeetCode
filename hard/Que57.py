class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:return [newInterval]
        merged = []
        mark = 0

        # 第一步，将新区间正确插入
        for i in range(len(intervals)):
            if i == len(intervals)-1:   # 判断插入前面还是后面
                if intervals[i][0] < newInterval[0]:
                    intervals.insert(i+1,newInterval)
                    mark = i
                else:
                    intervals.insert(i,newInterval)
                    mark = i
                break
            if newInterval[0] < intervals[i][0]:  # 插入当前前面一个
                intervals.insert(i,newInterval)
                mark = i
                break
            elif intervals[i][0] <= newInterval[0] <= intervals[i+1][0]:   # 插在当前后面,mark指向i
                intervals.insert(i+1,newInterval)
                mark = i
                break
            else:
                merged.append(intervals[i])
                mark = i
        if not merged:
            merged.append(intervals[0])

        for j in range(mark,len(intervals)):
            if intervals[j][0] <= merged[-1][1]:  #有重叠部分
                merged[-1][0] = min(intervals[j][0],merged[-1][0])
                merged[-1][1] = max(intervals[j][1],merged[-1][1])
            else:
                merged.append(intervals[j])
        return merged


test = Solution()
list = [[0,5],[9,12]]

newList = [7,16]
result = test.insert(list,newList)
print(result)
