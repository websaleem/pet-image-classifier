#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Saleem Khan 
# DATE CREATED: 15/9/2025                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    # create a list of file names in the directory
    file_name_list = listdir(image_dir)
    
    # create an empty dictionary
    results_dic = dict()

    # iterate through all the files and assign the labels
    for idx in range(0, len(file_name_list)):

      # check if it not a root directory name
      if file_name_list[idx][0] != '.':

        # extract the pet label from the file name
        pet_label_name = file_name_list[idx]

        # convert to lower and split all the words into list
        pet_label_name_word_list = pet_label_name.lower().split('_')

        # have a pet name variable to assign the label
        pet_name = ""

        # iterate to all the words and create a pet name with space
        for pet_name_word in pet_label_name_word_list:

          # only use the name which are alphbetics
          if pet_name_word.isalpha():
            pet_name += pet_name_word + ' '

        # remove any whitespace either side of name
        pet_name = pet_name.strip()

        # insert to dictionary if does not already exist, else print error
        if file_name_list[idx] not in results_dic:
          results_dic[file_name_list[idx]] = [pet_name]
        else:
          print("The file {} label already exist in dictionary results_dic".format(file_name_list[idx]))

    # return the created dictionry with pet label name
    return results_dic
