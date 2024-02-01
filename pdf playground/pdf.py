import PyPDF2 

with open("dummy.pdf" ,"rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open("idk.pdf" , "wb") as file2:
        writer.write(file2)
