# img-to-numworks-color

So, you want to convert an image to send it to your numworks ?

First of all, you need to scale down you image to 160*120 or 320*240 (you may need to lower the amount of colors if you choose the second option), and lower the image's color amount to a maximum of 26

To start converting an image, start by changing the parameters in "parameters.py" (the most important are SRCimage and outputFile)

Then, run the getImage script that converts the image to letters and copy the palette that was printed in the console to the "palette" variable in the decode.py script

Now run the encode script, copy the string in the outputFile and paste it to the compressed_input variable in the decode.py script

Finally, just send the decode.py script to your numworks calculator :)

(There are two versions of the decode.py script : minified decode and minified decode low. The low version is 160*120 and the other is 320*240)
