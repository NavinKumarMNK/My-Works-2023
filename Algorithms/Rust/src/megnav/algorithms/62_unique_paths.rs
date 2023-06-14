// LeetCode 62. Unique Paths
struct Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut array = vec![vec![-1; n as usize]; m as usize];
        Solution::recursive(m, n, 0, 0, &mut array)
    }

    pub fn recursive(m:i32, n:i32, i:i32, j:i32, array:&mut Vec<Vec<i32>>) -> i32 {
        if i == m-1 && j == n-1 {
            return 1;
        }
        if i >= m || j >= n {
            return 0;
        }

        if array[i as usize][j as usize] != -1 {
            return array[i as usize][j as usize];
        }

        array[i as usize][j as usize] = Solution::recursive(m,n, i+1, j, array) + Solution::recursive(m,n, i, j+1, array);
        array[i as usize][j as usize]

    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_62() {
        let m = 3;
        let n = 7;
        let res = Solution::unique_paths(m, n);
        assert_eq!(res, 28);
    }
}

fn main() {}
