#!/bin/sh

player_status=$(playerctl status)
if [ "$player_status" = "Playing" ]; then
    echo "$(playerctl metadata artist) - $(playerctl metadata title)"
else
    echo "Let's dance!" 
fi
