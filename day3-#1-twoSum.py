class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # 把数据存进hashmap
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        
        # 遍历数据
        for i,num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None and i != j:
                return [i,j]