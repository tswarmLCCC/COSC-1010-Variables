# DO NOT MODIFY THE CODE IN THIS FILE
# This file is used to test the implementation of the cylinder volume program
# Test for File Existence

import sys
import os.path

def test_cylinder_volume_file_exists():
    try:
        exists = os.path.exists("../Make_Assignment.py")
        assert exists == True
    except:
        sys.exit()