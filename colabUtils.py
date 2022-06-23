import matplotlib.pyplot as plt

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