import cv2


class Ipy:
    """
    Helper class for Ipython notebook prints, show images
    """

    @staticmethod
    def imshow_large(input_image):
        """
        API is to show bigger images in ipython notebook. Uses PIL, IPython.display and BytesIO
        """
        from PIL import Image
        import IPython.display
        from io import BytesIO
        
        rgb_img = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_img)

        b = BytesIO()
        img.save(b, format='png')

        IPython.display.display(IPython.display.Image(data=b.getvalue(), format='png', embed=True))

    @staticmethod
    def imshow(input_image):
        """
        API to show mini image in ipython notebook, using matplotlib
        """
        import matplotlib.pyplot as plt

        cv_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        plt.axis("off")
        plt.imshow(cv_rgb)
