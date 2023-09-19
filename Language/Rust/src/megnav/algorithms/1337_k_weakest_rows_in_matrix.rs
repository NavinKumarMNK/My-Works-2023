use std::cmp::Ordering;

impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut row_strength: Vec<(i32, i32)> = mat.iter().enumerate().map(|(i, row)| {
            (row.iter().sum(), i as i32)
        }).collect();

        row_strength.sort_by(|a, b| {
            match a.0.cmp(&b.0) {
                Ordering::Equal => a.1.cmp(&b.1),
                other => other
            }
        }); // Unstable sort

        row_strength.into_iter().map(|(_, i)| i).take(k as usize).collect() 
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_1337() {
        let mat = vec![vec![1, 1, 0, 0, 0],
                       vec![1, 1, 1, 1, 0],
                       vec![1, 0, 0, 0, 0],
                       vec![1, 1, 0, 0, 0],
                       vec![1, 1, 1, 1, 1]];
        let k = 3;
        let res = Solution::k_weakest_rows(mat, k);
        assert_eq!(res, vec![2, 0, 3]);
    }
}
