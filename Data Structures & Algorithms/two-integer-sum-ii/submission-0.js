class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(num, target) {
        let i = 0;
        let j = num.length-1;
        let counter = 0;



        while (i < j && counter++ < num.length) {
            let sum = num[i] + num[j];

            if (sum > target) {
                j--;
            } else if (sum < target) {
                i++;
            } else if (sum == target) {
                return [i+1,j+1];
            }
        }
    }
}
