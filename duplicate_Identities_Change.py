import os
import re
import cv2

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

    data_dir = '../COMP_473_Project/CK+'
    aug_data_dir = '../COMP_473_Project/CK_Augmented'

    # if not os.path.isdir(aug_data_dir):
    #     os.mkdir(aug_data_dir)

    for image_class in os.listdir(data_dir):
        # print(image_class)
        for image in os.listdir(os.path.join(data_dir, image_class)):
            image_name = image
            print(image_name)
            image_path = os.path.join(data_dir, image_class, image)

            image = cv2.imread(image_path)  # cv2.IMREAD_UNCHANGED
            face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            faces = face_cascade.detectMultiScale(image, 1.3, 5)
            global crop_img
            for (x, y, w, h) in faces:
                # To draw a rectangle in a face
                # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                crop_img = image[y:y + h, x:x + w]

            cv2.imwrite(os.path.join(aug_data_dir, image_class, image_name), crop_img)


"""
We are dividing each class into training(training and eval) and testing
when one person is in training set of an emotion they have to be only in training
skip contempt and neutral
"""

if __name__ == "__main__":
    main()
