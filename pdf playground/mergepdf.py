import PyPDF2
import sys 

pdfs = list(sys.argv)[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
        
    merger.write("merge.pdf")

pdf_merger(pdfs)