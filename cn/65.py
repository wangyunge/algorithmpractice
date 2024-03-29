'''
有效数字（按顺序）可以分成以下几个部分：

    1.一个 小数 或者 整数
    2.（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：

["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：

["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = ".1"
输出：true

'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = 'None'
        s = s + '#'

        for i in range(len(s)):
            if state == 'None':
                if s[i] == '+' or s[i] == '-':
                    state = 'sign'
                    continue
                if s[i].isdigit():
                    state = 'digit_1'
                    continue
                if s[i] == '.':
                    state = 'decimal'
                    continue
                if s[i] == '#':
                    continue
            if state == 'sign':
                if s[i].isdigit():
                    state = 'digit_1'
                    continue
                if s[i] == '.':
                    state = 'decimal'
                    continue

            if state == 'digit_1':
                if s[i].isdigit():
                    state = 'digit_1'
                    continue
                if s[i] == '.':
                    state = 'decimal'
                    continue
                if s[i] == 'E' or s[i] == 'e':
                    state = 'exp'
                    continue
                if s[i] == '#':
                    continue


            if state == 'decimal':
                if s[i].isdigit():
                    state = 'decimal'
                    continue
                if s[i] == 'E' or s[i] == 'e':
                    state = 'exp'
                    continue
                if s[i] == '#':
                    continue

            if state == 'exp':
                if s[i].isdigit():
                    state = 'digit_2'
                    continue
                if s[i] == '+' or s[i] == '-':
                    state = 'exp_sign'
                    continue
            if state == 'digit_2':
                if s[i].isdigit():
                    state = 'digit_2'
                    continue
                if s[i] == '#':
                    continue

            if state == 'exp_sign':
                if s[i].isdigit():
                    state = 'digit_2'
                    continue
            return False 
        return True 




