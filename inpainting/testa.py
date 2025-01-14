import tensorflow as tf
import numpy as np
class test:
    def run_tensorflow(self):

        n_input = 10000
        n_classes = 1000

        # Create model
        def multilayer_perceptron(x, weight):
            # Hidden layer with RELU activation
            layer_1 = tf.matmul(x, weight)
            return layer_1

        # Store layers weight & bias
        weights = tf.Variable(tf.random_normal([n_input, n_classes]))


        x = tf.placeholder("float", [None, n_input])
        y = tf.placeholder("float", [None, n_classes])
        pred = multilayer_perceptron(x, weights)

        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
        optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

        #init = tf.global_variables_initializer()

        with tf.Session() as sess:
            #sess.run(init)

            for i in range(100):
                batch_x = np.random.rand(10, 10000)
                batch_y = np.random.rand(10, 1000)
                sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})

        print ("finished doing stuff with tensorflow!")

    