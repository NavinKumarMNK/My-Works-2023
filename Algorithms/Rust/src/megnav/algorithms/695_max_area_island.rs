
use std::collections::VecDeque;
impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut max_area = 0;
        let (m, n) = (grid.len(), grid[0].len());
        let mut deque =  VecDeque::with_capacity(
                                grid[0].len()*grid.len());
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    deque.clear();
                    deque.push_back(vec![i, j]);
                    let mut count = 0;
                    while let Some(e) = deque.pop_back() {
                        if grid[e[0]][e[1]] == 0 {
                            continue;
                        }
                        count+=1;
                        
                        println!("{} {} {}", e[0], e[1], count);
                        if e[0] as i32 -1 >= 0 && grid[e[0]-1][e[1]] == 1 {
                            deque.push_back(vec![e[0]-1, e[1]]);
                        }
                        if e[0] + 1 < grid.len() && grid[e[0]+1][e[1]] == 1 {
                            deque.push_back(vec![e[0]+1, e[1]]);
                        }
                        if e[1] as i32 - 1  >= 0 && grid[e[0]][e[1]-1] == 1 {
                            deque.push_back(vec![e[0], e[1]-1]);
                        }
                        if e[1] + 1 < grid[0].len() && grid[e[0]][e[1]+1] == 1 {
                            deque.push_back(vec![e[0], e[1]+1]);
                        }
                        grid[e[0]][e[1]] = 0;
                    }
                    println!("{}", count);
                    //if count > max_area {max_area = count;}
                    max_area = max_area.max(count)
                }
            }
        }
        max_area
    }
}