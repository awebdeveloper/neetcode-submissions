class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        const len = nums.length;
        for (let out = 0; out < len - 1; out++) {
            for (let inner = out+1;  inner < len ; inner++) {
                if (nums[inner] + nums[out] == target) {
                    return [out,inner]
                }
            }
        }


        // if i > target ignore

        // if i-target exists in rest 



    }
}
