module Pages.Day.Id_ exposing (Model, Msg, page)

import Gen.Params.Day.Id_ exposing (Params)
import Html exposing (code, h1, h2, p, pre, text)
import Http
import Page
import Request
import Shared
import Solver exposing (solve)
import View exposing (View)


page : Shared.Model -> Request.With Params -> Page.With Model Msg
page _ req =
    Page.element
        { init = init req.params.id
        , update = update
        , view = view req.params.id
        , subscriptions = \_ -> Sub.none
        }



-- INIT


type Model
    = Failure
    | Loading
    | Success String


init : String -> ( Model, Cmd Msg )
init number =
    ( Loading
    , Http.get
        { url = "http://localhost:8000/" ++ number ++ ".txt"
        , expect = Http.expectString GotText
        }
    )



-- UPDATE


type Msg
    = GotText (Result Http.Error String)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        GotText result ->
            case result of
                Ok fullText ->
                    ( Success fullText, Cmd.none )

                Err _ ->
                    ( Failure, Cmd.none )



-- VIEW


view : String -> Model -> View Msg
view id model =
    case model of
        Failure ->
            { title = "._."
            , body =
                [ p [] [ text "Unable to load the input" ]
                ]
            }

        Loading ->
            { title = "..."
            , body = [ p [] [ text "Loading..." ] ]
            }

        Success input ->
            let
                solution =
                    solve id input
            in
            { title = "AoC 2021"
            , body =
                [ h1 [] [ text ("Day " ++ id) ]
                , h2 [] [ text "Part 1" ]
                , p [] [ text solution.part1 ]
                , h2 [] [ text "Part 2" ]
                , p [] [ text solution.part2 ]
                , h2 [] [ text "Input" ]
                , pre [] [ code [] [ text input ] ]
                ]
            }
