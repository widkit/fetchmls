import os
import imgkit


os.system('neofetch --stdout > neofetch_output.txt')
neofetch_output = open("neofetch_output.txt", "r")
data = neofetch_output.read()
print(data)
# Reading the file
with open('index.html', 'r') as file:
    filedata = file.read()

    # Doing the replacements of variables
    filedata = filedata.replace('$output', data)

    # Writing changes to new file
with open('render.html', 'w') as file:
    file.write(filedata)
# Using IMGKIT to render the render.html and outputting as result.png
imgkit.from_file('render.html', 'result.png')
os.system('feh result.png')


def remove_junk():
    remove_junk = input('You want to remove junk files? (y/n): ')
    if remove_junk == 'y':
        os.remove("result.png")
        os.remove("render.html")
        os.remove("neofetch_ııoutput.txt")
    elif remove_junk == 'n':
        quit()
    else:
        print('Invalid input. Try again.')
        remove_junk()


remove_junk()
