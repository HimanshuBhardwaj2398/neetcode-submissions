class Solution:
    
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0: 
            return "€"
        encoded_str="€".join(str for str in strs)
        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        if s == "": 
            return [""]
        elif s is "€": 
            return []
        decoded_strs=s.split("€")
        return decoded_strs
