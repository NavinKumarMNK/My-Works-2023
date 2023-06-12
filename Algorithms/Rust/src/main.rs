struct Solution;
impl Solution {
    /*
    Time Complexity : O(V+2E) // dfs 
    Space Complexity : O(V+2E) + O(2N) // graph + (low_tin + tin + visited)
    */
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n as usize];
        let mut low_tin = vec![0; n as usize];
        let mut tin = vec![0; n as usize];
        let mut visited = vec![0; n as usize];
        let mut bridges =  Vec::with_capacity(n as usize);

        for i in connections.iter() {
            adj[i[0] as usize].push(i[1] as usize);
            adj[i[1] as usize].push(i[0] as usize);
        }
        
        Solution::dfs(
            0,
            -1,
            &adj,
            &mut visited,
            &mut tin,
            &mut low_tin,
            &mut bridges,
            0,
        );
        bridges
    }

    pub fn dfs(node:usize, parent:i32, adj: &Vec<Vec<usize>>,
             visited: &mut Vec<i32>, tin: &mut Vec<i32>, low_tin: &mut Vec<i32>,
             bridges: &mut Vec<Vec<i32>>, timer:i32) {
        
        visited[node] = 1;
        low_tin[node] = timer;
        tin[node] = timer;

        for i in adj[node].iter() {
            if *i as i32 == parent {continue;}
            else if visited[*i] == 0 {
                Solution::dfs(
                    *i,
                    node as i32,
                    adj,
                    visited,
                    tin,
                    low_tin,
                    bridges,
                    timer+1
                );
                low_tin[node] = std::cmp::min(low_tin[node], low_tin[*i]);
                if low_tin[*i] > tin[node]{
                    bridges.push(vec![node as i32, *i as i32]);
                } 

            } else {
                low_tin[node] = std::cmp::min(low_tin[node], low_tin[*i]);
            }
        }


    }
}
#[cfg(test)]
pub mod tests{
    use super::*;
    #[test]
    pub fn test_graph(){
        let n = 4;
        let connections = vec![vec![0,1],vec![1,2],vec![2,0],vec![1,3]];
        let result = Solution::critical_connections(n, connections);
        assert_eq!(result, vec![vec![1,3]]);
    }

}

fn main() {}
