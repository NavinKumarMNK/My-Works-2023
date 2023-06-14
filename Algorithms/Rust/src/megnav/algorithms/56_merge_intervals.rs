// LeetCode 56 - Merge Intervals
struct Solution;

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = intervals.len();
        if n == 0 {return vec![];}
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut res: Vec<Vec<i32>> = Vec::new();
        res.push(intervals[0].clone());
        for i in 1..n {
            let last = res.last_mut().unwrap();
            if intervals[i][0] <= last[1] {
                last[1] = last[1].max(intervals[i][1]);
            } else {
                res.push(intervals[i].clone());
            }
        }
        res
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_56() {
        let mut intervals = vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]];
        let res = Solution::merge(intervals);
        assert_eq!(res, vec![vec![1, 6], vec![8, 10], vec![15, 18]]);
    }
}

fn main() {}
