"""
전화 번호 문자 조합
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

runtime:
memory:
"""

class Solution:
    def dfs_iterative(graph, node):
        """
        node = phone number
        adj_node = alphabets associated with a number
        """
        
        
    def letterCombinations(self, digits: str) -> list[str]:
        # 인덱싱 편의성을 위해 리스트의 index=2 ~ 9까지 알파벳들을 저장함
        phone_alphabets = [[], 
                           [], 
                           ['a', 'b', 'c'],
                           ['d', 'e', 'f'],
                           ['g', 'h', 'i'],
                           ['j', 'k', 'l'],
                           ['m', 'n', 'o'],
                           ['p', 'q', 'r', 's'],
                           ['s', 't', 'v'],
                           ['w', 'x', 'y', 'z'] 
                           ]
        
        self.dfs_iterative(phone_alphabets, '')

if __name__ == '__main__':
    phone_number = "23"