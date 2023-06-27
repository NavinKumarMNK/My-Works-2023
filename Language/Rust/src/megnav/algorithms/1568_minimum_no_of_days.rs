
struct Solution;
impl Solution {
    pub fn min_days(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut point: Vec<usize> = Vec::with_capacity(2);
        let (m, n) = (grid.len(), grid[0].len()); 
        let mut no_of_island = 0;
        let mut art = false;
        
        let mut timer = 0;
                    
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    println!("{} {}", i, j);
                    no_of_island += 1;
                    let mut low_tin = vec![vec![0; n]; m];
                    let mut tin = vec![vec![0; n]; m];
                    timer = 0;
                    Solution::dfs(
                        -1, -1,  &mut grid, i, j, &mut low_tin, &mut tin, &mut art,
                        &mut timer 
                    ); 
                }
            }
        }
        if no_of_island == 0 {return 0;}
        if no_of_island > 1 {return 0;}
        if timer == 1 {return 1;}
        if art {return 1;}
        return 2;
    }

    pub fn dfs(parentx:i32, parenty:i32, grid: &mut Vec<Vec<i32>>, i:usize, j:usize, 
    low_tin: &mut Vec<Vec<i32>>, tin: &mut Vec<Vec<i32>>, art: &mut bool, timer:&mut i32 ){
        
        grid[i][j] = -1;
        tin[i][j] = *timer;
        low_tin[i][j] = *timer;
        let mut rootcall = 0;
        *timer = *timer+1;

        let dirs: [[i32; 2]; 4] = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for it in dirs {
            let newx = i as i32+it[0];
            let newy = j as i32+it[1];
            if parentx == newx && parenty == newy {continue;}
            if newx >= 0 &&  newy >= 0 && newx < grid.len() as i32 && newy < grid[0].len() as i32 {
                if grid[newx as usize][newy  as usize] == 1{
                    Solution::dfs(
                        i as i32, j as i32, grid, newx as usize, newy as usize, low_tin, tin, art, timer
                    );   
                    low_tin[i][j] = std::cmp::min(low_tin[i][j], low_tin[newx as usize][newy as usize]);
                    if tin[i][j] <= low_tin[newx as usize][newy as usize] && parentx != -1 && parenty != -1 {
                        *art = true;
                    }
                    rootcall += 1;
                
                } else if grid[newx as usize][newy as usize] == -1 {
                    low_tin[i][j] = std::cmp::min(low_tin[i][j], tin[newx as usize][newy as usize]); 
                }
            } else {continue;}        
        }
        if parentx == -1 && parenty == -1  && rootcall > 1 {
            *art = true;
        }       

    }
}
#[cfg(test)]
pub mod tests{
    use super::*;
    #[test]
    pub fn works() {
        // [[0,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]]
        let mut graph = vec![vec![0,1,0,1,1],vec![1,1,1,1,1],vec![1,1,1,1,1],vec![1,1,1,1,0]];
        assert_eq!(Solution::min_days(graph), 1);
    }

}

fn main() {}
