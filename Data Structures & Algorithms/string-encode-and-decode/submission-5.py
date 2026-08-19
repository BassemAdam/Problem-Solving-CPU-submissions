class Solution:

    def encode(self, strs: List[str]) -> str:
     
        outStr = ""
        for s in strs:
            outStr += f"{len(s)}#{s}"
        print(outStr)
        return outStr

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        strs = []
        ptr = 0
        while ptr <= len(s):
            Len_str = ""
            while s[ptr] != "#":
                Len_str += s[ptr]
                ptr += 1

            ptr += 1
            strI = ""
            print(f"Len_str : {Len_str}")
            print(f"ptr bfr:{ptr}")
            if Len_str == "0":
                strs.append("")
            else: 
                for i in range(ptr,ptr + int(Len_str)):
                    strI +=s[i]
                    ptr = i
                print(strI)
                print(f"ptr after:{ptr}")
                ptr += 1
                strs.append(strI) 
            if ptr >= len(s):
                return strs
