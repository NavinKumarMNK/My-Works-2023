// Leet Code 53 - Maximum Subarray
struct Solution;


impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        
    }
}
#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    fn test_1() {
        let nums = vec![-2,1,-3,4,-1,2,1,-5,4];
        assert_eq!(Solution::max_sub_array(nums), 6);
    }
}

fn main () {}