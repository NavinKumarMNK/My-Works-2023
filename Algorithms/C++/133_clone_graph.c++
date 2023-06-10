// Definition for a Node.
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


class Solution {
public:
    unordered_map<Node*, Node*> map;

    auto dfs(Node *node) -> Node* {
        vector<Node*> neighbor;
        if (map.find(node)!=map.end()){
            return map[node];
        }
        Node* clone = new Node(node->val);
        map[node]=clone;
        for (auto it:node->neighbors){
            clone->neighbors.push_back(dfs(it));
        }
        return clone;
    }

    auto cloneGraph(Node* node) -> Node* {
        if (node==NULL) {return NULL;}
        return dfs(node);
    }    
};