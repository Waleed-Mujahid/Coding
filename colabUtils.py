import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image 
import os,random

def plotLoss(history, validation = False, dims=(7,4)):
    plt.figure(figsize = dims)
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

def plotAccuracy(history, validation = False, dims=(7,4)):
    plt.figure(figsize = dims)
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

def visualizeData(filepath, dims, fig_size = (10,5)):
    plt.figure(figsize = fig_size)
    count = 1
    for folder in os.listdir(filepath):
        path = filepath + '/' + folder
        img = random.choice(os.listdir(path))
        img_path = path + '/' + img
        plt.subplot(dims[0],dims[1],count)
        img = Image.open(img_path)    # Visualizing the image
        img.load()
        plt.xticks([])             # Disabling ticks
        plt.yticks([])
        plt.title(folder)
        plt.imshow(img, cmap = 'gray')
        count += 1  
        img_width, img_height = img.size
