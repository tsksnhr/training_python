#! python3
# edit filename from us-date to euro-date

# module import
import os
import sys
import re
import shutil

# make directory and change cwd
cd_str = os.getcwd()
dir_str = os.path.join(cd_str, "project9_1")

if os.path.exists(dir_str) == False:
    print("No directory. Please make directory.")
    sys.exit()

os.chdir(dir_str)

# make regular expression
# group is defined by "()"
us_date_regex = re.compile(r"""        # group(0)
    ^(.*?)                              # group(1)
    ((0|1)\d)-                          # group(2) grpuo(3)
    ((0|1|2|3)\d)-                      # group(4) group(5)
    ((19|20)\d\d)                       # group(6) group(7)
    (.*?)$                              # group(8)
    """, re.VERBOSE)

# get filename from cwd
for ext_dir_str in os.listdir():
    mo = us_date_regex.search(ext_dir_str)

    if mo == None:
        continue

    # split match object
    bef_str = mo.group(1)
    month_str = mo.group(2)
    date_str = mo.group(4)
    year_str = mo.group(6)
    aft_str = mo.group(8)

    # make us-date and euro-date strings 
    us_date_str = bef_str + month_str + "-" + date_str + "-" + year_str + aft_str
    euro_date_str = bef_str + date_str + "-" + month_str + "-" + year_str + aft_str

    #print("filename will change from \"{}\" to \"{}\".".format(us_date_str, euro_date_str))
    shutil.move(ext_dir_str, euro_date_str)

# End Of File