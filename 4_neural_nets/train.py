
import os
import numpy as np
import matplotlib.pyplot as plt
import time

from neural_net import NeuralNet

train_filepath = os.path.join("4_neural_nets", "mnist_train.csv")
train_file = open(train_filepath, 'r')
train_list = train_file.readlines()
train_file.close()

test_filepath = os.path.join("4_neural_nets", "mnist_test.csv")
test_file = open(test_filepath)
test_list = test_file.readlines()
test_file.close()


def display_image(img_list, img_index):
    '''
    We use this function to display any image given the image_list and the index of the image we want to display.
    '''
    all_values = img_list[img_index].split(',') #img_list is a list of strings. this splits each string into a list at every ,
    image_array = np.asfarray(all_values[1:]).reshape((28,28))
    plt.imshow(image_array, cmap='Greys', interpolation='None') # this plots the image

display_image(train_list, 59999)
plt.show() #this tells python to open the plot

######################################################################

nn = NeuralNet(sizes=[784, 128, 64, 10], epochs=10, lr=0.001)
nn.train(train_list, test_list, 10, function_type="relu")





