# Python学习记录

###列表的使用
####切片
一个切片操作要提供三个参数 [start_index:  stop_index:  step]，start_index是切片的起始位置，stop_index是切片的结束位置（不包括），step可以不提供，默认值是1，步长值不能为0，不然会报错ValueError。

当step 是正数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从左向右截取，start_index和stop_index不论是正数还是负数索引还是混用都可以，但是要保证list[stop_index]元素的【逻辑】位置必须在list[start_index]元素的【逻辑】位置右边，否则取不出元素。
当 step 是负数时，以list[start_index]元素位置开始， step做为步长到list[stop_index]元素位置（不包括）为止，从右向左截取

##### 逆序一个字符串
Que12
`list = list[::-1]`
字符串的重复多次
`str = str * times`
