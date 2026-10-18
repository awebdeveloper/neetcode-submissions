class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const duplicate = {}

        for (let num of nums) {
            if (duplicate[num] === num) {
                return true;
            } else {
                duplicate[num] = num;
            }
        }
        return false;
    }
}
