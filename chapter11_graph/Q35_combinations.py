"""
조합
https://leetcode.com/problems/combinations/

runtime: 925ms
memory: 64.67MB

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]
all integers are unique because they are generated from a range function

dfs를 매번 반복할 때 1,N에서 매번 integer를 고르는 것이 아니라 범위 시작점인 start:int를 승계해서 이전 인덱스의 숫자들을 다음 branch때 사용하지
못하도록 막으면 (1,2)와(2,1)을 구분할 필요가 없어짐 (새로운 integer가 무조건 상향순으로 추가되기 때문)
"""

class Solution:
    """
    default solution class
    """
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        method docstring
        """
        def dfs(start: int, level: int, combination: list) -> None:
            # 종료조건
            if level == k:
                outputs.append(combination[:])  # Append a copy of the combination
                return

            for integer in range(start, n+1):
                combination.append(integer)
                dfs(start=integer+1, level=level+1, combination=combination) 
                combination.pop()

        outputs = []
        dfs(1, 0, [])
        return outputs
    
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n=4, k=2))