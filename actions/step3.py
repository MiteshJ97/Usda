from .common import action, delete_file
import time

# function based view to get the file and perform step related actions
def step_actions(input_file_name, output_file_name):
    print("Entering next step.................. Processed the previous step file, saving the file.")
    time.sleep(1)
    output_file_name = action(input_file_name, output_file_name)
    #delete_file(input_file_name) 
    print("......... step 3 is over .........")

    return output_file_name