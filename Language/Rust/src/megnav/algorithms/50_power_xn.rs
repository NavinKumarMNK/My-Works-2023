// LeetCode pow(x, n) - leetcode 50
struct Solution;

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if n == 0 {
            return 1.0;
        }
        if n % 2 == 0 {
            Solution::my_pow(x, n / 2) * Solution::my_pow(x, n / 2)
        } else {
            if n > 0 {
                x * Solution::my_pow(x, n / 2) * Solution::my_pow(x, n / 2)
        
            } else {    
                (Solution::my_pow(x, n / 2) * Solution::my_pow(x, n / 2)) / x
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_my_pow() {
        assert_eq!(Solution::my_pow(2.0, 10), 1024.0);
        assert_eq!(Solution::my_pow(2.1, 3), 9.261);
        assert_eq!(Solution::my_pow(2.0, -2), 0.25);
    }
}

fn main() {}
