+++
title = "vscode"
description = "A text editor."
+++

# VSCODE

A text editor.

## Extensions

### Appearance

- One Dark Pro
- Error Lens

### Git

- GitHub Actions
- GitHub Codespaces
- GitLens
- GitHub Pull Requests
- GitHub Repositories
- Azure Repos

### AI

- Codeium
- GitHub Copilot
- GitHub Copilot Chat

### Containers and remote

- Dev Containers
- Remote Repositories
- WSL
- Docker

### Language Support

- Code spell Checker
- Code Runner
- IntelliCode
- MongoDB for VS Code
- C/C++
- CMake Tools
- LaTeX Workshop
- isort
- Pylance
- PyPI Assistant
- Python
- shell-format
- Tailwind CSS IntelliSense
- SQL Tools
- Jupyter

### Utilites

- Competitive Programming Helper (cph)
- **WakaTime**
- Live Share
- Live Server
- Preetier

## Config File

Sample config file for starters!
(Press F1 and look for `Preferences: Open Settings (JSON)`)

```json
{
    "terminal.integrated.fontFamily": "'FiraCode Nerd Font'",
    "editor.fontFamily": "'FiraCode Nerd Font','Droid Sans Mono', 'monospace', monospace",
    "editor.fontLigatures": true,
    "files.autoSave": "afterDelay",
    "git.confirmSync": false,
    "[python]": {
        "editor.formatOnType": true,
        "editor.defaultFormatter": "ms-python.autopep8"
    },
    "cmake.configureOnOpen": true,
    "git.enableSmartCommit": true,
    "git.autofetch": true,
    "editor.inlineSuggest.enabled": true,
    "github.copilot.enable": {
        "*": true,
        "plaintext": true,
        "markdown": true,
        "scminput": true,
        "cpp": true
    },
    "github.copilot.advanced": {},
    "window.titleBarStyle": "custom",
    "workbench.colorTheme": "One Dark Pro Flat",
    "editor.minimap.renderCharacters": false,
    "window.commandCenter": false,
    "editor.copyWithSyntaxHighlighting": false,
    "workbench.editor.splitInGroupLayout": "vertical",
    "[shellscript]": {
        "editor.defaultFormatter": "foxundermoon.shell-format"
    },
    "cSpell.language": "en,lorem",
    "cSpell.enabled": false,
    "githubPullRequests.pullBranch": "never",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.variableTypes": true,
    "[java]": {
        "editor.suggest.snippetsPreventQuickSuggestions": false
    },
    "cmake.showOptionsMovedNotification": false,
    "git.openRepositoryInParentFolders": "always",
    "editor.fontSize": 17,
    "debug.console.fontSize": 16,
    "scm.inputFontSize": 15,
    "terminal.integrated.fontSize": 16,
    "chat.editor.fontSize": 16,
    "markdown.preview.fontSize": 16,
    "[markdown]": {
        "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
    },
    "[cpp]": {
        "editor.defaultFormatter": "ms-vscode.cpptools"
    },
    "[javascript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "security.workspace.trust.untrustedFiles": "open",
    "[c]": {
        "editor.defaultFormatter": "ms-vscode.cpptools"
    },
    "latex-workshop.latex.recipe.default": "latexmk (xelatex)",
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "lualatexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-lualatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "xelatexmk",
            "command": "latexmk",
            "args": [
                "-shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-xelatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "latexmk_rconly",
            "command": "latexmk",
            "args": [
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ],
            "env": {}
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ],
            "env": {}
        },
        {
            "name": "rnw2tex",
            "command": "Rscript",
            "args": [
                "-e",
                "knitr::opts_knit$set(concordance = TRUE); knitr::knit('%DOCFILE_EXT%')"
            ],
            "env": {}
        },
        {
            "name": "jnw2tex",
            "command": "julia",
            "args": [
                "-e",
                "using Weave; weave(\"%DOC_EXT%\", doctype=\"tex\")"
            ],
            "env": {}
        },
        {
            "name": "jnw2texminted",
            "command": "julia",
            "args": [
                "-e",
                "using Weave; weave(\"%DOC_EXT%\", doctype=\"texminted\")"
            ],
            "env": {}
        },
        {
            "name": "pnw2tex",
            "command": "pweave",
            "args": [
                "-f",
                "tex",
                "%DOC_EXT%"
            ],
            "env": {}
        },
        {
            "name": "pnw2texminted",
            "command": "pweave",
            "args": [
                "-f",
                "texminted",
                "%DOC_EXT%"
            ],
            "env": {}
        },
        {
            "name": "tectonic",
            "command": "tectonic",
            "args": [
                "--synctex",
                "--keep-logs",
                "%DOC%.tex"
            ],
            "env": {}
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk",
            "tools": [
                "latexmk"
            ]
        },
        {
            "name": "latexmk (latexmkrc)",
            "tools": [
                "latexmk_rconly"
            ]
        },
        {
            "name": "latexmk (lualatex)",
            "tools": [
                "lualatexmk"
            ]
        },
        {
            "name": "latexmk (xelatex)",
            "tools": [
                "xelatexmk"
            ]
        },
        {
            "name": "pdflatex -> bibtex -> pdflatex * 2",
            "tools": [
                "pdflatex",
                "bibtex",
                "pdflatex",
                "pdflatex"
            ]
        },
        {
            "name": "Compile Rnw files",
            "tools": [
                "rnw2tex",
                "latexmk"
            ]
        },
        {
            "name": "Compile Jnw files",
            "tools": [
                "jnw2tex",
                "latexmk"
            ]
        },
        {
            "name": "Compile Pnw files",
            "tools": [
                "pnw2tex",
                "latexmk"
            ]
        },
        {
            "name": "tectonic",
            "tools": [
                "tectonic"
            ]
        }
    ],
    "[latex]": {
        "editor.defaultFormatter": "James-Yu.latex-workshop"
    },
    "github.copilot.editor.enableAutoCompletions": true,
    "workbench.sideBar.location": "right",
    "redhat.telemetry.enabled": true
}
```

