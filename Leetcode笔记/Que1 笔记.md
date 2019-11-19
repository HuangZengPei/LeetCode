# Que1 笔记

##### 题目描述

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。 

##### 解题思路

通过**哈希**来求解，这里通过字典来模拟哈希查询的过程。  字典记录了 `num1` 和 `num2` 的值和位置，而省了再查找 `num2` 索引的步骤。

    def twoSum(self,nums,target):
        hashmap ={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None and i != j:
                return [i,j]
