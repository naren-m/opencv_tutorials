"""
To run this tutorial we need ot have
the conda environment with opencv installed in it
"""

import cv2


def main():
    """
    main func
    """
    #capture from camera at location 0
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()

        cv2.imshow("input", img)

        key = cv2.waitKey(10)
        if key == 27:
            break

    cv2.destroyAllWindows()
    cv2.VideoCapture(0).release()

if __name__ == '__main__':
    main()
