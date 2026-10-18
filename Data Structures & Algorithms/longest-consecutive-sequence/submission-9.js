const sum = (arr)=> {
    return arr.reduce((result, curr) => result + curr ,0);
}

class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(input) {
        const set = new Set(input);
        let maxLength = 0;

        for (let i = 0; i < input.length; i++) {
            if (i == 0) {
                maxLength = 1;
            }
            if (i > 0 && set.has(input[i]-1)) {
                continue;   
            }

            let tempLength = 1;
            for (let j = 1; j <= input.length; j++) {
                if (set.has(input[i]+j)) {
                    tempLength++;
                } else {
                    break;
                }
            }
            maxLength = (tempLength > maxLength) ? tempLength : maxLength;
        }

        return maxLength;

    }
}
