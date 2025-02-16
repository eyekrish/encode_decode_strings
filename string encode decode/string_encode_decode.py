def encode(self, strs: list[str]) -> str:
        ls=""
        for s in strs:
            ls+=str(str(len(s))+"#"+s)
        return ls
        
def decode(self, s: str) -> list[str]:
        res,i=[],0
        while i<len(s):
            j=i
            while s[j] != "#":
                    j+=1
            length_str=int(s[i:j])
            word=s[j+1:j+length_str+1]
            res.append(word)
            i=j+length_str+1
        return res

encode_strings=encode(self=any,strs=["applele","banana","orange","pineapple"])
decode_strings=decode(self=any,s=encode_strings)
print("strings after encoding : ",encode_strings)
print("Decoded strings : ",decode_strings)

