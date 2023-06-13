impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let n = nums.len();
        let mut low: i32 = 0;
        let mut mid: i32 = 0;
        let mut high: i32 = n as i32 -1;

        while mid <= high && high > 0 {
            if(nums[mid as usize]==0) {nums.swap(mid as usize, low as usize); low+=1; mid+=1;}
            else if(nums[mid as usize]==1) {mid+=1;}
            else if(nums[mid as usize]==2) {nums.swap(mid as usize, high as usize); high-=1;}
            println!("{:?}", nums)
        }
    }
}