"""
MNIST handwritten digit classification with a convolutional neural network.

"""
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

from mnist_model import Model

def predict(images, save_dir='save/mnist'):
    # Model
    model = Model()

    # Saver
    saver = tf.train.Saver()

    with tf.Session() as sess:
        # Load model
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            print("Loading {}".format(ckpt.model_checkpoint_path))
            saver.restore(sess, ckpt.model_checkpoint_path)

        return model.predict(sess, images)

#///////////////////////////////////////////////////////////////////////////////

if __name__ == '__main__':
    # Load data
    data = input_data.read_data_sets('datasets/mnist', one_hot=True)

    idx   = 0
    image = data.test.images[idx]
    label = data.test.labels[idx]

    predicted_label = predict([image])[0]

    print("")
    print("True label for example image: {}".format(label.argmax()))
    print("Predicted label:              {}".format(predicted_label))

    plt.imshow(image.reshape((28, 28)), cmap='gray')