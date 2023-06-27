// LeetCode 169 - Majority Element
struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut element = -1;
        let mut count:i32 = 0;
        for i in 0..n {
            if count == 0 {
                element = nums[i];
            }
            if nums[i] == element {
                count+=1;
            } else {
                count-=1;
            }
        }
        return element;
    } 
    
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_169() {
        let nums = vec![2, 2, 1, 1, 1, 2, 2];
        let res = Solution::majority_element(nums);
        assert_eq!(res, 2);
    }
}

fn main() {}
