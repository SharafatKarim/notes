+++
title = "latex"
+++

# LaTeX

## LaTeX Installation

For ArchLinux, I just follow [Arch Wiki](https://wiki.archlinux.org/title/TeX_Live).
In vscode, it should work out of the box with, LaTeX Workshop extension. But formatting may not work properly. Try to trigger `latexindent` manually to resolve it.

### VSCODE

Here's my vscode config for now for latex,

```json
{
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
    }
}
```

## LaTeX Template

### First one with a bit of article style

```latex
\documentclass{article}

\usepackage{amsmath, amsthm, amssymb, amsfonts}
\usepackage{thmtools}
\usepackage{graphicx}
\usepackage{setspace}
\usepackage{geometry}
\usepackage{float}
\usepackage{hyperref}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{framed}
\usepackage[dvipsnames]{xcolor}
\usepackage{tcolorbox}
\usepackage{minted}

% ------------------------------------------------------------------------------
% \usepackage{times}
\usepackage{fontspec}
\setmainfont{Ubuntu Nerd Font}
\setsansfont{Noto Sans}
\setmonofont{FiraCode Nerd Font}
% ------------------------------------------------------------------------------

\colorlet{LightGray}{White!90!Periwinkle}
\colorlet{LightOrange}{Orange!15}
\colorlet{LightGreen}{Green!15}

\newcommand{\HRule}[1]{\rule{\linewidth}{#1}}

\declaretheoremstyle[name=Theorem,]{thmsty}
\declaretheorem[style=thmsty,numberwithin=section]{theorem}
\tcolorboxenvironment{theorem}{colback=LightGray}

\declaretheoremstyle[name=Proposition,]{prosty}
\declaretheorem[style=prosty,numberlike=theorem]{proposition}
\tcolorboxenvironment{proposition}{colback=LightOrange}

\declaretheoremstyle[name=Principle,]{prcpsty}
\declaretheorem[style=prcpsty,numberlike=theorem]{principle}
\tcolorboxenvironment{principle}{colback=LightGreen}

\setstretch{1.2}
\geometry{
    textheight=9in,
    textwidth=5.5in,
    top=1in,
    headheight=12pt,
    headsep=25pt,
    footskip=30pt
}

% ------------------------------------------------------------------------------

\begin{document}

% ------------------------------------------------------------------------------
% Cover Page and ToC
% ------------------------------------------------------------------------------

\title{ \normalsize \textsc{}
  \\ [2.0cm]
  \HRule{1.5pt} \\
  \LARGE \textbf{\uppercase{Template Title 2}
  \HRule{2.0pt} \\ [0.6cm] \LARGE{Subtitle} \vspace*{10\baselineskip}}
  }
\date{}
\author{\textbf{Author} \\ 
  Who? \\
  Where? \\
  When?}

\maketitle
\newpage

\tableofcontents
\newpage

% ------------------------------------------------------------------------------

\section{Examples}

\begin{theorem}
    This is a theorem.
\end{theorem}

\begin{proposition}
    This is a proposition.
\end{proposition}

\begin{principle}
    This is a principle.
\end{principle}

% Maybe I need to add one more part: Examples.
% Set style and colour later.

\subsection{Pictures}

% \begin{figure}[htbp]
%     \center
%     \includegraphics[scale=0.06]{img/photo.jpg}
%     \caption{Sydney, NSW}
% \end{figure}

\subsection{Citation}

\begin{minted}[frame=lines, fontsize=\footnotesize]{python}
    def hello_world():
        print("Hello, World!") # This is a comment
    
    hello_world()
    \end{minted}

\newpage

% ------------------------------------------------------------------------------
% Reference and Cited Works
% ------------------------------------------------------------------------------

\bibliographystyle{IEEEtran}
\bibliography{References.bib}

% ------------------------------------------------------------------------------

\end{document}
```

And here's one of my latex project for reference, [latex-projects](https://github.com/SharafatKarim/pstu-cse-academic/blob/main/semester%203/cce/networking%20exercises/ch%208/cce_ch8.tex).

