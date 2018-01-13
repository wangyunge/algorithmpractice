'''
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Cellphone

 Notice

Although the above answer is in lexicographical order, your answer could be in any order you want.

Have you met this question in a real interview? Yes
Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
'''
class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        self.res = []
        if not digits:
            return self.res
        index = 0
        self.digits = digits
        self.table = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
        letters = self.table[digits[index]]
        for thisLetter in letters:
            self.DFS(thisLetter,index+1)
        return self.res
    def DFS(self,parent,index):
        if index == len(self.digits):
            self.res.append(parent)
        else:
            letters = self.table[self.digits[index]]
            for thisLetter in letters:
                self.DFS(parent + thisLetter,index + 1)