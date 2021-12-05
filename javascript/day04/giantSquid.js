import fs from 'fs'

/**
 * Parses a block of 5 lines (passed as a single string wih '\n's) and returns
 * an array of 5 rows, where each row is a list of 5 numbers (as strings)
 */
function parseBlock(block) {
  return block
    .split('\n')
    .map( row => row.trim().split(/ +/) )
}

/**
 * Parses the input and returns a list of numbers that were drawn and an array
 * of boards
 */
function parseInput() {
  const blocks = fs.readFileSync('../../input/04.txt', 'utf8')
    .trim()
    .split('\n\n')

  const draws = blocks.shift().split(',')
  const boards = blocks.map(parseBlock)

  return { draws, boards }
}

/**
 * Returns a transposed board
 */
function transpose(board) {
  return board[0].map((_, i) => board.map(row => row[i]))
}

/**
 * Returns an array of all lines (rows and columns) on a given board
 */
function boardLines(board) {
  const rows = board
  const columns = transpose(board)
  return rows.concat(columns)
}

/**
 * Calculates the score of the board at the moment one of the lines is completed
 */
function getScore(lines, lastDraw) {
  const sumOfRemainingNumbers = [].concat(...lines)
    .map(number => Number(number))
    .reduce((number, acc) => number + acc, 0) / 2

  return sumOfRemainingNumbers * Number(lastDraw)
}

/**
 * Goes through the drawn numbers and returns an object, where `turn` is the
 * turn on which the board wins, and `score` is the score of the board at that
 * moment
 */
function predictedWin(board, draws) {
  let lines = boardLines(board)
  for (let [i, draw] of draws.entries()) {
    lines = lines.map(line => line.filter(number => number !== draw))
    if (lines.some(line => line.length === 0)) {
      return {
        turn: i,
        score: getScore(lines, draw)
      }
    }
  }
}

/**
 * Analyses the boards one by one and returns predictions of the turn and score
 * at the moment the board wins, then sorts them by the turn number
 */
function getPredictions(boards, draws) {
  return boards
    .map(board => predictedWin(board, draws))
    .sort((a, b) => a.turn - b.turn)
}

const { draws, boards } = parseInput()
const predictions = getPredictions(boards, draws)
const part1 = predictions.shift().score
const part2 = predictions.pop().score

console.log(part1)
console.log(part2)
