# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 17:13:06 2021

@author: Viny Vyas
"""

import PyPDF2
pdf = PyPDF2.PdfFileReader(open('C:/Users/Viny Vyas/Downloads/DS/0.pdf', "rb"))
for page in pdf.pages:
    text=(page.extractText())
    file1=open(r"C:/Users/Viny Vyas/OneDrive/Documents\\1.txt","a")
    file1.writelines(text)    