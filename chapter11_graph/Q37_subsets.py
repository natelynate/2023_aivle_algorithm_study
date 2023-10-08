"""
부분 집합
https://leetcode.com/problems/subsets/

runtime: 37ms
memory: 16.33MB
"""
class Solution:
    def subsets(self, nums:list[int]) -> list[list[int]]:        
        def dfs(idx:int, combination:list, length:int):
            if length == subset_size:
                answer.append(combination[:])
                return
            for new_idx in range(idx+1, len(nums)):
                combination.append(nums[new_idx])
                dfs(new_idx, combination, length+1)
                combination.pop()
                
        answer = [[]] # 공집합은 답안에 미리 포함하고 있음
        for subset_size in range(1, len(nums)+1): # 1~len(nums)+1 크기의 subset을 구하는 dfs를 반복해서 실행시켜준다
            dfs(idx=-1, combination=[], length=0)
        return answer
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets(nums=[1, 2, 3]))
            
        