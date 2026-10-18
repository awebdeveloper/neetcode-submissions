const sum = (arr)=> {
    return arr.reduce((result,curr) => result+curr ,0);
}

class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(input) {

        const nums = input
            .sort((a,b) => a - b)
            .filter((ele,i) => ele != input?.[i-1]);

        if (input.length === 0) {
            return 0;
        }


        let allList = [];
        let temp = [nums[0]];
        let prev = nums[0]

        for (let i = 1; i < nums.length; i++) {
            if (prev + 1 === nums[i]) {
                temp.push(nums[i]);
            } else {
                if (
                    allList.length == temp.length && sum(allList) < sum(temp) ||
                    allList.length < temp.length
                ) {
                    allList = temp;
                }
                //reset temp
                temp = [nums[i]];
            }
            prev = nums[i];
        }

        return (temp.length > allList.length) ?  temp.length :  allList.length;

    }
}
