"""
전화 번호 문자 조합
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

runtime: 37ms
memory: 16.28MB
"""

class Solution:
    """
    solution class
    """   
    def letterCombinations(self, digits) -> list[str]:
        """
        """
        def dfs(graph:list[list[str]], num_string:str, node:int):
            """
            function docstring
            
            node = 다음 번호(digits의 현재 인덱스)
            num_string = 현재까지 결합한 문자조합
            """
            # 결합한 문자조합의 길이가 전화번호의 길이와 동일한 시점에서 문자조합을 출력한 후 종료
            if node == len(digits):
                answer.append(num_string)
                return
            
            # next node
            next_node = int(digits[node])

            if next_node == 0 or next_node == 1:
                dfs(graph, num_string, node+1)
            
            for next_chr in graph[next_node]:
                dfs(graph, num_string+next_chr, node+1)
            
        if not digits:
            return []
        
        graph = {0:[],
                 1:[],
                 2:['a', 'b', 'c'],
                 3:['d', 'e', 'f'],
                 4:['g', 'h', 'i'],
                 5:['j', 'k', 'l'],
                 6:['m', 'n', 'o'],
                 7:['p', 'q', 'r', 's'],
                 8:['t', 'u', 'v'],
                 9:['w', 'x', 'y', 'z']
                 }
        answer = []
        dfs(graph, '', 0)
        return answer
    
if __name__ == '__main__':
    digits_lst = ["23"]
    solution = Solution()
    for digits in digits_lst:
        print(solution.letterCombinations(digits))
    
    