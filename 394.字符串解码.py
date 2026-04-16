#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = [] # 存数字
        str_stack = [] # 存字符
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif char == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat
            else:
                current_str += char
            
        return current_str
# @lc code=end

