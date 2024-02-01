# import PyPDF2


# with open("./merge.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     writer = PyPDF2.PdfWriter()

#     with open("./wtr.pdf", "rb") as wtr_file:
#         reader_watermark = PyPDF2.PdfReader(wtr_file)
#         watermark_page = reader_watermark.pages[0]
#         for page_number in range(len(reader.pages)):
#             print(page_number)
#             page = reader.pages[page_number]
#             page.merge_page(watermark_page)
#             writer.add_page(page)

#     with open("./merge_wtr.pdf", "wb") as output_file:
#         writer.write(output_file)




import PyPDF2

with open("merge.pdf" , "rb") as file:
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()

    with open("./wtr.pdf" ,"rb") as wtr_file:
        watermark_reader = PyPDF2.PdfReader(wtr_file)
        watermark_page = watermark_reader.pages[0]

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.merge_page(watermark_page)
            writer.add_page(page)

    with open("merge_wtr.pdf" , "wb") as output_file:
        writer.write(output_file)