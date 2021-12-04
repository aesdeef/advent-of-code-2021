package day02

import java.io.File

typealias Instruction = Pair<String, Int>

fun main() {
    val instructions = parseInput()
    val part1 = solvePart1(instructions)
    val part2 = solvePart2(instructions)
    println(part1)
    println(part2)
}

fun parseInput(): List<Instruction> {
    return File("../../input/02.txt")
        .readLines()
        .map { it.split(" ") }
        .map { Pair(it[0], it[1].toInt()) }
}

fun solvePart1(instructions: List<Instruction>): Int {
    var horizontal = 0
    var depth = 0

    instructions.forEach {
        val (command, value) = it
        when (command) {
            "forward" -> horizontal += value
            "down" -> depth += value
            "up" -> depth -= value
        }
    }

    return horizontal * depth
}

fun solvePart2(instructions: List<Instruction>): Int {
    var aim = 0
    var horizontal = 0
    var depth = 0

    instructions.forEach {
        val (command, value) = it
        when (command) {
            "forward" -> {
                horizontal += value
                depth += aim * value
            }
            "down" -> aim += value
            "up" -> aim -= value
        }
    }

    return horizontal * depth
}
