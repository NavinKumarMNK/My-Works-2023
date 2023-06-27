// LeetCode Rotate Image (48)
struct Solution;

impl Solution {
    pub fn rotate_loop(matrix: &mut [Vec<i32>], row_range: std::ops::Range<usize>) {
        let m = row_range.end - 1;
        let start = row_range.start;
        for i in start..m {
            let pos = [(i, m), (m, m - i + start), (m - i + start, start), (start, i)];
            let mut temp1 = matrix[start][i];
            let mut temp2 = 0;
            for j in 0..4 {
                temp2 = matrix[pos[j].0][pos[j].1];
                matrix[pos[j].0][pos[j].1] = temp1;
                temp1 = temp2;
            }
        }
    }

    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let m = matrix.len() - 1;
        let mut i = 0;
        while i < m - i {
            Solution::rotate_loop(matrix, i..(m - i + 1));
            i += 1;
        }
    }
}

impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        matrix.iter_mut().for_each(|row| row.reverse());
        let m = matrix.len();
        (1..m - 1)
            .map(|i| ((i, 0), (m - 1, m - i - 1)))
            .chain((0..m - 1).map(|j| ((0, j), (m - j - 1, m - 1))))
            .for_each(|coords| {
                std::iter::successors(Some(coords), |((r1, c1), (r2, c2))| {
                    Some(((*r1 + 1, *c1 + 1), (r2.wrapping_sub(1), c2.wrapping_sub(1))))
                })
                .take_while(|((r1, _), (r2, _))| *r1 < *r2)
                .for_each(|((r1, c1), (r2, c2))| {
                    let t = matrix[r1][c1];
                    matrix[r1][c1] = matrix[r2][c2];
                    matrix[r2][c2] = t;
                })
            })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let mut matrix = vec![
            vec![5, 1, 9, 11],
            vec![2, 4, 8, 10],
            vec![13, 3, 6, 7],
            vec![15, 14, 12, 16],
        ];
        Solution::rotate(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec![15, 13, 2, 5],
                vec![14, 3, 4, 1],
                vec![12, 6, 8, 9],
                vec![16, 7, 10, 11],
            ]
        );
    }
}

fn main() {}
