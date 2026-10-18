class Solution {
    
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hash = {};

        strs.forEach((s)=> {
            const key = new Array(26).fill(0);

            s.split("").forEach((letter)=>{
                key[letter.charCodeAt(0)-97] += 1;
            })

            hash[key] = hash[key] || [];
            hash[key].push(s);
        });

        return Object.values(hash);
    }
}
