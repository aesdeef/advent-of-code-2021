import fs from 'fs'

function parseInput() {
  return fs.readFileSync('../input.txt', 'utf8')
    .trim()
    .split('\n')
    .map(line => {
      const [command, value] = line.split(' ')
      return { command, value: +value }
    })
}

function solvePart1(instructions) {
  let horizontal = 0
  let depth = 0

  for (const { command, value } of instructions) {
    if (command === "forward") {
      horizontal += value
    } else if (command === "down") {
      depth += value
    } else if (command === "up") {
      depth -= value
    }
  }

  return horizontal * depth
}

function solvePart2(instructions) {
  let aim = 0
  let horizontal = 0
  let depth = 0

  for (const { command, value } of instructions) {
    if (command === "forward") {
      horizontal += value
      depth += aim * value
    } else if (command === "down") {
      aim += value
    } else if (command === "up") {
      aim -= value
    }
  }

  return horizontal * depth
}

const instructions = parseInput()
const part1 = solvePart1(instructions)
const part2 = solvePart2(instructions)

console.log(part1)
console.log(part2)
