#include<bits/stdc++.h>
using namespace std;

//Kosaraju's Solution
class Solution {  
public:
    void dfs(vector<vector<char>> *graph, int v, bool visited[], stack<int> &st) {
        visited[v] = true;
        for (int i=0; i<graph->at(v).size(); i++) {
            if (!visited[graph->at(v).at(i)]) {
                dfs(graph, graph->at(v).at(i), visited, st);
            }
        }
        st.push(v);
    }

    void dfs(vector<vector<char>> *graph, int v, bool visited[], vector<vector<char>> *scc) {
        visited[v] = true;
        scc->push_back(graph->at(v));
        for (int i=0; i<graph->at(v).size(); i++) {
            if (!visited[graph->at(v).at(i)]) {
                dfs(graph, graph->at(v).at(i), visited, scc);
            }
        }
    }

    vector<string> maxNumOfSubstrings(string s) {
        // graph
        vector<vector<char>> *graph = new vector<vector<char>>[26];
        int loc[26][2];
        for (int i=0; i<26; i++) {
            loc[i][0] = -1;
            loc[i][1] = -1;
        }

        for (int i=0; i<s.length(); i++) {
            int index = s[i] - 'a';
            if(loc[index][0] == -1){
                loc[index][0] = i;
                loc[index][1] = i;
            } else {
                loc[index][1] = i;
            }
        }

        set<char> charSet(s.begin(), s.end());

        for (auto it=charSet.begin(); it!=charSet.end(); it++) {
            int index = *it - 'a';
            vector<char> temp;
            for (int i=loc[index][0]; i <= loc[index][1]; i++) {
                temp.push_back(s[i]);
            }
            graph->push_back(temp);
        }

        // reverse the graph and find the SCC 
        vector<vector<char>> *rgraph = new vector<vector<char>>[26];
        for (int i=0; i< graph->size(); i++) {
            for (int j=0; j<graph[i].size(); j++) {
                rgraph[j].push_back(graph[i][j]);
            }
        }        

        // find the SCC
        vector<vector<char>> scc = new vector<vector<char>>[26];
        bool visited[26];
        for (int i=0; i<26; i++) {
            visited[i] = false;
        }

        stack<int> st;
        for (int i=0; i<26; i++) {
            if (!visited[i]) {
                dfs(graph, i, visited, st);
            }
        }

        for (int i=0; i<26; i++) {
            visited[i] = false;
        }

        while (!st.empty()) {
            int v = st.top();
            st.pop();
            if (!visited[v]) {
                dfs(rgraph, v, visited, scc);
            }
        }

        // find the max length of the SCC
        int maxLen = 0;
        for (int i=0; i<26; i++) {
            if (scc[i].size() > maxLen) {
                maxLen = scc[i].size();
            }
        }

        cout << scc << endl;

        // find the max length of the SCC
        #include<bits/stdc++.h>
using namespace std;

//Kosaraju's Solution
class Solution {  
public:
    void dfs(vector<vector<char>> *graph, int v, bool visited[], stack<int> &st) {
        visited[v] = true;
        for (int i=0; i<graph->at(v).size(); i++) {
            if (!visited[graph->at(v).at(i)]) {
                dfs(graph, graph->at(v).at(i), visited, st);
            }
        }
        st.push(v);
    }

    void dfs(vector<vector<char>> *graph, int v, bool visited[], vector<vector<char>> *scc) {
        visited[v] = true;
        scc->push_back(graph->at(v));
        for (int i=0; i<graph->at(v).size(); i++) {
            if (!visited[graph->at(v).at(i)]) {
                dfs(graph, graph->at(v).at(i), visited, scc);
            }
        }
    }

    vector<string> maxNumOfSubstrings(string s) {
        // graph
        vector<vector<char>> *graph = new vector<vector<char>>[26];
        int loc[26][2];
        for (int i=0; i<26; i++) {
            loc[i][0] = -1;
            loc[i][1] = -1;
        }

        for (int i=0; i<s.length(); i++) {
            int index = s[i] - 'a';
            if(loc[index][0] == -1){
                loc[index][0] = i;
                loc[index][1] = i;
            } else {
                loc[index][1] = i;
            }
        }

        set<char> charSet(s.begin(), s.end());

        for (auto it=charSet.begin(); it!=charSet.end(); it++) {
            int index = *it - 'a';
            vector<char> temp;
            for (int i=loc[index][0]; i <= loc[index][1]; i++) {
                temp.push_back(s[i]);
            }
            graph->push_back(temp);
        }

        // reverse the graph and find the SCC 
        vector<vector<char>> *rgraph = new vector<vector<char>>[26];
        for (int i=0; i< graph->size(); i++) {
            for (int j=0; j<graph[i].size(); j++) {
                rgraph[j].push_back(graph[i][j]);
            }
        }        

        // find the SCC
        vector<vector<char>> scc[26];
        bool visited[26];
        for (int i=0; i<26; i++) {
            visited[i] = false;
        }

        stack<int> st;
        for (int i=0; i<26; i++) {
            if (!visited[i]) {
                dfs(graph, i, visited, st);
            }
        }

        for (int i=0; i<26; i++) {
            visited[i] = false;
        }

        while (!st.empty()) {
            int v = st.top();
            st.pop();
            if (!visited[v]) {
                dfs(rgraph, v, visited, scc);
            }
        }

        // find the max length of the SCC
        int maxLen = 0;
        for (int i=0; i<26; i++) {
            if (scc[i].size() > maxLen) {
                maxLen = scc[i].size();
            }
        }

        cout << scc << endl;

        // find the max length of the SCC
        vector<string> result;
        for (int i=0; i<26; i++) {
            if (scc[i].size() == maxLen) {
                string temp(scc[i].begin(), scc[i].end());
                result.push_back(temp);
            }
        }
        return result;

    }
};

int main() {
    string s = "abab";
    Solution obj;
    vector<string> result = obj.maxNumOfSubstrings(s);
    for (int i=0; i<result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
}
        return result;

    }
};

int main() {
    string s = "abab";
    Solution obj;
    vector<string> result = obj.maxNumOfSubstrings(s);
    for (int i=0; i<result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
}