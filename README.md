
### photobooth-cleaner
The photobooth application on Mac OS does a couple of annoying things by default:
1) It creates spaces on filenames by default like this: `Photo on 1-12-20 at 2.56 PM.jpg`
2) It flips the image so it does not look what it looked like when you took the picture.

So I wrote this python program to fix these issues. Here is what it does:
1) It removes the spaces on the filenames like this : `Photo-on-1-12-20-at-2.56-PM.jpg`
2) It flops the image so that it looks exactly like what it looked like when you took the picture.

#### Installation
1) you will also need to have python version 3 which most recent OS should already have. If not, you should install
python version 3.5 or above. 
2) you will need to install imagemagick and one way to do that is with brew. 

```brew install imagemagick```

#### Usage
You can run the program from any where in your computer like this:

```python photobooth-cleaner.py```