# Bash script to be used on Apple's Shortcut App to make display rotation easier.

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

DISPLAY_ID="12AF78F9-CA2A-4B64-B483-62B0736A9568"

CURRENT_ANGLE=$(displayplacer list | grep -A 10 "Persistent screen id" | grep -o 'Rotation: [0-9]*' | tail -n 1 | cut -d ':' -f 2)

if [ -z "$CURRENT_ANGLE" ]; then
    CURRENT_ANGLE=0
fi

if [ "$CURRENT_ANGLE" -eq "0" ]; then
    displayplacer "id:12AF78F9-CA2A-4B64-B483-62B0736A9568 res:1000x1600 hz:60 color_depth:7 enabled:true scaling:off origin:(-1000,-644) degree:90"
else
    displayplacer "id:12AF78F9-CA2A-4B64-B483-62B0736A9568 res:1600x1000 hz:60 color_depth:7 enabled:true scaling:off origin:(-1600,0) degree:0"
fi