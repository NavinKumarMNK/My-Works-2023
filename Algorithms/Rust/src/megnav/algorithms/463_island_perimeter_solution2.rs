use std::collections;
struct Solution;
impl Solution {
        // Island Permister
        pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
            let mut start : Vec<usize> = Vec::new();
            let mut flag: bool = false;
            for i in 0..grid.len(){
                for j in 0..grid[i].len(){
                    if (grid[i][j] == 1){
                        start = vec![i,j];
                        flag = true;
                        break;
                    }
                }
                if flag {break;}
            }

            // dfs & perimeter
            let mut perimeter: i32 = 0;
            let mut visited: collections::VecDeque<Vec<usize>> = collections::VecDeque::new();
            let mut stack: collections::VecDeque<Vec<usize>> = collections::VecDeque::new();
            stack.push_back(start.clone());
            visited.push_back(start);
            while let Some(i) = stack.pop_back(){
                let sur_lnd = Solution::sur_land(&grid, &i);
                for j in sur_lnd{
                    if j.0 == 1 {
                        if !visited.contains(&j.1) {
                            stack.push_back(j.1.clone());
                            visited.push_back(j.1);
                        }
                    }
                    else if j.0 == 0 {
                        perimeter += 1;
                    }
                }
            } 


            return perimeter;
        }

        pub fn sur_land(grid: &Vec<Vec<i32>>, pos: &Vec<usize>) -> Vec<(i32, Vec<usize>)> {
            let mut lr: (i32, Vec<usize>) = (0, vec![0,0]);
            let mut ll: (i32, Vec<usize>) = (0, vec![0,0]);
            let mut ld: (i32, Vec<usize>) = (0, vec![0,0]);
            let mut lu: (i32, Vec<usize>) = (0, vec![0,0]);            
            println!("pos: {:?} ", &pos);

            if pos[0] as i32 - 1 >= 0 {
                lu = Solution::look_up(&grid, &pos);
            }
            if pos[0]  as i32 + 1 < grid.len() as i32 {
                ld = Solution::look_down(&grid, &pos);
            }
            if pos[1]  as i32 - 1 >= 0 {
                ll = Solution::look_left(&grid, &pos);
            }
            if pos[1]  as i32 + 1 < grid[0].len() as i32{
                lr = Solution::look_right(&grid, &pos);
            }
                
            let mut sur_lnd: Vec<(i32, Vec<usize>)> = Vec::new();
            sur_lnd.push(lr);
            sur_lnd.push(ll);
            sur_lnd.push(ld);
            sur_lnd.push(lu);
            return sur_lnd;
        }
        
        pub fn look_right(grid: &Vec<Vec<i32>>, pos:&Vec<usize>) -> (i32, Vec<usize>) {
            return (grid[pos[0]][pos[1]+1], vec![pos[0], pos[1]+1]);       
        }
        pub fn look_down(grid: &Vec<Vec<i32>>, pos:&Vec<usize>) -> (i32, Vec<usize>) {
            return (grid[pos[0]+1][pos[1]] , vec![pos[0]+1, pos[1]]);       
        }
        pub fn look_up(grid: &Vec<Vec<i32>>, pos:&Vec<usize>) -> (i32, Vec<usize>) {
                return (grid[pos[0]-1][pos[1]], vec![pos[0]-1, pos[1]]);       
        }
        pub fn look_left(grid: &Vec<Vec<i32>>, pos:&Vec<usize>) -> (i32, Vec<usize>) {
            return (grid[pos[0]][pos[1]-1], vec![pos[0], pos[1]-1]);           
        }
    }