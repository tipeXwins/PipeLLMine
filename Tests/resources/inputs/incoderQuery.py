<| file ext=.py |>
def bitcount(n):
    count = 0
    while n:
        <|mask:2|>
        <|mask:1|>
        <|endofmask|>
        count += 1
    return count
<|endoftext|>
