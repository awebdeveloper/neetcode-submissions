

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const input = nums.sort((a,b)=>a-b);
        const result = [];   

        for (let i = 0; i < input.length; i++) {
            if (input?.[i-1] == input[i]) {
                continue;
            }

            let end    = input.length - 1;
            let start  = i + 1;

            while (start < end) {
                let sum = input[start] + input[end] + input[i];
                if (sum  > 0) {
                    end--;
                } else if (sum  < 0) {
                    start++;
                } else if (sum == 0) {
                    result.push([input[i], input[start], input[end]]);
                    
                    start++;
                    while (start < end && input[start] === input[start - 1]) {
                        start++;
                    }
                }
            }
        }

        return result;
    }
}
