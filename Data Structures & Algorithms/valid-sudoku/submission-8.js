class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
   isValidSudoku(board) {
    const rows = {};
    const cols = {};
    const group = {};

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            const ele = board[i][j];
            const key = `${parseInt(i / 3, 10)}${parseInt(j / 3, 10)}`;

            if (ele === ".") {
                continue;
            } 

            if(rows[i]?.has(ele) || cols[j]?.has(ele) || group[key]?.has(ele)){
                return false;
            }

            rows[i] = rows[i] || new Set();
            cols[j] = cols[j] || new Set();
            group[key] = group[key] || new Set();
            rows[i].add(ele);
            cols[j].add(ele);
            group[key].add(ele);

        }
    }

    return true;
}
}