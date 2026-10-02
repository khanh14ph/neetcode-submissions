import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map=dict()
        for i in range(n):
            adj_map[i]=[]
        for i in edges:
            adj_map[i[0]].append(i[1])
            adj_map[i[1]].append(i[0])
        visited=set()
        count=0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                
                queue=collections.deque()
                queue.append(i)
                while queue:
                    cur=queue.popleft()
                    for neighbor in adj_map[cur]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                count+=1
        return count