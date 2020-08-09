"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for idx in range(len(nums)):
            search = _next_idx(idx)
            while search != idx :
                if nums[search] > nums[idx]:
                    res.append(nums[search])
                    break
            res.append(-1)
        return res 

        def _next_idx(cur):
            if cur + 1 < len(nums):
                return cur+1 
            else:
                return len(nums) - cur -1

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        


@annotate("string->string")
class Udf(object):
    def __init__(self):
        self.name_id_mapping= {}

    def load_resource(self, model_name):
        records = get_cache_file(model_name)
        for line in records:
            line = line.split(',')
            feature_name = line[0].strip()
            feature_id = line[1].strip()
            self.name_id_mapping[feature_name] =  feature_id

    def evaluate(self, kv_string):
        if kv_string is None or len(kv_string) == 0:
            return
        if not self.name_id_mapping:
            self.load_resource("dip_appkey_tag_file")
        feature_list = kv_string.strip().split(',')
        res_list = []
        for kvp in feature_list:
            kv_tuple = kvp.split('_')
            value = kvp.split(':')[-1]
            if len(kv_tuple) != 2:
                continue
            suffix, _ = kv_tuple
            if suffix in self.name_id_mapping:
                feature_id = self.name_id_mapping[suffix]
            
            res_list.append(feature_id + '_' + value)

        return ','.join(res_list)

