# Binary To Image
> Convert those hard to read programs into nice color images!



## How to use it?
```bash
&> python3 main.py {Input Filename} {Output Filename}
```
You can also convert this file into anything you want. This file is completely open, so feel free to copy without worrying about any licences. 

## What it can do?
This program converts any file's data into nice color images. It takes each byte from a file and generates a color out of it. The color is defined by (`RED=tan(byte)`, `GREEN=cos(byte)`, `BLUE=sin(byte)`). When green is the only color (the input byte would be null) the color is switched to black. The output image format is `.png`. 

You can not convert big files with this tool as they take up way too much memory. I would use <30 MB files as anything above that eats up large amounts of ram. A 100MB file on my computer used over 11 GB of ram and crashed.  



## This is the output of `/bin/bash`
![qemu](https://user-images.githubusercontent.com/33582457/119050610-b72f8380-b987-11eb-8524-99d321923b25.png)

