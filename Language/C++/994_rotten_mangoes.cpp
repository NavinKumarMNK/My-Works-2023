#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    
    auto orangesRotting(vector<vector<int>>& grid) -> int {
        if (grid.empty()) {return 0;}
        int m = grid.size();
        int n = grid[0].size();
        int depth = 0;
        int countfo = 0;
        queue<pair<int, int>> q;

        for(int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                    grid[i][j]=0;
                }  else if (grid[i][j] == 1) {
                    countfo+=1;
                }
            }
        }

        if (countfo == 0){
            return 0;
        }

        vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()){
            int size = q.size();
            while (size--){
                auto [x, y] = q.front();
                q.pop();
                for (auto [dx, dy] : dirs) {
                    int i = x+dx;
                    int j = y+dy;
                    if (i>=0 && i < m && j < n && j >=0 && grid[i][j]==1) {
                        grid[i][j] = 0;
                        countfo--;
                        q.push({i, j});
                        
                    }
                }
            }
            depth++;
        }
        if (countfo != 0) {
            return -1;
        }
        return depth-1;
    }

};