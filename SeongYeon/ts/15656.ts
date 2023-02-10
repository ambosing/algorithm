// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result = '';
const [n, m] = input[0]!.split(' ').map(Number);
const inputList: number[] = input[1]!
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
const nums: number[] = new Array(m);

// solution
const dfs = (depth: number) => {
  if (depth === m) {
    result += nums.join(' ') + '\n';
    return;
  }
  for (let i = 0; i < n!; i++) {
    nums[depth] = inputList[i]!;
    dfs(depth + 1);
  }
};

dfs(0);

// output
console.log(result);
