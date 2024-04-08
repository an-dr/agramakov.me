cat cv-header.md cv-body.md > ./cv.md

pandoc -f gfm -t html5 -V margin-top=3 -V margin-left=3 -V margin-right=3 -V margin-bottom=3 -V papersize=A4 --metadata pagetitle="cv.md" --css styles.css  cv.md -o cv.pdf --pdf-engine-opt=--enable-local-file-access
