import sys
sys.path.append("..")
sys.path.append(".")
from Make_Assignment import main
from tud_tests import *

def test_cylinder_volume_output():
    set_keyboard_input(["5", "10"])  # Radius = 5, Length = 10
    main()
    output = get_display_output()

    # Verify the output
    assert output[0].lower() == "enter the radius of the base: "
    assert output[1].lower() == "enter the length of the cylinder: "
    assert output[2] == "The volume of the cylinder is: 785.40"