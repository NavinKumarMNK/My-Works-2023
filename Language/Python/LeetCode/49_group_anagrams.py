class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for n in strs:
            x, y = 0, 1
            key = tuple((x := x + (ord(a)), y := y * (ord(a))) for a in n)
            if key == (): key = (0, 0)
            else : key = key[-1]
            if key not in dct:
                dct[key] = [n]
            else:
                dct[key].append(n)
        
        print(dct)
        return  list(dct.values())
