module Solver exposing (solve)

import Day01
import Day02
import Day03
import Day04
import Day05
import Day06
import Day07
import Day08
import Day09
import Day10
import Day11
import Day12
import Day13
import Day14
import Day15
import Day16
import Day17
import Day18
import Day19
import Day20
import Day21
import Day22
import Day23
import Day24
import Day25
import Solution exposing (Solution)


solve : String -> String -> Solution
solve id input =
    case id of
        "01" ->
            Day01.solve input

        "02" ->
            Day02.solve input

        "03" ->
            Day03.solve input

        "04" ->
            Day04.solve input

        "05" ->
            Day05.solve input

        "06" ->
            Day06.solve input

        "07" ->
            Day07.solve input

        "08" ->
            Day08.solve input

        "09" ->
            Day09.solve input

        "10" ->
            Day10.solve input

        "11" ->
            Day11.solve input

        "12" ->
            Day12.solve input

        "13" ->
            Day13.solve input

        "14" ->
            Day14.solve input

        "15" ->
            Day15.solve input

        "16" ->
            Day16.solve input

        "17" ->
            Day17.solve input

        "18" ->
            Day18.solve input

        "19" ->
            Day19.solve input

        "20" ->
            Day20.solve input

        "21" ->
            Day21.solve input

        "22" ->
            Day22.solve input

        "23" ->
            Day23.solve input

        "24" ->
            Day24.solve input

        "25" ->
            Day25.solve input

        _ ->
            { part1 = "not available", part2 = "not available" }
