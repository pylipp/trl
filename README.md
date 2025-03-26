# trl

A dumb trello cli with shortcuts.

This is a **fork** with features such as
- `bm` command: show board members

and fixes such as
- handle labels without color


## Setup

```sh
git clone https://github.com/pylipp/pytrl
cd pytrl
python -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
python trullo.py
```
Authenticate yourself by putting these variables in you environment:

    export TRELLO_API_KEY=<api_key>
    export TRELLO_TOKEN=<your_token>

Go get them on [trello](https://trello.com/app-key)!

## Usage

As for now you can do basic stuff.

Here is the usage (check `trl -h` too):

    trl b [<board_shortcut>]
        shows the boards you can access
        with board_shortcut you can select the board you want to work with

    trl l [<list_shortcut> [<list_shortcut>]]
        shows lists and cards in the board you have currently selected
        with list_shortcut you can show cards of a single list

    trl ll
        shows only the board's lists

    trl lb
        shows the board's labels

    trl bm
        shows the board's members

    trl c <card_shortcut> [o | m <list_shortcut> | e]
        shows the card infos
        with o it opens the card shortUrl with your default browser
        with m and a target list you can move the card to that list
        with e you can edit the card title and description in your $EDITOR

    trl c n <list_shortcut>
        pops your $EDITOR to create a new card in the list specified by list_shortcut

    trl g <api_path>
        make a direct api call adding auth params automatically (for debugging/hacking purpose)
        Cf. [REST API reference](https://developer.atlassian.com/cloud/trello/rest)

## Shortcuts

Shortcuts are derived from boards and cards names and short urls
and from lists names and ids (lists does not have short urls).

So to move the card *Architecture design* to the list *Done*
you get something like this:

    trl c arch m done

Everything is kept lowercase, holding shift is a pain in the ass.


## Notes

I know, It's nothing fancy, I just started because I have to use Trello
and I wanted to check some stuff directly from the terminal, and eventually
edit them or open them in the browser.

