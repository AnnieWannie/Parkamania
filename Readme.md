# Park-a-mania

An app created using Python and OpenCV during the FGF brands' first hackathon.

The app works by first providing an image of the desired parking lot and then plotting squares to best match the parking spots sizing.

Behind the scenes video will be converted to greyscale and and squares that have been plotted will have a threshold value that if surpassed signal an occupied or open parking space. This is done by essentially treating the image as binary with white pixels = 1's while dark pixels = 0's.

There is certainly room for improvement as the plotting of squares is essentially fixed and rigid which means depending on the angle of the camera its coverage it may become inaccurate.
