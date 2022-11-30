import os
import re
import cv2

# TODO
"""Crop the image to the edge of the eye location"""


def main():
    # data_dir = '../COMP_473_Project/CK+'
    # new_dir = '../COMP_473_Project/CK_formatted'
    #
    # for image_class in os.listdir(data_dir):
    #     print(image_class +"-----------------------")
    #     for image in os.listdir(os.path.join(data_dir, image_class)):
    #         image_path = os.path.join(data_dir, image_class, image)
    #         # print(image_path)
    #
    #         name = re.findall(r'(?<=\/)S[0-9]+', image_path)
    #
    #         print(name[0])

    data_dir = '../COMP_473_Project/CK+'
    aug_data_dir = '../COMP_473_Project/CK_Augmented'

    if not os.path.isdir(aug_data_dir):
        os.mkdir(aug_data_dir)

    cw, ch = 248, 248
    half_size = 248 // 2
    cx, cy = 0, 0
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
                # # To draw a rectangle in a face
                # # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                # if ((x + w) or (y + h)) < 248:
                #
                #     # Get the center coordinate of the image
                #     center_y = y + h // 2
                #     center_x = x + w // 2
                #
                #     # Get the top left corner based on desired final dimension of the image
                #     cx = center_x - half_size
                #     cy = center_y - half_size

                # crop_img = image[y:cy + ch, x:cx + cw]
                crop_img = image[y:y + h, x:x + w]

            cv2.imwrite(os.path.join(aug_data_dir, image_class, image_name), crop_img)


"""
We are dividing each class into training(training and eval) and testing
when one person is in training set of an emotion they have to be only in training
skip contempt and neutral
"""

if __name__ == "__main__":
    main()
