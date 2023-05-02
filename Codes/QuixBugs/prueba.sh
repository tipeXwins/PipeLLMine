#!/bin/sh
for file in BuggyCodes/*.py; do
    echo UniDiffs/”${file##*/}”
done

