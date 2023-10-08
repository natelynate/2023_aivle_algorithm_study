"""
조합의 합
https://leetcode.com/problems/combination-sum/

runtime: 2632ms
memory: 16.56MB
"""
from collections import Counter

class Solution:
    """
    default solution class
    """
    def combinationSum(self, candidates:list[int], target:int) -> list[list[int]]:
        """
        method docstring
        """
        def is_distinct(newCounter:dict, prevCounters:list[dict]):
            """
            새로운 정답 후보와 임의의 이전 답안이 서로 unique한지 여부를 판정한다면
            새로운 정답 후보의 모든 elementwise frequency 중 하나라도 임의의 이전 답안의 동일한 elementwise frequency와 다르다면
            두 답은 서로 구별된다고 볼 수 있다. 
            """
            globally_distinct = 0
            for prevCounter in prevCounters: # 모든 이전 답안에 대해 비교
                locally_distinct = False
                for i in newCounter.keys():
                    if locally_distinct:
                        break
                    elif i not in prevCounter: # 이전 답안에 포함되지 않은 정수가 사용됐다면
                        locally_distinct = True
                        break
                    elif prevCounter[i] != newCounter[i]:
                        locally_distinct = True
                        break 
                if locally_distinct:
                    globally_distinct += 1
                    
            if globally_distinct == len(prevCounters):
                return True
            else:
                return False

        def dfs(combination:list) -> None:
            # if the sum of combination equals target or if the end node has been reached, exit from function
            if sum(combination) >= target:
                if sum(combination) == target and is_distinct(Counter(combination), prev_answers):
                    outputs.append(combination[:])
                    prev_answers.append(Counter(combination)) # Counter dictionary 사본을 리스트에 저장함
                return
            for integer in candidates:
                combination.append(integer)
                dfs(combination)
                combination.pop()
        outputs = []
        prev_answers = []
        
        dfs(combination=[])
        return outputs
        
if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    solution = Solution()
    print(solution.combinationSum(candidates, target))