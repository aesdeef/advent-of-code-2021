package day01

import java.io.File

fun main() {
    val depths = parseInput()
    val part1 = countIncreases(depths)
    val slidingWindows = getSlidingWindows(depths)
    val part2 = countIncreases(slidingWindows)

    println(part1)
    println(part2)
}

fun parseInput(): List<Int> {
    return File("../../input/01.txt")
        .readLines()
        .map { it.toInt() }
}

fun countIncreases(measurements: List<Int>): Int {
    return (measurements.dropLast(1) zip measurements.drop(1))
        .count { it.first < it.second }
}

fun getSlidingWindows(depths: List<Int>): List<Int> {
    return zipSum(
        zipSum(
            depths.dropLast(2),
            depths.dropLast(1).drop(1)
        ),
        depths.drop(2)
    )
}

fun zipSum(first: List<Int>, second: List<Int>): List<Int> {
    return (first zip second).map{ it.first + it.second }
}
