##############
## PREAMBLE ##
##############

import os
import cv2
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# NOTE: Place all images to be processed in a directory
# called "images" within the source directory
input_img_path = f'{os.path.dirname(os.path.realpath(__file__))}\\images'

# Create output directory for processed images if it doesn't already exist
output_img_path = f'{input_img_path}\\output'
if not os.path.isdir(output_img_path):
    os.mkdir(output_img_path)

# Description of various algorithms:
# 1: Using a manual threshold value on the RGB average
# 2: Kmeans Clustering using RGB columns
# 3: Kmeans Clustering using RGB average
# 4: Kmeans Clustering using RGB average and stdev
# NOTE: Edit list to control which algorithms to run
algorithm_list = [1,2,3,4]

threshold_algorithm_one = 200



##################
## MAIN PROGRAM ##
##################

# Add the files in the image directory to a list
file_list = []
[ file_list.append(files) for root,folders,files in os.walk(input_img_path)]

# Main Loop (cycle through input folder for files)
for input_img in file_list[0]:

    # Store image as array
    full_path = f'{input_img_path}\\{input_img}'
    img = cv2.imread(full_path)

    # Extract image shape as height, width, and depth
    height = img.shape[0]
    width = img.shape[1]
    depth = img.shape[2]

    # Reshape array with pixels in single row with rgb values as columns
    img = img.reshape( height * width, depth )

    # Loop through each algorithm
    for algorithm in algorithm_list:

        # Convert array to DataFrame and add calculated columns
        df = pd.DataFrame(img,columns=['R','G','B'])
        df['calc'] = df[['R','G','B']].mean(axis=1)
        df['calc2'] = df[['R','G','B']].std(axis=1)
        
        if algorithm == 1 or algorithm == 3:
            df = pd.DataFrame(df['calc'])
        
        if algorithm == 1:
            df['result'] = (df['calc'] > threshold_algorithm_one).astype(int)
            algorithm_results = pd.array(df['result'])
        
        if algorithm == 4:
            df = pd.DataFrame(df[['calc','calc2']])

        if algorithm != 1:
            # Execute K-Means Clustering Algorithm
            model_obj = KMeans(n_clusters=2)
            model_obj.fit(df)

            # Assign variable for the algorithm results
            algorithm_results = model_obj.labels_

        # Color list for setting and inverting output colors
        color = [[255,0], [0,255]]

        # Loop through twice to create two files with inverted colors
        for x in range(0,2):

            # Rebuild image as black and white based off results
            img_results = np.zeros((height * width, depth))
            for row in range(0,img.shape[0]):
                if algorithm_results[row] == 0:
                    new_value = color[x][0]
                else:
                    new_value = color[x][1]
                for col in range(0,img.shape[1]):
                    img_results[row][col] = new_value

            # Reshape output image
            output_img = img_results.reshape(height,width,depth)

            # Store filename and extension as separate variables
            filename = input_img[ : input_img.find('.') ]
            extension = input_img[ input_img.find('.') + 1 : ]

            # Set name for output image and save it to disk
            file_output = f'{output_img_path}\\_{filename}_output_v{str(algorithm)}-{str(x+1)}.{extension}'
            cv2.imwrite(file_output,output_img)

print('\nDone...\n')