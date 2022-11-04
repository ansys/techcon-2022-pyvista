BUILD = ./build

build:
	latexmk -pdflatex=lualatex -pdf *.tex -interaction=nonstopmode --shell-escape -outdir=$(BUILD)

clean:
	rm -rf $(BUILD)

.PHONY: build clean

all: build
