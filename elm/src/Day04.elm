module Day04 exposing (..)

import Solution exposing (Solution)


{-| Returns the answers to the problem
-}
solve : String -> Solution
solve input =
    let
        draws =
            Tuple.first (parseInput input)

        boards =
            Tuple.second (parseInput input)
    in
    { part1 = answerPart1 draws boards
    , part2 = answerPart2 draws boards
    }


type alias Draws =
    List Int


type alias Board =
    List (List Int)


{-| Parses the drawn numbers string
-}
parseDraws : Maybe String -> Draws
parseDraws draws =
    case draws of
        Just string ->
            string
                |> String.split ","
                |> List.filterMap String.toInt

        Nothing ->
            []


{-| Parses a board row
-}
parseRow : String -> List Int
parseRow row =
    row
        |> String.words
        |> List.filterMap String.toInt


{-| Parses a block (passed as a string with '\\n's) and returns a Board
-}
parseBoard : String -> Board
parseBoard block =
    block
        |> String.split "\n"
        |> List.map parseRow


{-| Parses the input and returns a tuple of draws and boards
-}
parseInput : String -> ( Draws, List Board )
parseInput input =
    let
        blocks =
            input
                |> (\str ->
                        if String.endsWith "\n" str then
                            String.dropRight 1 str

                        else
                            str
                   )
                |> String.split "\n\n"

        draws =
            blocks
                |> List.head
                |> parseDraws

        boards =
            blocks
                |> List.drop 1
                |> List.map parseBoard
    in
    ( draws, boards )


{-| Transposes the board
-}
transpose : Board -> Board
transpose board =
    let
        nth n list =
            List.drop n list |> List.head
    in
    board
        |> List.indexedMap (\i _ -> board |> List.filterMap (nth i))


{-| Returns all lines on the board (rows and columns)
-}
boardLines : Board -> List (List Int)
boardLines board =
    let
        rows =
            board

        columns =
            transpose board
    in
    List.append rows columns


{-| Returns the numbers on the board that have not yet been marked
-}
remainingNumbers : Draws -> List Int -> List Int
remainingNumbers draws line =
    let
        notDrawn drawn number =
            not (List.member number drawn)
    in
    line
        |> List.filter (notDrawn draws)


{-| Finds the last draw (or returns 0 if for some reason it can't find it)
-}
lastDraw : Draws -> Int
lastDraw draws =
    case draws |> List.reverse |> List.head of
        Just last ->
            last

        Nothing ->
            0


{-| Returns the final score for the board
-}
boardScore : Board -> Draws -> Int
boardScore board draws =
    (board
        |> List.map (remainingNumbers draws)
        |> List.map List.sum
        |> List.sum
    )
        * lastDraw draws


{-| Checks if the board wins and retuns Just score if it does, Nothing otherwise
-}
checkBoard : Board -> Draws -> Maybe Int
checkBoard board draws =
    let
        score =
            boardScore board draws

        won =
            board
                |> boardLines
                |> List.map (remainingNumbers draws)
                |> List.any List.isEmpty
    in
    if won then
        Just score

    else
        Nothing


type alias Prediction =
    { turn : Int, score : Int }


{-| Finds the turn on which the board wins and the score at that moment
-}
predictedWin : Draws -> Int -> Board -> Prediction
predictedWin draws counter board =
    let
        outcome =
            checkBoard board (List.take counter draws)
    in
    case outcome of
        Just score ->
            { turn = counter, score = score }

        Nothing ->
            predictedWin draws (counter + 1) board


{-| Finds the expected turn number and score at the moment each board wins
-}
getPredictions : List Board -> Draws -> List Prediction
getPredictions boards draws =
    boards
        |> List.map (predictedWin draws 1)
        |> List.sortBy .turn



-- PART 1


{-| Finds the first winning board and returns the score as a String
-}
answerPart1 : Draws -> List Board -> String
answerPart1 draws boards =
    let
        predictions =
            getPredictions boards draws

        first =
            List.head predictions
    in
    case first of
        Just { score } ->
            String.fromInt score

        _ ->
            "not found"



-- PART 2


{-| Finds the last winning board and returns the score as a String
-}
answerPart2 : Draws -> List Board -> String
answerPart2 draws boards =
    let
        predictions =
            getPredictions boards draws

        last =
            predictions
                |> List.reverse
                |> List.head
    in
    case last of
        Just { score } ->
            String.fromInt score

        _ ->
            "not found"
