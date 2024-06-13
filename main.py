"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""


text = "Disneyland Review Analyser"
dashes = "-" *len(text)

print(dashes)
print(text)
print(dashes)
print("\n")



import tui
tui.Disneyland_Review_Analyser()




