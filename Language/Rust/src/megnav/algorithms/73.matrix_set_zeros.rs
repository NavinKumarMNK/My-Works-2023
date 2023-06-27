// Leet Code 73 - Set Matrix Zeroes
struct Solution;

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut col0 = 1;
        let (m, n) = (matrix.len(), matrix[0].len());
        for i in 0..m {
            for j in 0..n {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    if j == 0 {col0 = 0;}
                    else {matrix[0][j] = 0;}                   
                } 
            }
        } 

        for i in (0..m).rev(){
            for j in (1..n).rev() {
                println!("matrix {} {} {}", i, j, matrix[i][j]);
            
                //row 
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0;
                }    
            }
        }

        for i in 0..m{
            if col0 == 0 || matrix[i][0] == 0 {
                matrix[i][0] = 0;
            }
        }
    }
} 

#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    fn test_1() {
        let mut matrix = vec![vec![1,1,1],vec![1,0,1],vec![1,1,1]];
        Solution::set_zeroes(&mut matrix);
        assert_eq!(matrix, vec![vec![1,0,1],vec![0,0,0],vec![1,0,1]]);
    }
}

fn main () {}