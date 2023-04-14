import math
import os
 
# assign directory
directory = '.'

# find
from PyPDF2 import PdfReader
# pip install PyMuPDF
import fitz
# import libraries
import fitz
import io
from PIL import Image


def some_magic(pdf_file_path):
    '''

    @param pdf_file_path:
    @return:
    '''
    import images
    for i in dir(images):
        item = getattr(images, i)
        if callable(item):
            item(pdf_file_path)

os.system(f"mkdir to_delete")

for filepath_obj in os.scandir(directory):
    if filepath_obj.is_file() and ".pdf" in filepath_obj.path:
        print(filepath_obj.path)
        try:
            doc = PdfReader(open(filepath_obj.path, "rb"))
        except:
            print(filepath_obj.path +" is not a readable pdf file")
            continue
    else:
        continue
    import re
    #if  len(re.findall(".pdf", filepath_obj.path))>1:
    #    continue
    doc = fitz.open(filepath_obj.path)
    #if doc.metadata["producer"]== "paper_sorter":


    #    continue
    doc.close()
    '''
    **************************  https://stackoverflow.com/a/34431716/5550255   ********************
    '''
    # capture the output of pdftitle to get the article title

    import subprocess
    try:
        captured_title = (subprocess.check_output(f"pdftitle -p '{filepath_obj.path}' -a max2    --replace-missing-char=# ",shell=True))   # the original pdf would be replaced with the one with new name
    except subprocess.CalledProcessError as err:
        print(err)
        try:
            captured_title = (
                subprocess.check_output(f"pdftitle -p '{filepath_obj.path}' -a eliot    --eliot-tfs=0 --replace-missing-char=# ",
                                    shell=True))  # the original pdf would be replaced with the one with new name

        except subprocess.CalledProcessError as err:
            print(err)
            continue
    # Path
    import os

    captured_title = captured_title.decode()
    captured_title = captured_title.strip()
    if len(captured_title)<=5:
        continue
    # to remedy problem of "OSError File name too long", handle here rather than using pdftitle
    import string

    new_name = captured_title.lower()  # Lower case name
    valid_chars = set(string.ascii_lowercase + string.digits + " ")
    new_name = "".join(c for c in new_name if c in valid_chars)
    # split by space
    words = str(new_name).split(" ")
    # captitalized
    words_cap = [word.capitalize() for word in words]
    words_bound = " ".join(words_cap)
    '''
    ***********   https://askubuntu.com/questions/166764/how-long-can-file-names-be   ************
    '''

    words_bound = words_bound[:245]
    title_with_space = words_bound

    '''
    **********    END    *******************8
    '''
    title_without_space = words_bound.replace(' ', '_')
    new_name_pdf = title_without_space + ".pdf"

    os.rename(filepath_obj.path, new_name_pdf)
    filepath_obj_path  = os.path.join(os.getcwd(), new_name_pdf)

    print(new_name)



    #captured_title = str(captured_title).strip().replace(".pdf","").replace("b'","").replace("\\n","").replace('\'',"")


    '''
    ************************    END    ***********************************************************
    '''
    temp_path = "to_delete/"+title_without_space
    os.system(f"mkdir {temp_path}")


    '''
    *************************   https://stackoverflow.com/a/65946983/5550255     ****************************
     write the tile into a blank pdf page     
    '''
    import fitz

    # path = "PyMuPDF_test.pdf"

    pdf3 = filepath_obj_path
    pdf3_obj = fitz.open(pdf3)
    old_first_page = pdf3_obj[0]

    '''
    ***********   https://stackoverflow.com/a/64790804/5550255    ****************
    '''
    doc = fitz.open()

    page = doc.new_page(width=old_first_page.rect.width, height=old_first_page.rect.height)

    #where = fitz.Point(50, 50)
    #page.insert_text(where, captured_title_normal, fontsize=20)
    fontname_to_use = "Times-Roman"
    fontsize_to_use = 20

    text_lenght = fitz.get_text_length(title_with_space,
                                     fontname=fontname_to_use,
                                     fontsize=fontsize_to_use)

    rect_x1 = 50
    rect_y1 = 100
    rect_x2 = rect_x1 + text_lenght + 2  # needs margin
    rect_x2 = rect_x2 if rect_x2<=(old_first_page.rect.width -50) else  old_first_page.rect.width -50
    rect_y2 = rect_y1 + fontsize_to_use*math.ceil(text_lenght/(rect_x2-rect_x1))*2 + 2  # needs margin

    rect = (rect_x1, rect_y1, rect_x2, rect_y2)

    # Uncomment if you wish to display rect
    page.draw_rect(rect,color=(.25,1,0.25))

    rc = page.insert_textbox(rect, title_with_space,
                            fontsize=fontsize_to_use,
                            fontname=fontname_to_use,
                            align=0)
    '''
    ***************** END ******************
    '''
    print(doc.metadata)

    import copy
    metadata = doc.metadata
    metadata["producer"] = "paper_sorter"
    doc.set_metadata(metadata)  # clear all fields
    print(doc.metadata)
    doc.write() #?
    os.system(f"mkdir {temp_path}")
    pdf1 = f"{temp_path}/_only_title.pdf"
    doc.save(pdf1)
    doc.close()






    pages = []
    pages.append(pdf1)
    '''
    ************************     END *******************
    '''
    from images import *
    extract_image(new_name_pdf)

    #some_magic(captured_title)
    pdf2 = f"{temp_path}/extracted_images.pdf" # derived file from some_magic

    if os.path.exists(pdf2):
        open(pdf2)
        pages.append(pdf2)

    pages.append(pdf3)


    '''
    **************************   https://stackabuse.com/working-with-pdfs-in-python-inserting-deleting-and-reordering-pages/ *******************
    '''

    import fitz




    original_pdf = fitz.open(pdf1)
    if os.path.exists(pdf2):
        extra_page_1 = fitz.open(pdf2)
        original_pdf.insert_pdf(extra_page_1)

    extra_page_2 = fitz.open(pdf3)
    original_pdf.insert_pdf(extra_page_2)

    original_pdf.save(filepath_obj_path)

    '''
    ************************************   END  ********************
    '''

