use std::io;

// Logest Common Substring
struct Solution;
impl Solution {
    fn longest_common_substring_dp(string1: &str, string2: &str) -> i32 {
        let mut matrix = vec![vec![0; string2.len()]; string1.len()];
        let mut max = 0;
        for i in 0..string1.len(){
            for j in 0..string2.len(){
                if string1.chars().nth(i).unwrap() == string2.chars().nth(j).unwrap(){
                    if i == 0 || j == 0 {
                        matrix[i][j] = 1;
                    } else{
                        matrix[i][j] = matrix[i-1][j-1] + 1;
                    }
                } else {
                    matrix[i][j] = 0;
                }
                if max < matrix[i][j]{
                    max = matrix[i][j];
                }
            }
        }
        max
    }

    fn longest_common_substring_rf(string1: &str, string2: &str, i: i32, j: i32, count:&mut i32) -> i32 {
        if(i == 0 || j == 0){
            return *count;
        } 

        if string1.chars().nth(i as usize - 1).unwrap() == string2.chars().nth(j as usize - 1).unwrap(){
            *count = Solution::longest_common_substring_rf(string1, string2, i-1, j-1,  &mut (*count+1));

        }
        *count = std::cmp::max(*count,
                            std::cmp::max(Solution::longest_common_substring_rf(string1, string2, i-1, j, &mut 0),
                            Solution::longest_common_substring_rf(string1, string2, i, j-1, &mut 0)
                        ));   

        *count
    }

}

// Test
fn main(){
    let mut string1 = String::new();
    let mut string2 = String::new();
    io::stdin().read_line(&mut string1);
    io::stdin().read_line(&mut string2);

    let num = Solution::longest_common_substring_dp(&string1.trim(), &string2.trim());
    println!("{}", num);

    let mut count = 0;
    let num = Solution::longest_common_substring_rf(&string1.trim(), &string2.trim(), string1.trim().len() as i32, string2..trim().len() as i32, &mut count);
    println!("{}", num);
}
