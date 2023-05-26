impl Solution{
    fn dfs(i: i32, j: i32, grid: &mut Vec<Vec<i32>>, count: &mut i32) {
        if i < 0 || j < 0 || i >= grid.len() as i32  || j >= grid[0].len() as   i32 || grid[i as usize][j as usize] == 0  {
            
            *count += 1;
            return; 
        }
        if grid[i as usize][j as usize] == -1 {
            return;
        }
        grid[i as usize][j as usize] = -1;
        Solution::dfs(i + 1, j, grid, count);
        Solution::dfs(i - 1, j, grid, count);
        Solution::dfs(i, j + 1, grid, count);
        Solution::dfs(i, j - 1, grid, count);
    }
    fn island_perimeter(grd: Vec<Vec<i32>>) -> i32 {
        let mut grid = grd.clone();
        let mut count = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    Solution::dfs(i as i32, j as i32, &mut grid, &mut count);
                    break;
                }
            }
        }
        count
    }
}