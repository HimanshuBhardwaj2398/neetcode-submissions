class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CounterS,CounterT={},{}

        for k1 in s: 
            CounterS[k1]=CounterS.get(k1,0)+1
        
        for k2 in t: 
            CounterT[k2]=CounterT.get(k2,0)+1


        return CounterS==CounterT

