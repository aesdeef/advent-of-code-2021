module Day03 exposing (..)

import Solution exposing (Solution)


solve : String -> Solution
solve input =
    let
        entries =
            parseInput input
    in
    { part1 = answerPart1 entries
    , part2 = answerPart2 entries
    }


type alias Entry =
    List Int


parseEntry : String -> Entry
parseEntry entry =
    entry
        |> String.toList
        |> List.map String.fromChar
        |> List.filterMap String.toInt


parseInput : String -> List Entry
parseInput input =
    input
        |> String.lines
        |> List.map parseEntry


entryToInt : Entry -> Int
entryToInt =
    List.foldl (\bit total -> total * 2 + bit) 0


moreCommonBit : List Entry -> Int -> Int
moreCommonBit entries position =
    let
        numberOfOnes =
            entries
                |> List.map (List.drop position)
                |> List.filterMap List.head
                |> List.sum

        moreOnesOrEqual =
            (numberOfOnes * 2) >= List.length entries
    in
    if moreOnesOrEqual then
        1

    else
        0


lessCommonBit : List Entry -> Int -> Int
lessCommonBit entries position =
    1 - moreCommonBit entries position



-- PART 1


rate : List Entry -> (List Entry -> Int -> Int) -> Int
rate entries function =
    let
        entryLength =
            12
    in
    List.range 0 (entryLength - 1)
        |> List.map (function entries)
        |> entryToInt


answerPart1 : List Entry -> String
answerPart1 entries =
    let
        gamma =
            rate entries moreCommonBit

        epsilon =
            rate entries lessCommonBit
    in
    gamma
        * epsilon
        |> String.fromInt



-- PART 2


rating : List Entry -> (List Entry -> Int -> Int) -> Int -> Int
rating entries function accumulator =
    let
        bit =
            function entries 0

        newAccumulator =
            accumulator * 2 + bit

        newEntries =
            entries
                |> List.filter (\entry -> List.head entry == Just bit)
                |> List.filterMap List.tail
    in
    case entries of
        last :: [] ->
            (accumulator * 2 ^ List.length last) + entryToInt last

        _ ->
            rating newEntries function newAccumulator


answerPart2 : List Entry -> String
answerPart2 entries =
    let
        oxygen =
            rating entries moreCommonBit 0

        co2 =
            rating entries lessCommonBit 0
    in
    oxygen
        * co2
        |> String.fromInt
