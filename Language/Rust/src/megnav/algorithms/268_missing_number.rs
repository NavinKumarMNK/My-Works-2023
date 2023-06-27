impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut sum = 0;
        for i in 0..n {
            sum += nums[i];
        }

        let total = n * (n+1) / 2;
        return total as i32 - sum;

    }
}