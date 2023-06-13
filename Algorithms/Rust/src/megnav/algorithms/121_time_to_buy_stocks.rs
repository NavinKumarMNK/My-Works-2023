// Leet Code  121. Best Time to Buy and Sell Stock
struct Solution;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices.iter()
              .fold((0, prices[0]), |(profit, mini), i| {
                  (
                  profit.max(i - mini),
                  mini.min(*i),
                    )
              }).0        
    }
}

#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    fn test_1() {
        assert_eq!(Solution::max_profit(vec![7,1,5,3,6,4]), 5);
    }
    
}

fn main () {}