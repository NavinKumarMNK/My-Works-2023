#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int m, n;
    auto solve(vector<vector<char>>& board) -> void {       
        if (board.empty()) {return;}  
        if (board.size() == 1 && board[0].size() == 1) {return;}

        m = board.size();
        n = board[0].size();

        for (int i = 0; i < m; i += 1) {
            for (int j = 0; j < n; j += 1) {
                if (i==0 || j==0 || i==m-1 || j==n-1)
                    if (board[i][j] == 'O') {
                        dfs(board, i, j, 'O', 'T');
                    }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'T') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    auto dfs(vector<vector<char>>& board, int i, int j, char find, char replace) -> void { 
        if (i >= 0 && i < m && j < n &&  j >=0 ){
            cout << i << j;
            if (board[i][j]==find){
                cout<<i<<j;
                board[i][j] = replace;
                dfs(board, i-1, j, find, replace);
                dfs(board, i+1, j, find, replace);
                dfs(board, i, j-1, find, replace);
                dfs(board, i, j+1, find, replace);
            }
        }
    }
};
