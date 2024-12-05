# DO NOT MODIFY THE CODE IN THIS FILE
# This file is used to test the implementation of the cylinder volume program
# Test for Zero Length Input

import sys
sys.path.append("..")
sys.path.append(".")
from Make_Assignment import main
from tud_tests import *

def test_zero_length():
    set_keyboard_input(["5", "0"])  # Radius = 5, Length = 0
    main()
    output = get_display_output()

    # Verify the output
    assert output[0].lower() == "enter the radius of the base: "
    assert output[1].lower() == "enter the length of the cylinder: "
    assert output[2] == "The volume of the cylinder is: 0.00"