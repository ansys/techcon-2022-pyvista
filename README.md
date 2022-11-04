## Ansys LaTeX Beamer Slide Template

This is a [LaTeX](https://www.latex-project.org/) [beamer](https://ctan.org/pkg/beamer?lang=en) template you can use to create an Ansys style presentations without the use of PowerPoint. It follows the Ansys template as much as possible including:

- Style
- Font
- Organization
- Theme

Please feel free to point out any problems with this template by opening an [issue](https://github.com/ansys/beamer-template/issues).

### Preview

Visit [sample.pdf](https://ubiquitous-spoon-7c23a783.pages.github.io/sample.pdf) to see the full generated presentation.

[![sample.pdf](figures/title.png)](https://ubiquitous-spoon-7c23a783.pages.github.io/sample.pdf)


### Installation

Due to the usage of ttf fonts, this template requires [LuaTeX](https://www.luatex.org/). Also requires the ``inkscape`` to read svg files.

On Linux (Debian) install with:

```
sudo apt update
sudo apt install -y latexmk texlive-luatex texlive-fonts-extra inkscape
```

On Windows, use a distribution like [MiKTeX](http://miktex.org/). See [Get LaTeX](https://www.latex-project.org/get/).


### Build

Clone this repository with:
```
git clone https://github.com/ansys/beamer-template/
cd beamer-template
```

Build with:

```
latexmk -pdflatex=lualatex -pdf sample.tex -interaction=nonstopmode -outdir=./build
```

Or simply:
```
make
```

This will output `sample.pdf` in the `build` directory. You can feel free to rename the main `sample.tex` file for your own presentation.
