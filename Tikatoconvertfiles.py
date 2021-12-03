# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:56:04 2021

@author: Viny Vyas
"""
import tika
tika.initVM()
from tika import parser  
  
# opening pdf file
parsed_pdf = parser.from_file(r"C:/Users/Viny Vyas/Downloads/DS/0.pdf")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 
  
# Printing of content 
file1=open(r"C:/Users/Viny Vyas/OneDrive/Documents\\0.txt","a")
file1.writelines(data)   