module TestDay04 exposing (..)

import Day04
import Expect exposing (Expectation, equal)
import Fuzz exposing (Fuzzer, int, list, string)
import Test exposing (..)


suite : Test
suite =
    describe "Day 04"
        [ describe "parseRow"
            [ test "example board 1 row 1" <|
                \_ ->
                    Day04.parseRow "22 13 17 11  0"
                        |> Expect.equal [ 22, 13, 17, 11, 0 ]
            , test "example board 3 row 5" <|
                \_ ->
                    Day04.parseRow " 2  0 12  3  7"
                        |> Expect.equal [ 2, 0, 12, 3, 7 ]
            ]
        , describe "parseBoard"
            [ test "example board 1" <|
                \_ ->
                    Day04.parseBoard "22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19"
                        |> Expect.equal
                            [ [ 22, 13, 17, 11, 0 ]
                            , [ 8, 2, 23, 4, 24 ]
                            , [ 21, 9, 14, 16, 7 ]
                            , [ 6, 10, 3, 18, 5 ]
                            , [ 1, 12, 20, 15, 19 ]
                            ]
            ]
        , describe "parseInput"
            [ test "the entire sample input" <|
                \_ ->
                    Day04.parseInput "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19\n\n 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6\n\n14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7"
                        |> Expect.equal
                            ( [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1 ]
                            , [ [ [ 22, 13, 17, 11, 0 ]
                                , [ 8, 2, 23, 4, 24 ]
                                , [ 21, 9, 14, 16, 7 ]
                                , [ 6, 10, 3, 18, 5 ]
                                , [ 1, 12, 20, 15, 19 ]
                                ]
                              , [ [ 3, 15, 0, 2, 22 ]
                                , [ 9, 18, 13, 17, 5 ]
                                , [ 19, 8, 7, 25, 23 ]
                                , [ 20, 11, 10, 24, 4 ]
                                , [ 14, 21, 16, 12, 6 ]
                                ]
                              , [ [ 14, 21, 17, 24, 4 ]
                                , [ 10, 16, 15, 9, 19 ]
                                , [ 18, 8, 23, 26, 20 ]
                                , [ 22, 11, 13, 6, 5 ]
                                , [ 2, 0, 12, 3, 7 ]
                                ]
                              ]
                            )
            ]
        , describe "transpose"
            [ test "example board 1" <|
                \_ ->
                    Day04.transpose
                        [ [ 22, 13, 17, 11, 0 ]
                        , [ 8, 2, 23, 4, 24 ]
                        , [ 21, 9, 14, 16, 7 ]
                        , [ 6, 10, 3, 18, 5 ]
                        , [ 1, 12, 20, 15, 19 ]
                        ]
                        |> Expect.equal
                            [ [ 22, 8, 21, 6, 1 ]
                            , [ 13, 2, 9, 10, 12 ]
                            , [ 17, 23, 14, 3, 20 ]
                            , [ 11, 4, 16, 18, 15 ]
                            , [ 0, 24, 7, 5, 19 ]
                            ]
            ]
        , describe "boardLines"
            [ test "example board 1" <|
                \_ ->
                    Day04.boardLines
                        [ [ 22, 13, 17, 11, 0 ]
                        , [ 8, 2, 23, 4, 24 ]
                        , [ 21, 9, 14, 16, 7 ]
                        , [ 6, 10, 3, 18, 5 ]
                        , [ 1, 12, 20, 15, 19 ]
                        ]
                        |> Expect.equal
                            [ [ 22, 13, 17, 11, 0 ]
                            , [ 8, 2, 23, 4, 24 ]
                            , [ 21, 9, 14, 16, 7 ]
                            , [ 6, 10, 3, 18, 5 ]
                            , [ 1, 12, 20, 15, 19 ]
                            , [ 22, 8, 21, 6, 1 ]
                            , [ 13, 2, 9, 10, 12 ]
                            , [ 17, 23, 14, 3, 20 ]
                            , [ 11, 4, 16, 18, 15 ]
                            , [ 0, 24, 7, 5, 19 ]
                            ]
            ]
        , describe "remainingNumbers"
            [ test "example board 1 row 1 at win" <|
                \_ ->
                    Day04.remainingNumbers
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16 ]
                        [ 22, 13, 17, 11, 0 ]
                        |> Expect.equal
                            [ 22, 13 ]
            , test "example board 1 row 3 at win" <|
                \_ ->
                    Day04.remainingNumbers
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16 ]
                        [ 21, 9, 14, 16, 7 ]
                        |> Expect.equal
                            []
            , test "example board 1 column 1 at win" <|
                \_ ->
                    Day04.remainingNumbers
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16 ]
                        [ 22, 8, 21, 6, 1 ]
                        |> Expect.equal
                            [ 22, 8, 6, 1 ]
            ]
        , describe "lastDraw"
            [ test "example board 1 last draw" <|
                \_ ->
                    Day04.lastDraw
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16 ]
                        |> Expect.equal 16
            ]
        , describe "boardScore"
            [ test "example board 3 final score" <|
                \_ ->
                    Day04.boardScore
                        [ [ 14, 21, 17, 24, 4 ]
                        , [ 10, 16, 15, 9, 19 ]
                        , [ 18, 8, 23, 26, 20 ]
                        , [ 22, 11, 13, 6, 5 ]
                        , [ 2, 0, 12, 3, 7 ]
                        ]
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24 ]
                        |> Expect.equal 4512
            ]
        , describe "checkBoard"
            [ test "example board 1 at win" <|
                \_ ->
                    Day04.checkBoard
                        [ [ 22, 13, 17, 11, 0 ]
                        , [ 8, 2, 23, 4, 24 ]
                        , [ 21, 9, 14, 16, 7 ]
                        , [ 6, 10, 3, 18, 5 ]
                        , [ 1, 12, 20, 15, 19 ]
                        ]
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16 ]
                        |> Expect.equal (Just 2192)
            , test "example board 1 at start" <|
                \_ ->
                    Day04.checkBoard
                        [ [ 22, 13, 17, 11, 0 ]
                        , [ 8, 2, 23, 4, 24 ]
                        , [ 21, 9, 14, 16, 7 ]
                        , [ 6, 10, 3, 18, 5 ]
                        , [ 1, 12, 20, 15, 19 ]
                        ]
                        []
                        |> Expect.equal Nothing
            ]
        , describe "predictedWin"
            [ test "example board 1" <|
                \_ ->
                    Day04.predictedWin
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1 ]
                        1
                        [ [ 22, 13, 17, 11, 0 ]
                        , [ 8, 2, 23, 4, 24 ]
                        , [ 21, 9, 14, 16, 7 ]
                        , [ 6, 10, 3, 18, 5 ]
                        , [ 1, 12, 20, 15, 19 ]
                        ]
                        |> Expect.equal { turn = 14, score = 2192 }
            ]
        , describe "getPredictions"
            [ test "example" <|
                \_ ->
                    Day04.getPredictions
                        [ [ [ 22, 13, 17, 11, 0 ]
                          , [ 8, 2, 23, 4, 24 ]
                          , [ 21, 9, 14, 16, 7 ]
                          , [ 6, 10, 3, 18, 5 ]
                          , [ 1, 12, 20, 15, 19 ]
                          ]
                        , [ [ 3, 15, 0, 2, 22 ]
                          , [ 9, 18, 13, 17, 5 ]
                          , [ 19, 8, 7, 25, 23 ]
                          , [ 20, 11, 10, 24, 4 ]
                          , [ 14, 21, 16, 12, 6 ]
                          ]
                        , [ [ 14, 21, 17, 24, 4 ]
                          , [ 10, 16, 15, 9, 19 ]
                          , [ 18, 8, 23, 26, 20 ]
                          , [ 22, 11, 13, 6, 5 ]
                          , [ 2, 0, 12, 3, 7 ]
                          ]
                        ]
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1 ]
                        |> Expect.equal
                            [ { turn = 12, score = 4512 }
                            , { turn = 14, score = 2192 }
                            , { turn = 15, score = 1924 }
                            ]
            ]
        , describe "answerPart1"
            [ test "example" <|
                \_ ->
                    Day04.answerPart1
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1 ]
                        [ [ [ 22, 13, 17, 11, 0 ]
                          , [ 8, 2, 23, 4, 24 ]
                          , [ 21, 9, 14, 16, 7 ]
                          , [ 6, 10, 3, 18, 5 ]
                          , [ 1, 12, 20, 15, 19 ]
                          ]
                        , [ [ 3, 15, 0, 2, 22 ]
                          , [ 9, 18, 13, 17, 5 ]
                          , [ 19, 8, 7, 25, 23 ]
                          , [ 20, 11, 10, 24, 4 ]
                          , [ 14, 21, 16, 12, 6 ]
                          ]
                        , [ [ 14, 21, 17, 24, 4 ]
                          , [ 10, 16, 15, 9, 19 ]
                          , [ 18, 8, 23, 26, 20 ]
                          , [ 22, 11, 13, 6, 5 ]
                          , [ 2, 0, 12, 3, 7 ]
                          ]
                        ]
                        |> Expect.equal "4512"
            ]
        , describe "answerPart2"
            [ test "example" <|
                \_ ->
                    Day04.answerPart2
                        [ 7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1 ]
                        [ [ [ 22, 13, 17, 11, 0 ]
                          , [ 8, 2, 23, 4, 24 ]
                          , [ 21, 9, 14, 16, 7 ]
                          , [ 6, 10, 3, 18, 5 ]
                          , [ 1, 12, 20, 15, 19 ]
                          ]
                        , [ [ 3, 15, 0, 2, 22 ]
                          , [ 9, 18, 13, 17, 5 ]
                          , [ 19, 8, 7, 25, 23 ]
                          , [ 20, 11, 10, 24, 4 ]
                          , [ 14, 21, 16, 12, 6 ]
                          ]
                        , [ [ 14, 21, 17, 24, 4 ]
                          , [ 10, 16, 15, 9, 19 ]
                          , [ 18, 8, 23, 26, 20 ]
                          , [ 22, 11, 13, 6, 5 ]
                          , [ 2, 0, 12, 3, 7 ]
                          ]
                        ]
                        |> Expect.equal "1924"
            ]
        ]
