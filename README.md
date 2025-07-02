# img-to-numworks-color

So, you want to convert an image to send it to your numworks ?

First of all, you need to scale down you image to 160*120 (otherwise it will be to large), and change the amount of color to 26 or less

To start converting an image, start by changing the parameters in "parameters.py" (the most important are SRCimage and outputFile)

Then, run the getImage script that converts the image to letters

All you have to do now is to copy the palette that was printed in the console to the "palette" variable in the decode.py and copy the "outputfile"'s content and paste it to the "compressed_input" variable,now just send it to your numworks calculator :)
