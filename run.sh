#!/bin/bash

clear

echo "Make a selection: "
options=("Do I need to defrost my windscreen?" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Do I need to defrost my windscreen?")
            python3 /Users/"$(whoami)"/Weather-Tidbits/windscreen.py
            break
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done