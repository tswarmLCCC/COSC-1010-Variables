import sys
sys.path.append("..")
sys.path.append(".")
from Make_Assignment import main
from tud_tests import *

def test_large_values():
    set_keyboard_input(["100", "200"])  # Radius = 100, Length = 200
    main()
    output = get_display_output()

    # Verify the output
    assert output[0].lower() == "enter the radius of the base: "
    assert output[1].lower() == "enter the length of the cylinder: "
    assert output[2] == "The volume of the cylinder is: 6283200.00"