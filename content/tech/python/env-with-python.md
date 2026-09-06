---
title: env with python
tags:
- python
- tech
aliases:
- env with python
---

create ‘.env’ and ‘.env.sample’ and let’s track ‘.env’ with ‘.gitignore’

example, `.env.sample`

```JavaScript
API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BOT_API="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

main code implementation,

```JavaScript
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BOT_API = os.getenv("BOT_API")
```
