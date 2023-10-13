class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        heap = []
        
        rows,cols=range(len(points)),range(len(points[0]))
        
        for i in points:
                
                dis = i[0]*i[0] + i[1]*i[1]
                
                heapq.heappush(heap,(-dis,[i[0],i[1]]))
                
                if len(heap) > k:
                    heapq.heappop(heap)
                
        print(heap)
        return [i for a,i in heap]