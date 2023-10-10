class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1=0, cnt2=0;
        int ele1=0, ele2=0;

        for (int i=0; i < nums.size(); i++) {
            if (cnt1 == 0 && nums[i] != ele2) {
                cnt1 = 1;
                ele1 = nums[i];
            } 
            else if (cnt2 == 0 && nums[i] != ele1) {
                ele2 = nums[i];
                cnt2 = 1;
            }
            else if (ele1 == nums[i]) {
                cnt1++;
            }
            else if (ele2 == nums[i]) {
                cnt2++;
            }
            else {
                cnt1--;
                cnt2--;
            }
        }

        vector <int> ans;
        int n = nums.size()/3;
        cnt1 = 0, cnt2 = 0;
        for (int i=0; i < nums.size(); i++) {
            if (ele1 == nums[i]) {
                cnt1++;
            }
            else if (ele2 == nums[i]) {
                cnt2++;
            }
        } 

        if (cnt1 > n) {
            ans.push_back(ele1);
        }
        if (cnt2 > n) {
            ans.push_back(ele2);
        }
        return ans;
    }
};
