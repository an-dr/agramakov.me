#!/usr/bin/env python3
# *************************************************************************
#
# Copyright (c) 2024 Andrei Gramakov. All rights reserved.
#
# site:    https://agramakov.me
# e-mail:  mail@agramakov.me
#
# *************************************************************************
import os
import subprocess
import pathlib
import distutils.spawn

def get_date_string():
    import datetime
    # dd-mmm-yyyy
    return datetime.datetime.now().strftime("%d-%b-%Y")

def build_md(file_a, file_b, output_file):
    with open(file_a, 'r') as file_a:
        with open(file_b, 'r') as file_b:
            with open(output_file, 'w') as output_file:
                content_a = file_a.read()
                content_b = file_b.read()
                content_out = content_a + content_b
                content_out = content_out.replace("DD-MMM-YYYY", get_date_string())
                output_file.write(content_out)
    return output_file

def convert_md_to_pdf(md_file, pdf_file, css_file, margin_top, margin_bottom, margin_left, margin_right):
    # pandoc process
    ret = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", 
                          "-V", f"margin-top={margin_top}", 
                          "-V", f"margin-left={margin_left}",
                          "-V", f"margin-right={margin_right}",
                          "-V", f"margin-bottom={margin_bottom}",
                          "-V", "papersize=A4", 
                          "--metadata", "pagetitle=cv.md", 
                          "--css", css_file, 
                          md_file, "-o", pdf_file, 
                          "--pdf-engine-opt=--enable-local-file-access"])

def _find_program(name):
    return distutils.spawn.find_executable(name)

def validate_env():
    for p in ["pandoc", "wkhtmltopdf"]:
        if _find_program(p) is None:
            print(f"Could not find {p}")
            return False
    return True

if __name__ == '__main__':
    if not validate_env():
        exit(1)
    current_file_root = pathlib.Path(__file__).parent.absolute()
    
    cv_header = current_file_root / "cv-header.md"
    cv_body = current_file_root / "cv-body.md"
    css = current_file_root / "styles.css"
    
    tmp_md = current_file_root / "cv.md"
    out_pdf = current_file_root / "../../cv/Andrei_Gramakov_CV.pdf"
    
    build_md(cv_header, cv_body, tmp_md)
    convert_md_to_pdf(tmp_md, out_pdf, css, 10, 10, 20, 20)
    
    # remove tmp_md if exists
    if os.path.exists(tmp_md):
        os.remove(tmp_md)

