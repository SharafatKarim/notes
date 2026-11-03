---
title: Match (switch case)
tags:
- python
- tech
aliases:
- Match (switch case)
---

```Python
choice: str = input("what is your favorite color: ").lower()

match choice:
    case "black":
        print("you are adventurous")
    case "pink":
        print("you are girlish")
    case _:
        print(f"you are like {choice}")
```

requires python 3.10+

---

**copyright**

bles to work with the interpreter
