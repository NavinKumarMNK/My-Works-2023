#![allow(unused)]

use std::collections;
use std::io;
// Logest Common Substring
struct Solution;
impl Solution {
    fn longest_common_subsequence_dp(string1: &str, string2: &str) -> (String, i32) {           
        // memoization
        let mut matrix = vec![vec![0; string2.len()+1]; string1.len()+1];
        for i in 1..string1.len()+1{
            println!("i: {}", i); 
            for j in 1..string2.len()+1{
                if string1.as_bytes().get((i-1) as usize) == string2.as_bytes().get((j-1) as usize){        
                    matrix[i][j] = matrix[i-1][j-1] + 1;
                } else {
                    matrix[i][j] = std::cmp::max(matrix[i-1][j], matrix[i][j-1]);
                }
            }    
        }
        
        // prune 
        let mut sub_string = String::new();
        let mut i = string1.len();
        let mut j = string2.len();
        while i as i32 >=1 && j as i32 >=1 {
            if matrix[i][j] == matrix[i-1][j]{
                i -=1;
            } else if  matrix[i][j] == matrix[i][j-1]{
                j -=1;
            }
            else {
                sub_string.push(string1.chars().nth(i-1).unwrap());
                i -=1;
                j -=1;
            }
        }

        print!("{:?}", matrix);
        (sub_string.chars().rev().collect(), matrix[string1.len()][string2.len()])
    }

}

// Test
fn main(){
    // Test
    let mut string1 = String::new();
    let mut string2 = String::new();
    io::stdin().read_line(&mut string1);
    io::stdin().read_line(&mut string2);

    let (string, num) = Solution::longest_common_subsequence_dp(&string1.trim(), &string2.trim());
    println!("{} {}", string, num)
}

