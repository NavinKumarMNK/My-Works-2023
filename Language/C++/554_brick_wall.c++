#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    auto leastBricks(vector<vector<int>> &wall) -> int
    {
        unordered_map<int, int> map;
        int temp;

        for (int i = 0; i < wall.size(); i++)
        {
            temp = 0;
            for (int j = 0; j < wall[i].size() - 1; j++)
            {
                temp += wall[i][j];
                map[temp]++;
            }
        }

        int max_val = 0;
        for (const auto &iter : map)
        {
            max_val = max(iter.second, max_val);
        }

        return wall.size() - max_val;
    }
};