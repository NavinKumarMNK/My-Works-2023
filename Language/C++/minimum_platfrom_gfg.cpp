//{ Driver Code Starts
// Program to find minimum number of platforms
// required on a railway station
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    auto findPlatform(int arr[], int dep[], int n) -> int
    {
        int max_val = 0;

        sort(arr, arr + n);
        sort(dep, dep + n);

        for (int i = 0, j = 0; i < n and j < n;)
        {
            if (arr[i] <= dep[j])
            {
                i++;
            }
            else
            {
                j++;
            }

            max_val = max(max_val, i - j);
        }

        return max_val;
    }
};

//{ Driver Code Starts.
// Driver code
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        int dep[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        for (int j = 0; j < n; j++)
        {
            cin >> dep[j];
        }
        Solution ob;
        cout << ob.findPlatform(arr, dep, n) << endl;
    }
    return 0;
}
// } Driver Code Ends