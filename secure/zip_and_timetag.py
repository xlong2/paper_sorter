import os
def return_non_python_files(filename_obj):
    if filename_obj.is_file():
        print(filename_obj.path)

        if not os.path.splitext(filename_obj.path)[-1] == ".py":
            return filename_obj




def zip_and_timetag(directory_path):
    files = [return_non_python_files(filename_obj) for filename_obj in os.scandir(directory_path) if return_non_python_files(filename_obj) is not None]

    write_to_file(files, file_list_record_txt)
    # get time tag
    import datetime
    now = datetime.datetime.now()

    # zip all files and time tag it
    os.system("zip {} -@ < {}".format("archive_"+now.isoformat("_")+".zip",file_list_record_txt) )



