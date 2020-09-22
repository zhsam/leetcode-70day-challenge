class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 变为实际数字
        num = 0
        for i in range(len(digits)):
            num += (10**i) * digits[len(digits)-1-i]
        # 数字加一
        result_num = num + 1
        result_list = []
        # 转变为list
        for i in range(len(str(result_num))):
            result_list.append(int(str(result_num)[i]))
        return result_list