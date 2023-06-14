// LeetCode 493. Reverse Pairs
struct Solution;
impl Solution {
    pub fn reverse_pairs(mut nums: Vec<i32>) -> i32 {
        let mut count=0;
        let m = nums.len();
        Solution::merge_sort(
            &mut nums.iter().map(|&x| x as i64).collect(),
            0,
            (m-1) as i64,
            &mut count
        );
        count as i32
    }

    pub fn merge_sort(nums:&mut Vec<i64>, low:i64, high:i64, count: &mut i64){
        if low >= high {return ;}
        let mid = (low+high) / 2;
        Solution::merge_sort(nums, low, mid, count);
        Solution::merge_sort(nums, mid+1, high, count);
        Solution::merge(nums, low, mid, high, count);
    }

    pub fn merge(nums:&mut Vec<i64>, low:i64, mid:i64, high:i64, count: &mut i64) {
        let mut i = low;
        let mut j = mid+1;
        let mut temp = vec![0; (high-low+1) as usize];
        let mut p = 0;
        while i <= mid && j <= high {
            if nums[i as usize] > 2* nums[j as usize] {
                *count+=mid-i+1;
                j+=1;
            }
            else {
                i+=1;
            }
        }
        let mut i = low;
        let mut j = mid+1;
        
        while i <= mid && j <= high {
            if nums[i as usize] > nums[j as usize] {
                temp[p] = nums[j as usize];
                p+=1;
                j+=1;
            } else {
                temp[p] = nums[i as usize];
                p+=1;
                i+=1;
            }
        }
        for k in i..=mid {
            temp[p] = nums[k as usize];
            p+=1;
        }
        for k in j..=high {
            temp[p] = nums[k as usize];
            p+=1;
        }

        for i in 0..p {
            nums[low  as usize+i] = temp[i]; 
        }
    }
    
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        assert_eq!(Solution::reverse_pairs(vec![2147483647,2147483647,2147483647,2147483647,2147483647,2147483647]), 0);
    }
}

fn main() {}
