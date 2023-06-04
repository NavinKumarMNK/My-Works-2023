use std::io;
use std::cmp::max;

// Knuth-Morris-Pratt Algorithm     
struct Solution;
impl Solution {
    fn kmp(string: String, pattern:String) -> i32{
        let lps = Solution::compute_lps(pattern.clone());
        println!("{:?}", lps);
        let bytes_string = string.as_bytes();
        let bytes_pattern = pattern.as_bytes();    


        let mut i = 0;
        let mut j = -1 as i32;

        while i < bytes_string.len() {
            if bytes_string[i] == bytes_pattern[(j + 1) as usize]{
                i+=1;
                j+=1;
            } else {
                if j != -1 {
                    j = lps[j as usize] as i32 -1;
                } else {
                    i+=1;

                }
                
            }
            if j == bytes_pattern.len() as i32 - 1 {
                return (i - bytes_pattern.len()) as i32;
            }
        }
            -1
    }
    
    fn compute_lps(pattern: String) -> Vec<usize>{
        let mut lps = vec![0; pattern.len()];
        let bytes_pattern = pattern.as_bytes();
        lps[0] = 0;
        
        let mut i = 1;
        let mut len = 0;
        while i < bytes_pattern.len(){ 
            if bytes_pattern[i] == bytes_pattern[len]{
                len +=1;
                lps[i] = len;
                i +=1;
            } else {
                if len != 0 {
                    len = lps[len-1];
                } else {
                    lps[i] = 0;
                    i +=1;
                }
            }
        }
        lps
    }
}

fn main(){
    // Test 
    let string = String::from("ababcabcabababd");
    let pattern  = String::from("ababdewfs");   
    let result = Solution::kmp(string, pattern);
    println!("{}", result);

} 