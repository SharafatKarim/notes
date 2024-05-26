#!/usr/bin/env python

# A building block!
# This script is made to copy markdown files
# prepand a header like,
# +++
# title = "Hello Friend"
# date = 2021-02-01
# +++
# and paste them to the content directory.

import os

def generate_posts():
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as src:
                    src_md = src.read()
                    if not os.path.exists("content"):
                        os.makedirs("content")
                    with open(f"content/{file}", "w") as post:
                        post.write("+++\n")
                        post.write(f"title = \"{file[:-3]}\"\n")
                        post.write("+++\n")
                        post.write("\n")
                        post.write(src_md)
                        post.write("\n")

if __name__ == "__main__":
    generate_posts()