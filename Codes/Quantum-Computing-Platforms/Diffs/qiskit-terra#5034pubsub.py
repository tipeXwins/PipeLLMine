55c55
<                        id(self.callback) == id(other.callback)  # Allow 1:N subscribers
---
>                        self.callback.__name__ == other.callback.__name__
