// LeetCode 229 - Majority Element II
struct Solution;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        // atmost two elemnt will be dominating n/3 occurences
        let n = nums.len();
        let mut element1 = -1;
        let mut count1: i32 = 0;
        let mut element2 = -1;
        let mut count2: i32 = 0;
        for i in 0..n {
            if count1 == 0 && nums[i] != element2 {
                element1 = nums[i];
            } else if count2 == 0 && nums[i] != element1 {
                element2 = nums[i];
            } 
            if nums[i] == element1 {
                count1+=1;
            } else if nums[i] == element2 {
                count2+=1;
            } else {
                count1-=1;
                count2-=1;
            }
        }
        count1 = 0;
        count2 = 0;
        for i in 0..n {
            if nums[i] == element1{
                count1 +=1;
            } else if nums[i] == element2 {
                count2 +=1;
            } 
        }
        println!("{} {}", count1, count2);
        println!("{} {}", element1, element2);
        let  mut ret_vec: Vec<i32> = Vec::with_capacity(2);
        if count1 > n as i32/3  {
            ret_vec.push(element1);
        } if count2 > n as i32/3 {
            ret_vec.push(element2);
        }
        ret_vec
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_229() {
        let nums = vec![1, 1, 1, 3, 3, 2, 2, 2];
        let res = Solution::majority_element(nums);
        assert_eq!(res, vec![1, 2]);
    }
}

fn main() {}
