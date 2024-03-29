#!/usr/bin/env python3
"""
Module to create a layer
"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """
    a function that create layers
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=init,
                            name="layer")
    return layer(prev)
