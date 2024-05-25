#!/usr/bin/env python

# A building block!
# This script is made to generate a README.md file, combining
# the contents of the readme directory
# Generate a TOC for the markdown files of src directory.

import os
from natsort import natsorted

def generate_readme():
    # read from readme/head.md
    with open("readme/head.md", "r") as head:
        head_md = head.read()
        with open("README.md", "w") as readme:
            readme.write(head_md)
            readme.write("\n")
    
    # Generate a TOC for the markdown files of src directory
    with open("README.md", "a") as readme:
        readme.write("## Table of Contents\n\n")
        for root, dirs, files in os.walk("src"):
            for file in natsorted(files):
                if file.endswith(".md"):
                    readme.write(f"- [{file[:-3]}]({os.path.join(root, file)})\n")
        readme.write("\n")
    
    # read from readme/foot.md
    with open("readme/foot.md", "r") as foot:
        foot_md = foot.read()
        with open("README.md", "a") as readme:
            readme.write(foot_md)
            readme.write("\n")

if __name__ == "__main__":
    generate_readme()