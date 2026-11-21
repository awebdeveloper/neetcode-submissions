#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int area  = 0;
        int prev  = 0;
        for (int i=0; i < heights.size(); i++) {
            if (prev > heights[i]) {
                continue;
            }
            for (int j=i+1; j < heights.size(); j++) {
                int currentArea = (j-i) * min(heights[j],heights[i]);
                area = max(currentArea, area);
            }
            prev = heights[i];
        }

        return area;
    }
};
