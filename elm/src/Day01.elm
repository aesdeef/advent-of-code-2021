module Day01 exposing (..)

import Solution exposing (Solution)


solve : String -> Solution
solve input =
    { part1 = answer input 1
    , part2 = answer input 3
    }


parseInput : String -> List Int
parseInput input =
    input
        |> String.lines
        |> List.filterMap String.toInt


countIncreases : Int -> List Int -> Int
countIncreases gap depths =
    List.map2 (<) depths (List.drop gap depths)
        |> List.filter (\x -> x)
        |> List.length


answer : String -> Int -> String
answer input gap =
    input
        |> parseInput
        |> countIncreases gap
        |> String.fromInt
