module Day02 exposing (..)

import Maybe exposing (andThen)
import Solution exposing (Solution)


solve : String -> Solution
solve input =
    let
        commands =
            parseInput input
    in
    { part1 = answerPart1 commands
    , part2 = answerPart2 commands
    }


type Command
    = Forward Int
    | Down Int
    | Up Int


parseCommand : String -> Int -> Maybe Command
parseCommand command value =
    case command of
        "forward" ->
            Just (Forward value)

        "down" ->
            Just (Down value)

        "up" ->
            Just (Up value)

        _ ->
            Nothing


parseWords : List String -> Maybe Command
parseWords words =
    case words of
        first :: second :: [] ->
            String.toInt second
                |> andThen (parseCommand first)

        _ ->
            Nothing


parseLine : String -> Maybe Command
parseLine line =
    line
        |> String.words
        |> parseWords


parseInput : String -> List Command
parseInput input =
    input
        |> String.lines
        |> List.filterMap parseLine



-- PART 1


type alias ModelPart1 =
    { horizontal : Int
    , depth : Int
    }


stepPart1 : Command -> ModelPart1 -> ModelPart1
stepPart1 command init =
    case command of
        Forward value ->
            { init | horizontal = init.horizontal + value }

        Down value ->
            { init | depth = init.depth + value }

        Up value ->
            { init | depth = init.depth - value }


initPart1 : ModelPart1
initPart1 =
    { horizontal = 0, depth = 0 }


answerPart1 : List Command -> String
answerPart1 commands =
    commands
        |> List.foldl stepPart1 initPart1
        |> (\values -> values.horizontal * values.depth)
        |> String.fromInt



-- PART 2


type alias ModelPart2 =
    { horizontal : Int
    , depth : Int
    , aim : Int
    }


stepPart2 : Command -> ModelPart2 -> ModelPart2
stepPart2 command init =
    case command of
        Forward value ->
            { init | horizontal = init.horizontal + value, depth = init.depth + init.aim * value }

        Down value ->
            { init | aim = init.aim + value }

        Up value ->
            { init | aim = init.aim - value }


initPart2 : ModelPart2
initPart2 =
    { horizontal = 0, depth = 0, aim = 0 }


answerPart2 : List Command -> String
answerPart2 commands =
    commands
        |> List.foldl stepPart2 initPart2
        |> (\values -> values.horizontal * values.depth)
        |> String.fromInt
