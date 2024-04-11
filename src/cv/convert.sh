cat cv-header.md cv-body.md > ./cv.md

pandoc -f gfm -t html5 -V margin-top=5 -V margin-left=10 -V margin-right=10 -V margin-bottom=5 -V papersize=A4 --metadata pagetitle="cv.md" --css styles.css  cv.md -o cv.pdf --pdf-engine-opt=--enable-local-file-access
