#![allow(unused)]

use std::collections::HashMap;
use std::io;

fn main(){
    
    struct Solution;
    impl Solution {
        pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
            let mut map = HashMap::new();
            for (index, i) in nums.iter().enumerate() {
                let complement = target - i;
                /*if map.contains_key(&complement){
                    return vec![*map.get(&complement).unwrap(), index as i32];
                } */
                if let Some(&prev_index) = map.get(&complement) {
                    return vec![prev_index, index as i32];
                } // Speed Up

                map.insert(i, index as i32);
                
            }
            vec![]
        }        
    }

    // Test
    let mut nums = vec![3,2,4];
    let target = 6;
    let result = Solution::two_sum(nums, target);
    println!("{:?}", result);
}