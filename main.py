import os
import os.path
import imgkit


os.system('neofetch --stdout > neofetch_output.txt')
neofetch_output = open("neofetch_output.txt", "r")
data = neofetch_output.read()
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

    if os.path.isfile("./.alwaysremove") == False:
       remove_junk = input('Remove junk files? ((Y)es/(N)o/(A)lways): ')
       if remove_junk == 'y' or 'Y':
           os.remove("result.png")
           os.remove("render.html")
           os.remove("neofetch_output.txt")
       elif remove_junk == 'n' or 'N':
           quit()
       elif remove_junk == 'a' or 'A':
            os.remove("result.png")
            os.remove("render.html")
            os.remove("neofetch_output.txt")
            os.system("touch .alwaysremove")
       else:
           print('Invalid input. Try again.')
           remove_junk()

    elif os.path.isfile("./.alwaysremove") == True:
       os.remove("result.png")
       os.remove("render.html")
       os.remove("neofetch_output.txt")

remove_junk()
