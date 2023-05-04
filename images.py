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
    temp_path = "to_delete/" + pdf_file_obj_path.replace(".pdf", "")

    os.system("java -jar pdffigures/pdffigures2-assembly-0.1.0.jar -m "+temp_path+"/  "+pdf_file_obj_path)
    #pdf_file = fitz.open(pdf_file_obj_path)
    image_obj_filepath_list = []
    image_obj_list = []
    for file in os.listdir(temp_path):
        image_obj_filepath_list.append(temp_path+"/"+file)

    '''
    ************** https://dev.to/techlearners/create-a-pdf-from-multiple-images-using-python-1l7o  # https://stackoverflow.com/questions/17788685/python-saving-multiple-figures-into-one-pdf-file   ***************
    '''
    extracted_image_path = f"{temp_path}/extracted_images.pdf"
    print(extracted_image_path)

    if len(image_obj_filepath_list) >0:

        #pdf = matplotlib.backends.backend_pdf.PdfPages(extracted_image_path)

        image_list = []
        for img_path in image_obj_filepath_list:  ## will open an empty extra figure :(
            if ".png" in img_path:
                image = Image.open(img_path)
                image.convert('RGB')
                image_list.append(image)




            #pdf.savefig(1)
            # img_obj,img_bytes, img_ext, img_width, img_height
        if len(image_list)==0:
            return 0
        image1 = image_list[0]
        imageList = image_list[1:]
        image1.save(extracted_image_path, save_all=True, append_images=imageList)

        #plt.close('all')
        #plt.clf()


    '''
    ***************   END   **********************
    '''








    # get the tile of a pdf file