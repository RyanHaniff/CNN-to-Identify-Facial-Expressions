import cv2

class ImageProcessing:

    def happy_img(self):
        img = cv2.imread('..COMP_473_PROJECT/CK+48/happy/S010-006-00000013.png')
        print(img.show)
        # cv2.imshow('img', img)




def main():
    ip = ImageProcessing()
    ip.happy_img()



if __name__ == '__main__':
    main()
