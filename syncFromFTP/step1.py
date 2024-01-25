from .common import action, delete_file
import time

# function based view to get the file and perform step related actions
def step_actions(input_file_name, output_file_name):
    print("finding the file.")
    time.sleep(1)
    print("file found, now entering step 1 .........")
    time.sleep(1)
    output_file_name = action(input_file_name, output_file_name)
    delete_file(input_file_name)
    print("......... step 1 is over .........")
    return output_file_name