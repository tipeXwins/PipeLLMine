 -for file in BuggyCodes/*.py; do
    diff -u "$file" "CorrectCodes/${file##*/}" > UniDiffs/”${file##*/}”
done

