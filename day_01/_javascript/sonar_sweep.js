import fs from 'fs'

function parseInput() {
  return fs.readFileSync('../input.txt', 'utf8')
    .trim()
    .split('\n')
    .map(line => parseInt(line))
}

function countIncreases(measurements) {
  return measurements
    .filter((measurement, i, array) => i > 0 && measurement > array[i - 1])
    .length
}

function getSlidingWindows(depths) {
  return depths.map((depth, i, depths) => {
    if (i < 2) return 0
    return depths[i - 2] + depths[i - 1] + depth
  }).slice(2)
}

const depths = parseInput()
const part1 = countIncreases(depths)
const slidingWindows = getSlidingWindows(depths)
const part2 = countIncreases(slidingWindows)

console.log(part1)
console.log(part2)
