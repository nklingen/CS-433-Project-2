"""
Helpers functions for AICrowd submission generation
These functions were taken and adapted from mask_to_submission.py provided by the EPFL ML course
"""
import os
import numpy as np
import matplotlib.image as mpimg
import re
import time


foreground_threshold = 0.25

""" Assign label to a patch. """
def patch_to_label(patch):
    df = np.mean(patch)
    if df > foreground_threshold:
        return 1
    else:
        return 0

""" Reads a single image and outputs the strings that should go into the submission file. """
def mask_to_submission_strings(image_filename):
    img_number = int(re.search(r"\d+", image_filename).group(0))
    im = mpimg.imread(image_filename)
    patch_size = 16
    for j in range(0, im.shape[1], patch_size):
        for i in range(0, im.shape[0], patch_size):
            patch = im[i:i + patch_size, j:j + patch_size]
            label = patch_to_label(patch)
            yield("{:03d}_{}_{},{}".format(img_number, j, i, label))

""" Converts images into a submission file. """
def masks_to_submission(submission_filename, *image_filenames):

    with open(submission_filename, 'w+') as f:
        f.write('id,prediction\n')
        for fn in image_filenames[0:]:
            f.writelines('{}\n'.format(s) for s in mask_to_submission_strings(fn))

""" Created the .csv submission file """
def submission_to_csv(submission_path, predictions_path):
    date = time.strftime("%d-%m-%Y")
    submission_filename = submission_path + 'submission_' + date +'.csv'
    image_filenames = []
    for i in range(1, 51):
        image_filename = predictions_path + 'satImage_' + '%.3d' % i + '.png'
        image_filenames.append(image_filename)
    masks_to_submission(submission_filename, *image_filenames)
