import fs from 'fs'

/**
 * Parses the data and returns a list of binary entries
 */
function parseInput() {
  return fs.readFileSync('../../input/03.txt', 'utf8')
    .trim()
    .split('\n')
}

/**
 * Returns the numbers of occurrences of "1"s and "0"s in bits
 */
function countBits(bits) {
  const ones = bits.filter(x => x === "1").length
  const zeros = bits.filter(x => x === "0").length
  return { ones, zeros }
}

/**
 * Returns the more common bit or "1" if both are equally common
 */
function moreCommonBit(bits) {
  const { ones, zeros } = countBits(bits)
  return ones >= zeros ? "1" : "0"
}

/**
 * Returns the less common bit or "0" if both are equally common
 */
function lessCommonBit(bits) {
  const { ones, zeros } = countBits(bits)
  return ones >= zeros ? "0" : "1"
}

/**
 * Parses two strings representing binary numbers and multiplies them
 */
function multiplyBinary(first, second) {
  return parseInt(first, 2) * parseInt(second, 2)
}

/**
 * Finds the solution to part 1 (the power consumption of the submarine)
 */
function solvePart1(data) {
  var gamma = ""
  var epsilon = ""

  for (let i = 0; i < data[0].length; i++) {
    const bits = data.map(entry => entry[i])
    gamma += moreCommonBit(bits)
    epsilon += lessCommonBit(bits)
  }

  return multiplyBinary(gamma, epsilon)
}

/**
 * Finds the rating by going through each bit position and keeping only those
 * entries where the ith bit matches the one returned by the keepCondition
 * function
 */
function findRating(data, keepCondition) {
  for (let i = 0; i < data[0].length; i++) {
    const bits = data.map(entry => entry[i])
    data = data.filter(entry => entry[i] === keepCondition(bits))

    if (data.length === 1) return data[0]
  }
}

/**
 * Finds the solution to part 2 (the life support rating of the submarine)
 */
function solvePart2(data) {
  const oxygenGeneratorRating = findRating(data, moreCommonBit)
  const co2ScrubberRating = findRating(data, lessCommonBit)

  return multiplyBinary(oxygenGeneratorRating, co2ScrubberRating)
}

const data = parseInput()
const part1 = solvePart1(data)
const part2 = solvePart2(data)
console.log(part1)
console.log(part2)
