//
// Created by zizheng zhang on 2019-08-22.
//
#include <vector>
#include <iostream>
class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        if (nums.empty()){
            return std::vector<int> {};
        }
        int maxPosition = -1;
        int minNum = *std::min_element(nums.begin(), nums.end());
        int maxNums = minNum;
        std::vector<int> result;
        for (int i = k - 1; i < nums.size(); ++i){
            if (maxNums != -1 && i - k + 1 <= maxPosition && maxPosition < i){
                    if (nums[i] > maxNums) {
                        maxNums = nums[i];
                        maxPosition = i;
                    }
            }
            else{
                int subMax = minNum;
                int subPos = 0;
                for (int j = i - k + 1; j <= i; ++j){
                    if (nums[j] >= subMax){
                        subMax = nums[j];
                        subPos = j;
                    }
                }
                maxPosition = subPos;
                maxNums = subMax;

            }
            result.push_back(maxNums);
        }
        return result;
    }
};