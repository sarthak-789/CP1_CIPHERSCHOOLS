// link: https://leetcode.com/problems/pascals-triangle-ii

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> result;
        vector<int> helper;
        for (int i = 0; i < rowIndex+1; i++){
            for (int j = 0; j <= i; j++){
                if (i==j || j==0){
                    helper.push_back(1);
                }
                else{
                    helper.push_back(result[i-1][j-1]+result[i-1][j]);
                }
            }
            result.push_back(helper);
            helper.erase(helper.begin(),helper.end());
        }
        return result[rowIndex];
    }
};