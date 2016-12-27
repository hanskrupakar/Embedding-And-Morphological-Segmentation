#!/bin/bash
if [ $2 != "" ]; then
    (cat $1 | tr -s [:space:] '\n' | grep -v "^\s*$" | sort | uniq -c | sort -bnr) > $2
else
    echo "USAGE: ./word_occurrence_count srcfile wcfile"
fi

