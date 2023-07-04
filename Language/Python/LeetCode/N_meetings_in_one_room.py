class Solution:
    def maximumMeetings(self,n,start,end):
        # n -> number of meeetings in start , end
        meetings = []
        for i in range(n):
            meetings.append([i ,start[i], end[i]])
        meetings.sort(key=lambda x: x[2])
        curr_time = 0
        count = 0
        for i in range(n):
            if curr_time < meetings[i][1]:
                curr_time = meetings[i][2]
                count+=1 
        return count 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))