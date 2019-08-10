//
// Created by zizheng zhang on 2019-07-25.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:

    int FindStart(vector<int> nums, int start, int end){
        int index = (start + end) / 2;
        if (start == end){
            return index;
        }
        if (index - 1 >= 0 && nums[index - 1] > nums[index]){
            return index;
        }
        if (index + 1 < nums.size() && nums[index] > nums[index + 1]){
            return index + 1;
        }
        if (nums[start] >= nums[index]){
            return FindStart(nums, start, index);
        }
        if (nums[index] >= nums[end]){
            return FindStart(nums, index, end);
        }
        return 0;
    }

    int BinarySearch(vector<int> nums, int target, int start, int end){
        if (start > end){
            return -1;
        }

        int index = (start + end) / 2;
        if (nums[index] < target){
            return BinarySearch(nums, target, index + 1, end);
        }
        else if (nums[index] == target){
            return index;
        }
        else if (nums[index] > target){
            return BinarySearch(nums, target, start, index - 1);
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {
        if (nums.size() == 0){
            return -1;
        }

        int result = -1;
        int start_index = FindStart(nums, 0, nums.size() - 1);
//        cout << start_index << endl;
        if (target <= nums.back()){
            result = BinarySearch(nums, target, start_index, nums.size() - 1);
        }
        else{
            result = BinarySearch(nums, target, 0, start_index);
        }


        return result;
    }
};

int main(){
    Solution s;
    vector<int> input_array({1, 3});
//    vector<int> input_array({0,1,2,3,4,5,6,7});
    int target = 0;
    cout << s.search(input_array, target);
}