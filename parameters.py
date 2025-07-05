SRCimage : str = "Images/plane.jpg" # // the image you want to convert
outputFile : str = "newFile.txt" # // the file where the encoded image will be written
showResult : bool = True # // if turned on, the getImage script will render the image in a kandinsky window

similarity_threshold = 30 # // Distance threshold to consider two colors "the same"
                          # //-> the higher, the more variety in colors (but some colors may be ignored)
                          # // tip : if color palette is not full, lower the value
                          
colorAmount = 15 # // amount of different colors (max is 26)