#! python3
# make zip file with serial number

# module import 
import os
import sys
import zipfile

# define function
# argument is a path of directory or file you want to archive
def make_zip(str_folder):

    # get abspath
    str_abs_path = os.path.abspath(str_folder)

    # define zip-file's name
    int_num = 1
    while True:
        str_zip_name = os.path.basename(str_abs_path) + "_" + str(int_num) + ".zip"

        # search name
        if os.path.exists(str_zip_name) == False:
            break
        else:
            int_num += 1

    # make zip object
    zipobj_backup = zipfile.ZipFile(str_zip_name, "w")

    # walk directories and make zip-files
    for str_foldername, dummy, lst_filenames in os.walk(str_folder):

        # make zip-file of directory
        print("making zip-file of files in {}".format(str_foldername))
        zipobj_backup.write(str_foldername)

        for str_filename in lst_filenames:

            # make new path(basename)
            str_new_basename_path = os.path.basename(str_abs_path) + "_"

            # skip zip file which already achived
            if str_filename.startswith(str_new_basename_path) == True and str_filename.endswith(".zip"):
                continue
            else:
                print("making zip-file of files in {}".format(str_filename))
                str_file_path_to_zip = os.path.join(str_foldername, str_filename)
                zipobj_backup.write(str_file_path_to_zip)

    zipobj_backup.close()
    print("Finished.")
    return

# test fnction
str_cwd = os.getcwd()
str_file_path = os.path.join(str_cwd, "project9_2")

# why outputs are different following two process
# make_zip(str_file_path)
make_zip("project9_2")

# End Of File