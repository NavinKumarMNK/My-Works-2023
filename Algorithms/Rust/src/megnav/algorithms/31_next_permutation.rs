// Leet Code 31 - Next Permutation
struct Solution;

impl Solution {
    // Leet Code 31 - Next Permutation
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let m = nums.len();
        let mut pos = 0;
        for i in (1..m).rev() {
            if nums[i] > nums[i-1] {
                pos=i;
                break;
            }
        }

        if pos == 0 {
            nums.sort();
            return;
        }

        let mut smallest = nums[pos];
        let mut smallest_pos = pos;
        for i in pos..m {
            if nums[i] > nums[pos-1] && nums[i] <= smallest {
                smallest = nums[i];
                smallest_pos = i;
            }
        } 

        nums.swap(pos-1, smallest_pos);

        nums[pos..].reverse();
    }
}
#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    fn test_1() {
        let mut nums = vec![2,3,1,3,3];
        Solution::next_permutation(&mut nums);
        assert_eq!(nums, vec![2,3,3,1,3]);
    }
}

fn main () {}