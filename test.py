#User function Template for python3
from typing import List
class Solution:
    def playOfGlasses(self, c1:int, w1:int, c2:int, w2:int, c3:int, w3:int) -> List[int] :
        # code here
        for _ in range(10^4):
            poured_to_b = min(w1,c2-w2)
            w1 -= poured_to_b
            w2 += poured_to_b
            
            poured_to_c = min(w2,c3-w3)
            w2 -= poured_to_c
            w3 += poured_to_c
            
            poured_to_a = min(w3,c1-w1)
            w3 -= poured_to_a
            w1 += poured_to_a
        
        final_list=[w1,w2,w3]
        return final_list

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    
    c1, w1, c2, w2, c3, w3 = map(int,input().split())
    obj = Solution()
    res = obj.playOfGlasses(c1, w1, c2, w2, c3, w3)
    print(" ".join(map(str,res)))
# } Driver Code Ends