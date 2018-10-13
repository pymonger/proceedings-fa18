FILENAME=vonLaszewski-proceedings-fa18
INDEX=all.md
IMAGE_DIRS=$(shell ../book/bin/find-image-dirs.py)

DIRS_523=fa18-523-51 fa18-523-52 fa18-523-53 fa18-523-54 fa18-523-56 fa18-523-57 fa18-523-58 fa18-523-59 fa18-523-60 fa18-523-61 fa18-523-62 fa18-523-63 fa18-523-64 fa18-523-65 fa18-523-66 fa18-523-67 fa18-523-69 fa18-523-71 fa18-523-72 fa18-523-79 fa18-523-68 fa18-523-70 fa18-523-80 fa18-523-81 fa18-523-82 fa18-523-83 fa18-523-84 fa18-523-85 fa18-523-86 fa18-523-73 fa18-523-74 fa18-423-01 fa18-423-02 fa18-423-03 fa18-423-04 fa18-423-05 fa18-423-06 fa18-423-08

DIRS_516=fa18-516-26 fa18-516-02 fa18-516-03 fa18-516-11 fa18-516-04 fa18-516-06 fa18-516-08 fa18-516-10 fa18-516-12 fa18-516-14 fa18-516-17 fa18-516-18 fa18-516-19 fa18-516-21 fa18-516-22 fa18-516-29 fa18-516-31  fa18-516-24 

BROKEN=fal18-516-23 fal18-516-25

DIRS=$(DIRS_516) $(DIRS_523) 

.PHONY: $(DIRS) all bib dest
all: $(DIRS)

PROJECT_VOL10: 

PAPER_VOL10: fa18-516-04/section/vs-code.md

$(DIRS):
	[ -e $@ ] ||	git clone git@github.com:cloudmesh-community/$@.git 
	cd $@; git pull



list:
	python list.py  > list.md

MARKDOWN-OPTIONS=--verbose $(MERMAID) --filter pandoc-fignos -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
FORMAT=--toc --number-sections
BIB=--bibliography all.bib
FONTS=--epub-embed-font='fonts/*.ttf'
RESOURCE=--resource-path=$(IMAGE_DIRS)

projects: bib
	mkdir -p dest
	echo > dest/projects.md
	cat project-report/report.md >> dest/projects.md
	for i in $(DIRS); do \
		cat $$i/project-paper/report.md >> dest/projects.md ; \
		cat $$i/project-report/report.md >> dest/projects.md ; \
		echo "\n" >> dest/projects.md ; \
	done ;
	cd dest; iconv -t utf-8 projects.md > all.md
	cp -r template dest
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub ../metadata.txt all.md
	cp dest/$(FILENAME).epub . 
#	cd dest; pandoc $(RESOURCE) --number-sections -V secnumdepth:5 --pdf-engine=xelatex -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' --template=../template/eisvogel/eisvogel.latex --listings --bibliography all.bib -o $(FILENAME).pdf metadata.txt $(INDEX)

push:
	-for i in $(DIRS); do \
		echo $$i ;\
		cd $$i ; git push; cd ..; \
	done ;


bib:
	mkdir -p bib
	cp project-report/*.bib bib
	-for i in $(DIRS); do \
		cp $$i/paper/references.bib bib/refernces-$$i.bib ; \
		cp $$i/project-paper/report.bib bib/report-$$i.bib ; \
	done ;
	mkdir -p dest
	cat bib/*.bib > dest/all.bib




#cp $($$i)/papers/refernces.bib 	cp refernces-$$(i).bib ; \
#	done ;

clean:
	rm -rf fa18*
