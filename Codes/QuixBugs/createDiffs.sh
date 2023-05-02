 -for file in BuggyCodes/*.py; do
    diff "$file" "CorrectCodes/${file##*/}" > UniDiffs/”${file##*/}”
done

