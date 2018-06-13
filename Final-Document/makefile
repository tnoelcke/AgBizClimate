filename=Final-Document

all: $(filename).pdf

.PHONY: clean

$(filename).pdf: *.tex *.bib
		pdflatex -shell-escape $(filename).tex
		pdflatex -shell-escape $(filename).tex
		makeindex $(filename)
		bibtex $(filename)
		pdflatex -shell-escape $(filename).tex
		pdflatex -shell-escape $(filename).tex


clean:
	rm -f ${filename}.{ps,log,aux,out,dvi,bbl,blg,toc, lof}
