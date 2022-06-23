import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image 

def plotLoss(history, validation = False, height = 7, width = 4):
    plt.figure(figsize = (height,width))
    plt.plot(history.history['loss'])    
    plt.title('Loss Curve')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    if (validation) :
        plt.plot(history.history['val_loss'])
        plt.legend(['Train', 'Test'], loc='upper right')
    # else :
    #     plt.legend(['Train'], loc='upper right')
    plt.show()

def plotAccuracy(history, validation = False, height = 7, width = 4):
    plt.figure(figsize = (height,width))
    plt.plot(history.history['accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    if (validation) :
        plt.plot(history.history['val_accuracy'])
        plt.legend(['Train', 'Test'], loc='lower right')
    plt.show()

def processImg(path,target_shape,show=False,grayscale=False ):
    if (show):
        _img = Image.open(path)    # Visualizing the image
        _img.load()
        plt.xticks([])             # Disabling ticks
        plt.yticks([])
        plt.imshow(_img)

    # Converting the image so it can be fed into the model
    img = tf.io.read_file(path)
    img = tf.image.decode_image(img)
    test_img = tf.image.resize(img, size = target_shape)    # Resize the image according to the model
    if (grayscale):
        test_img = tf.image.rgb_to_grayscale(test_img)                     # Model expects a grayscale image
    test_img = test_img/255.                                           # Normalizing the image
    return test_img
