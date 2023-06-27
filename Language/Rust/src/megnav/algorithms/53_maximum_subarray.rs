// Leet Code 53 - Maximum Subarray
struct Solution;


use std::cmp::max;
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        return *Solution::slc(&nums[..])
            .iter()
            .max()
            .unwrap();
    }

    // summing via logical continuty 
    pub fn slc(nums: &[i32]) -> [i32; 4] {
        // bc, lc, rc, nc 
        if nums.len() == 1 {
            return [nums[0]; 4]
        }

        let (left_sums, right_sums) = nums.split_at(nums.len()/2);
        let [l_bc, l_lc, l_rc, l_nc] = Solution::slc(left_sums);
        let [r_bc, r_lc, r_rc, r_nc] = Solution::slc(right_sums);
        
        let bc = r_bc + l_bc;
        let lc = max(l_lc, l_bc + r_lc);
        let rc = max(r_rc, r_bc + l_rc);
        let nc = max( max(l_nc, r_nc), l_rc + r_lc);
        return [bc, lc, rc, nc];
    } 
}

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        nums.iter()
            .fold((0, nums[0]), |(cur, ans), i| {
                (0.max(cur + i), ans.max(cur + i))
            })
            .1
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