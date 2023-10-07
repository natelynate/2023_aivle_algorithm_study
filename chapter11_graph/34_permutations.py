"""
순열
https://leetcode.com/problems/permutations/

runtime: 47ms
memory: 16.30MB

결과를 추가할 때 num_list[:]로 사본을 append해야 된다. .append(num_list)를 하게 되면 num_list의 참조가 리스트에 추가되면서
이후에 pop을 할 때처럼 값이 변경될 때 같이 바뀌어버리게 된다. copy를 하거나 deepcopy를 하는 방법도 있다. 
"""
class Solution:
    """
    Solution class
    """
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(level:int, num_list:list):
            # Exit Condition
            
            if level == len(nums): # Exit after reaching the end node
                output.append(num_list[:]) # Append a copy of num_list
                return
            
            for next_node in nums:
                if next_node not in num_list: # 미방문인 노드에 한해서 추가
                    num_list.append(next_node)
                    dfs(level+1, num_list)
                    num_list.pop()
        
        output = []
        dfs(level=0, num_list=[])
        return output
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.permute(nums=[1, 2, 3]))
    
            
            
        