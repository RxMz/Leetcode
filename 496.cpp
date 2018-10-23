class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> to_ret;
        for(int i = 0; i < findNums.size(); i++){
            int greater = -1;
            int index = 0;
            for(int k = 0; k < nums.size(); k++){
                if(findNums.at(i) == nums.at(k)){
                    index = k;
                    break;
                }
            }
            for(int j = index; j < nums.size(); j++){
                if(findNums.at(i) < nums.at(j)){
                    greater = nums.at(j);
                    break;
                }
            }
            to_ret.push_back(greater);
        }
        return to_ret;
    }
};
