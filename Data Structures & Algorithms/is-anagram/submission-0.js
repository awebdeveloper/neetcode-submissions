class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const hash = new Array(26).fill(0);
        if (s.length !== t.length) {
            return false;
        }

        for (let i=0; i<s.length; i++) {
            const sKey = s.charCodeAt(i) - 97;
            const tKey = t.charCodeAt(i) - 97;
            hash[sKey] = hash[sKey] + 1;
            hash[tKey] = hash[tKey] - 1;
        }

        return hash.every((ele) => ele === 0);
    }
}
