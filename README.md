# Video-Matrix Arduino R4
This little project is an Arduino sketch designed for the R4 ver. 
featured with a 12*8 LED matrix.

It uses the `Arduino_LED_Matrix.h` and everything is set in the `loop()` function

# Videos
Using the **vid.py** you can generate your own .h file to include in the sketch.

It uses the OpenCV library to fit the video in the matrix.

Because i set the file picker to an specific DIR, it might not work!

### Available vids
* Bad Apple
* Lagtrain

# Short Guide

Open the .ino file with your **Arduino IDE** and upload to your arduino R4

_You might need to install the library mentioned before_

**Bad Apple** is alredy set inside, but if you want to change it, you can
even generate a video by running the python script and pick a video inside your pc. 
But be aware that arduno has not much memory (BadApple takes approx 60%)

If you have generated your own video, you have to change the file in the section

```c
#include "YOURVIDEO.h"
```

