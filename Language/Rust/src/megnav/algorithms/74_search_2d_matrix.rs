// LeetCode 74 - Search a 2D Matrix
struct Solution;

impl Solution {
    pub fn search_matrix(mut matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (m, n) = (matrix.len() as i32, matrix[0].len() as i32);
        let mut vec = Vec::with_capacity(n as usize);
        for i in 0..m {
            vec.push(matrix[i as usize][0]);
        }
        println!("vec: {:?}", vec);
        let mut index:i32 = 0; 
        let mut value:i32 = i32::MAX;
        Solution::binary_search_approx(&mut vec, 0, m-1, &mut index, target, &mut value);       

        println!("index: {}", index);
        let mut count = -1;
        Solution::binary_search(&mut matrix[index as usize], 0, n-1, &mut count, target);
        println!("count: {}", count);

        if count == -1 {
            return false;
        }
        return true;
    }

    pub fn binary_search(vec: &mut Vec<i32>, low:i32, high:i32, count:&mut i32, target: i32) {
        if low > high {return;}
        let mid = (low+high) / 2;
        if vec[mid as usize] == target {
            *count = mid as i32;
            return;
        } else if vec[mid as usize] > target {
            Solution::binary_search(vec, low, mid-1, count, target);
        } else {
            Solution::binary_search(vec, mid+1, high, count, target);
        }
    }

    pub fn binary_search_approx(vec: &mut Vec<i32>, low:i32, high:i32, count:&mut i32, target: i32, value: &mut i32) {
        if low > high {return;}
        let mid = (low+high) / 2;
        if vec[mid as usize] == target {
            *count = mid as i32;
            *value = 0;
            return;
        } else if target - vec[mid as usize] > 0 && target - vec[mid as usize] <= *value {
            *count = mid as i32;
            *value = target - vec[mid as usize];
        }
        if vec[mid as usize] > target {
            Solution::binary_search_approx(vec, low, mid-1, count, target, value);
        } else {
            Solution::binary_search_approx(vec, mid+1, high, count, target, value);
        }
    }
}

impl Solution {
    pub fn search_matrix(mut matrix: Vec<Vec<i32>>, target: i32) -> bool {
        matrix.concat().binary_search(&target).is_ok() 
    }
}


use std::cmp::Ordering;
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let matrix = matrix.concat();
        return Self::search(&matrix, target).is_some()
        
    }
    fn search(nums: &[i32], target: i32) -> Option<usize> { 
        let (mut l, mut r) = (0, nums.len());
        while l < r { 
            let m = (l + r) / 2;
            match nums[m as usize].cmp(&target) { 
                Ordering::Greater => r = m,
                Ordering::Less => l = m + 1,
                Ordering::Equal => return Some(m as usize)
            }
        }
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_74() {
        let matrix = vec![vec![1], vec![3]];
        let target =3;
        let res = Solution::search_matrix(matrix, target);
        assert_eq!(res, true);
    }
}

fn main() {}
