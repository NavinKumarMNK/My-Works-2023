struct Solution;

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut visited = vec![vec![0; grid[0].len()]; grid.len()];
        
        let mut queue: Vec<Vec<usize>> = Vec::new();
        let mut count_island = 0;
  
        let mut i = 0;
        let mut j = 0;
        while i < grid.len(){
            while j < grid[0].len(){
                
                println!("{} {}", i, j);
                if visited[i][j] != 1 && grid[i][j] == '1'{
                    // start bfs
                    queue.push(vec![i, j]);
                    while let Some(element) = queue.pop() {
                        let mut k = element[0];
                        let mut l = element[1];
                        
                        if ((k as i32 + 1) as usize) < grid[0].len()
                        && (visited[k+1][l]!=1 
                        && grid[k+1][l] == '1') {
                            queue.push(vec![k + 1, l]);
                        } 
                        
                        if k as i32 - 1 >= 0
                        && (visited[k-1][l] !=1
                        && grid[k-1][l] == '1') {
                            queue.push(vec![k-1, l]);
                        }

                        if l as i32 - 1  >= 0
                        && (visited[k][l-1] !=1 
                        && grid[k][l-1] == '1') {
                            queue.push(vec![k, l-1]);
                        } 

                        if ((l as i32 + 1) as usize) < grid.len() 
                        && (visited[k][l+1] != 1
                        && grid[k][l+1] == '1'){
                            queue.push(vec![k, l+1]);
                        }
                    
                        visited[k][l] = 1;
                    }
                    count_island += 1;
                }
                j+=1;
            }
            i+=1;
        }
        count_island
    }
}

struct solution2;



#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    pub fn works() {
        let mut graph = vec![vec!['1', '1', '1', '1', '0'],
                             vec!['1', '1', '0', '1', '0'],
                             vec!['1', '1', '0', '0', '0'],
                             vec!['0', '0', '0', '0', '0']];
        assert_eq!(Solution::num_islands(graph), 1);
    }
}

fn main() {
    println!("Hello, world!");
}