---
title: making it faster
tags:
- python
- tech
aliases:
- making it faster
---

```Python
from numba import njit


@njit
def counter(n):
    print(n)
    while n != 10000000000:
        n += 1
    return n


print(counter(0))
```
