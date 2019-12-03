from Braille import *

name = input("Enter file name:\n> ") + ".scad"
size = float(input("\nEnter scale factor:\n> "))
print("\nEnter dot lists:")
print("'print' to show current text;")
print("'delete' to backspace;")
print("'export' to end text;\n")

text = BrllText()
strChar = ""
while strChar != "export":
    print("-----\n")
    strChar = input("> ")
    if strChar == "print":
        text.print()
    elif strChar == "delete":
        text.back()
    elif strChar != "export":
        text.add(BrllChar(strChar))


scad_render_to_file(text.solid(size), name)
input("\nSuccessfully exported model to '" + name + "'.\n")
