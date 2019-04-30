#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sotirios Zikas
# DATE CREATED: April 11, 2019                                 
# REVISED DATE: 

# Imports python modules
from os import listdir
from os import path


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
    filenames = listdir(image_dir)
    results_dic = dict()
    
    for i in range(0, len(filenames), 1):
        if filenames[i][0] != ".":
            label_placeholder = ""
            pet = filenames[i]
            pet_lowercase = pet.lower()
            pet_no_ext = path.splitext(pet_lowercase)[0]
            pet_lower_separated = list(pet_no_ext.split('_'))
            
            for word in pet_lower_separated:
                if word.isalpha():
                    label_placeholder += word + " "
                    
            label_placeholder = label_placeholder.strip()
            
            if filenames[i] not in results_dic:
                results_dic[filenames[i]] = [label_placeholder]
            else:
                print("** Warning: Double file in directory: ", filename[i])
    
    
    
    
  
# Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
