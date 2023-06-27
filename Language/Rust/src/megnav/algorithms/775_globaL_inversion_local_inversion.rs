// LeetCode 775 - Global and Local Inversions
struct Solution;
impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        let n = nums.len();
        // Global Inversion - Merge Sort
        let mut count_gi: i32 = 0;
        Solution::merge_sort(&mut nums.clone(), 0, n-1, &mut count_gi);

        // Local Inversion - O(n)
        let mut count_li = 0;
        for i in 0..n-1 {
            if nums[i] > nums[i+1] {count_li +=1;}
        }
        println!("count_gi: {}, count_li: {}", count_gi, count_li);
        count_gi == count_li 
    }

    pub fn merge_sort(nums: &mut Vec<i32>, low:usize, high:usize, count: &mut i32) {
        if high <= low {return;}
        let mid = (high + low) / 2;
        Solution::merge_sort(nums, low, mid, count);
        Solution::merge_sort(nums, mid+1, high, count);
        Solution::merge(nums, low, mid, high, count);
    }

    pub fn merge(nums: &mut Vec<i32>, low:usize, mid:usize, high:usize, count: &mut i32) {
        let mut i = low;
        let mut j = mid+1;
        let mut temp: Vec<i32> = Vec::with_capacity(high -low + 1);
        while i != mid+1 && j != high+1 {
            if nums[i] > nums[j] {
                temp.push(nums[j]);
                j+=1;
                *count += (mid-i+1) as i32;
            } else {
                temp.push(nums[i]);
                i+=1;
            }
        }
        
        if i == mid+1 {
            for k in j..high+1 {
                temp.push(nums[k]);
            }
        } else {
            for k in i..mid+1 {
                temp.push(nums[k]);
            }
        }


        for i in 0..temp.len() {
            nums[low+i] = temp[i];
        }
    }

    
}

impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        
        for i in 0..nums.len() {
            if (nums[i] - i as i32).abs() > 1 {
                return false;
            }
        }
        true
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_1() {
        let nums = vec![5, 3, 2, 4, 1];
        assert_eq!(Solution::is_ideal_permutation(nums), false);
    }
    
}

fn main() {}
