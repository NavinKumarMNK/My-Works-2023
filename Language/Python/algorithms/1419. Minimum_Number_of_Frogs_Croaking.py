class Solution:
    def minNumberOfFrogs(self, string: str) -> int:
        croak_string = "croak"
        lengths = [0 for i in range(len(croak_string))]
        croak = {key: [] for key in croak_string}
        for pos, char in enumerate(string):
            croak[char].append(pos)
            lengths[croak_string.index(char)] +=1 
            # check lengths
            is_sorted = lengths == sorted(lengths, reverse=True)
            if is_sorted == False: return -1

        if len(set(lengths)) != 1:
            return -1
        
        #croak['c'], croak['k']
        i, j = 0, 0
        max_count=0
        count=0
        while i < len(croak['c']) and j < len(croak['k']):
            if croak['c'][i] < croak['k'][j]:
                count+=1
                if max_count < count:
                    max_count = count
                i+=1

            elif croak['c'][i] > croak['k'][j]:
                j+=1
                count -=1
    
        return max_count

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        use = res = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                use += 1
                res = max(use, res)
            elif ch == 'r':
                r += 1
                if r > c:
                    return -1
            elif ch == 'o':
                o += 1
                if o > r:
                    return -1
            elif ch == 'a':
                a += 1
                if a > o:
                    return -1
            elif ch == 'k':
                k += 1
                if k > a:
                    return -1
                use -= 1
        return res if c == k else -1

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counts = [0 for _ in range(5)]
        frog_count = 0
        frog_count_max = 0
        char_to_counts_idx = {
            "c": 0, "r": 1, "o": 2, "a": 3, "k": 4,}
        for char in croakOfFrogs:
            counts_idx = char_to_counts_idx[char]

            # pop previous letter
            if char != "c":
                counts[counts_idx-1] -= 1
                if counts[counts_idx-1] < 0:
                    return -1
                if char == "k":
                    frog_count -= 1
            else:
                frog_count += 1
                frog_count_max = max(
                    frog_count_max, 
                    frog_count
                )
            # push this letter
            counts[counts_idx] += 1

        for i in range(4):
            if counts[i]:
                return -1

        return frog_count_max


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        string = input()
        ob=Solution()
        print(ob.minNumberOfFrogs(string))