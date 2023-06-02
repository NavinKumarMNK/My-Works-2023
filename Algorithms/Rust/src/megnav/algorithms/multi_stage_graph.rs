#![allow(unused)]

use std::collections::HashMap;
use std::io;
use std::cmp::max;
use rand;

// multistage graph
struct Solution;
impl Solution {
    pub fn multistage_graph(graph: &Vec<Vec<i32>>, stage: &mut Vec<i32>) -> Vec<i32>{
        // Dynamic Programming 
        let node_count = graph.len();
        let mut matrix = vec![vec![i32::MAX; node_count] ; 2]; // cost
        
        // cumulative sum of stage
        let mut sum = 0;
        for (i, value) in stage.iter_mut().enumerate() {
            sum = sum + *value;
            *(value) = sum; 
        }
        stage.insert(0, 0);
        
        // compute distance
        matrix[0][node_count-1] = 0;
        matrix[1][node_count-1] = (node_count) as i32; 
        for i in 0..stage.len() - 2 {
            for j in stage[stage.len() - i -3] as usize..stage[stage.len()-i-2] as usize {
                for k in stage[stage.len() - i-2] as usize..stage[stage.len()-i-1] as usize {
                    if graph[j][k] == 0 {
                        continue;
                    }
                    if (graph[j][k] + matrix[0][k] < matrix[0][j]) {
                        matrix[0][j] = graph[j][k] + matrix[0][k];
                        matrix[1][j] = k as i32;
                    }
                }
            }
        } //seems like n3 but its n2 
        
        // print path
        let mut path = vec![0; stage.len()-2];
        let mut i = 0 as usize;
        let mut j = 0 as usize;
        loop {
            if matrix[0][i] == 0 {break;}
            i = matrix[1][i] as usize;
            path[j] = i as i32;
            j+=1;
            
        }

        path

    }
    
    pub fn generate_graph(stage: &Vec<i32>) -> Vec<Vec<i32>> {
        // Build Multi Stage graph [Directed Graph]
        let mut matrix  = vec![vec![0; stage.iter().sum::<i32>() as usize]; stage.iter().sum::<i32>() as usize];
        let mut count=0;
    
        for (mut i, num) in stage[0..(stage.len()-1)].iter().enumerate(){
            for j in 0..stage[i] {
                for k in 0..stage[i+1]{
                    if i == stage.len() - 2 || i == 0 {
                        matrix[count+j as usize][count+stage[i] as usize +k as usize] = (rand::random::<u16>() % 9 + 1) as i32;
                        continue;
                    }
                    let is_path = rand::random::<i32>() % 5;
                    if is_path != 0 {
                        matrix[count+j as usize][count+stage[i] as usize+k as usize] = (rand::random::<u16>() % 9 + 1) as i32;
                    } else {
                        matrix[count+j as usize][count+stage[i] as usize+k as usize] = 0;
                    }
                }
            }
            count += stage[i] as usize;
        }
        matrix
    }

}


fn main(){
    // Test
    let mut stage = vec![1, 3, 3, 1];
    //let graph = Solution::generate_graph(&stage);
    let graph = vec![vec![0,2,1,3,0,0,0,0],
    vec![0,0,0,0,2,3,0,0],
    vec![0,0,0,0,6,7,0,0],
    vec![0,0,0,0,6,8,9,0],
    vec![0,0,0,0,0,0,0,6],
    vec![0,0,0,0,0,0,0,4],
    vec![0,0,0,0,0,0,0,5],
    vec![0,0,0,0,0,0,0,0]];

    println!("{:?}", graph);

    let distance = Solution::multistage_graph(&graph, &mut stage);
    println!("{:?}", distance);


}