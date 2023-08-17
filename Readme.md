# Park-a-mania

An app created using Python and OpenCV during the FGF brands' first hackathon.

The app works by first providing an image of the desired parking lot and then plotting rectangles to best match the parking spot sizing.

Video will be converted to greyscale and rectangles that have been plotted will have a designated threshold value that if surpassed signal an occupied while values below the threshold indicate an open parking space. 
This is done by treating the pixels within a plotted rectangle as binary with white pixels = 1's while dark pixels = 0's.

There is certainly room for improvement as the plotting of rectangles is currently fixed and rigid. Depending on the angle of the camera's coverage it may be difficult to accurately capture certain parking spaces.
