"""
조합의 합
https://leetcode.com/problems/combination-sum/

runtime: 61ms
memory: 16.35mb
"""
class Solution:
    """
    default solution class
    """
    def combinationSum(self, candidates:list[int], target:int) -> list[list[int]]:
        def dfs(index:int, combination:list):
            # 종료조건
            if sum(combination) >= target:
                if sum(combination) == target:
                    result.append(combination[:])
                return
            
            # 자기자신부터 그 이후의 하위 원소까지 나열하여 재귀 호출
            for nxt_idx in range(index, len_candidates):
                combination.append(candidates[nxt_idx])
                dfs(nxt_idx, combination)
                combination.pop()
        

        result = [] # 합이 target인 조합
        len_candidates = len(candidates) # 사용하는 정수 개수
        dfs(0, [])
        return result