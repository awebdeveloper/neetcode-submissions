class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(str) {
        let s = str.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
        let i = 0;
        let j = s.length - 1;


        console.log(s);

        while (j>=i) {
            if (s[i] !== s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
