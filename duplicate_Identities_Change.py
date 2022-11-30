import os
import re

# TODO
"""Crop the image to the edge of the eye location"""


def main():
    data_dir = '../COMP_473_Project/CK+'
    new_dir = '../COMP_473_Project/CK_formatted'

    for image_class in os.listdir(data_dir):
        print(image_class +"-----------------------")
        for image in os.listdir(os.path.join(data_dir, image_class)):
            image_path = os.path.join(data_dir, image_class, image)
            # print(image_path)

            name = re.findall(r'(?<=\/)S[0-9]+', image_path)

            print(name[0])


"""
We are dividing each class into training(training and eval) and testing
when one person is in training set of an emotion they have to be only in training
skip contempt and neutral
"""

if __name__ == "__main__":
    main()
