module Pages.Home_ exposing (view)

import Html exposing (..)
import Html.Attributes exposing (..)
import View exposing (View)


view : View msg
view =
    { title = "Advent of Code 2021"
    , body =
        [ h1 [] [ Html.text "Advent of Code 2021" ]
        , day "01"
        , day "02"
        , day "03"
        , day "04"
        , day "05"
        , day "06"
        , day "07"
        , day "08"
        , day "09"
        , day "10"
        , day "11"
        , day "12"
        , day "13"
        , day "14"
        , day "15"
        , day "16"
        , day "17"
        , day "18"
        , day "19"
        , day "20"
        , day "21"
        , day "22"
        , day "23"
        , day "24"
        , day "25"
        ]
    }


day : String -> Html msg
day number =
    p []
        [ a [ href ("/day/" ++ number) ] [ text ("Day " ++ number) ]
        ]
