# image-to-black-and-white
This program attempts to convert a logo/picture file into true black and white using a machine learning algorithm

## Backstory:

This project started out with me manually editing some small logos for another project. I was cleaning up edges and removing those random off-white artifacts you see in the whitespace of low quality picture files using image editing software. The goal was to make the logos true black and white (no shades of gray). The files were small and I only needed to complete two of them for my project so it wasn't too intensive, but I did wonder if there was a way that I could speed up the task.

I did first attempt to utilize built-in functions in a few other imaging programs to achieve this effect, and it did work well enough on relatively clean files but not so much on more complicated logo files (those with shading, 3D effects, etc.). And even then, while the conversion was quicker, I still had to open each file and perform the task manually.

I am in the middle of taking some data science and machine learning classes, and I have a small piece of code I recently wrote to convert an image file into an array, traverse the array, modify the RGB values, and rebuild the image so that's a good starting point. I've been looking for a way to apply what I've learned in these classes towards some sort of application of my own, so I started thinking of algorithms that might accomplish this task.

## Algorithms:

### Algorithm #1:
I started with that initial piece of code and built a very simple algorithm which averaged together the RGB values and chose black or white based on a set threshold value. It worked well for clean logos just as the imaging software but not so well on more complex images, but at least now I could automate it.

### Algorithm #2:
Next, I wanted to make use of a machine learning algorithm. Since this would be unsupervised learning, I decided to go with the K-Means Clustering algorithm. After a little bit of data formatting to get pixels in a single column with three additional columns for the RGB values, I used this as the input for the algorithm. Results were better but still not ideal on the more complex images.

### Algorithm #3:
Same as #2, but used the RGB average instead. It worked about the same as #2, sometimes worse.

### Algorithm #4:
Same as #3, but I added a column for the standard deviation of the RGB values. This algorithm seems to work the best, although it is still far from perfect.

### Other ideas I haven't tried yet:
- Utilizing an aggregate function other than 'mean', perhaps min or max.
- Testing standard deviation on its own. The closer the RGB values are to each other, the more grayscale they are. Maybe this will work well on colored logos, but may still have issues with shading.
- Try out some other machine learning algorithms.

## Other Notes on Software:

1. The 'images' file in this repository contains a few of the logos I've tried so far, with varying success.

2. I added automation to process multiple files in a single run. Place any image you want to process into a folder called 'images' in the source folder and the program will run all files through the program.

3. The program also loops through all the algorithms. There is a list in the source that can be modified to run any combination of the algorithms.

4. The machine learning algorithm assigns an arbitrary 0 or 1 to the files and I do not currently have a way to determine which color belongs to which designation. To get around this, I simply generate two files, one being the inverse of the other.

5. I am still trying to solve an issue with transparency. The program does not work well if the logo has a transparent background. I am working on a fix for this, but for now I have to manually go into the image file and add a white pixel in the upper left corner which seems to "break the transparency". This seems to allow the algorithm to run as expected for the moment.

## Wrap Up:
This initial release was developed in just a few days. I'd like to continue to develop it to see if I can perfect it as I learn some new machine learning tricks, but I wanted to get it uploaded on here. I'm pretty happy with it so far even though it doesn't do the whole job yet. It seems to do a better job than the manual imaging solutions I tried and it's automated...it can process 6 images through 4 algorithms with 2 outputs each in less than a minute. Most importantly, I was able to apply some machine learning to my own application, so all in all this was a good learning experience.
