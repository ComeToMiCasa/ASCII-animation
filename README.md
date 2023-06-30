# ASCII-animation
ASCII-animation is a convenient command line video-to-ascii converter. It slices the video into frames, converts each into ascii art and saves them into `ascii/\<output-path-name\>`.
Supports background removal, resize, frame rate adjustment.

![ezgif-2-9203c1ccf4](https://github.com/ComeToMiCasa/ASCII-animation/assets/89723696/11fa7077-4dfd-4f00-9c91-7f6b15ea92c9)

Command Line Arguments
--
### Required Arguments
|Parameter|Description|
|------|---|
|path_in|path to the desired video file(string)|
|path_out|name of the output folder(string)|

### Optional Arguments
|Parameter|Shortened|Default|Description|
|------|---|---|---|
|--remove_background|-rb|False|remove background if set|
|--width|-w|100|width to resize image(int)|
|--freq|-f|10|# of frames to capture per second(int)|

### Example
```shell
python3 main.py cat.mp4 cat -rb -w 200 -f 20
```
will create an ASCII animation based on `cat.mp4`, remove the background, resize to width of 200 characters, adjust frame rate to 20 fps, and save to `ascii/cat`.

## References
https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7
