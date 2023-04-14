from PyPDF2 import PdfReader
import fitz
# import libraries
import fitz
import io
from PIL import Image
import img2pdf
import os


# https://www.thepythoncode.com/article/extract-pdf-images-in-python


def extract_image(pdf_file_obj_path):
    '''
    :param pdf_file:
    :return:
    '''
    import matplotlib.backends.backend_pdf
    import matplotlib.pyplot as plt
    pdf_file = fitz.open(pdf_file_obj_path)
    image_obj_filepath_list = []
    image_obj_list = []
    temp_path = "to_delete/" + pdf_file_obj_path.replace(".pdf", "")

    for page_index in range(len(pdf_file)):

        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        if image_list:
            print(
                f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        '''
        **********************https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/ *********************************
        '''

        # create a temporary directory to store the extracted images
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]

            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]

            # get the image extension
            image_ext = base_image["ext"]
            # Generate image file name


            #image = Image.open(io.BytesIO(image_bytes))   # open images one after another
            #image.show()

            # get the image size
            #imgwidth, imgheight = image.width, image.height
            # save it to local disk
            image_path = f"{temp_path}/image_{page_index + 1}_{image_index}.{image_ext}"
            imgout = open(image_path, "wb")
            imgout.write(image_bytes)

            imgout.close()

            #image.save(open(image_path, "wb"))
            #image_obj_list.append((base_image, image_bytes, image_ext, imgwidth, imgheight))
            image_obj_filepath_list.append(image_path)

        '''
        ************************  END ***************************************
        '''

    '''
    ************** https://dev.to/techlearners/create-a-pdf-from-multiple-images-using-python-1l7o  # https://stackoverflow.com/questions/17788685/python-saving-multiple-figures-into-one-pdf-file   ***************
    '''
    extracted_image_path = f"{temp_path}/extracted_images.pdf"
    print(extracted_image_path)

    if len(image_obj_list) >0:

        #pdf = matplotlib.backends.backend_pdf.PdfPages(extracted_image_path)

        image_list = []
        for img_path in image_obj_filepath_list:  ## will open an empty extra figure :(
            image = Image.open(img_path)
            image.convert('RGB')
            image_list.append(image)




            #pdf.savefig(1)
            # img_obj,img_bytes, img_ext, img_width, img_height
        image1 = image_list[0]
        imageList = image_list[1:]
        image1.save(extracted_image_path, save_all=True, append_images=imageList)

        #plt.close('all')
        #plt.clf()


    '''
    ***************   END   **********************
    '''








    # get the tile of a pdf file