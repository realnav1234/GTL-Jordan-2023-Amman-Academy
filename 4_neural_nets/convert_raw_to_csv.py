
import os

def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

# train_images_x = "..\data\MNIST\raw\train-images-idx3-ubyte"
train_images_x = os.path.join("data", "MNIST", "raw", "train-images-idx3-ubyte")
print(train_images_x)
# train_images_x = "C:\Users\navpr\Documents\GTl-Jordan\GTL-Jordan-2023-Amman-Academy\data\MNIST\raw\train-images-idx3-ubyte"
train_images_y = os.path.join("data", "MNIST", "raw", "train-labels-idx1-ubyte")
train_outf = "4_neural_nets\mnist_train.csv"

test_images_x = os.path.join("data", "MNIST", "raw", "t10k-images-idx3-ubyte")
test_images_y = os.path.join("data", "MNIST", "raw", "t10k-labels-idx1-ubyte")
test_outf = "4_neural_nets\mnist_test.csv"

convert(train_images_x, train_images_y, train_outf, 60000)
convert(test_images_x, test_images_y, test_outf, 10000)

train_file = open(train_outf, 'r')
train_list = train_file.readlines()
train_file.close()

print(len(train_list))
