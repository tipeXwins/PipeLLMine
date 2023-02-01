86,89c86
<         if self.id == -1:
<             return self is other
<         return (isinstance(other, BasicQubit) and
<                 self.id == other.id and
---
>         return (isinstance(other, self.__class__) and self.id == other.id and
102,104c99
<         if self.id == -1:
<             return object.__hash__(self)
<         return hash((self.engine, self.id))
---
>         return hash((self.id, self.engine, object.__hash__(self)))
