"""
#!/usr/bin/python3
#-*- coding: utf-8 -*-
@FileName: measure_execution_time.py.py
@Time: 2022/9/27 15:11        
@Author:
"""
import time
import tensorflow as tf
import numpy as np
import os

# only use the cpu
os.environ["CUDA_VISIBLE_DEVICES"] = ''

if __name__ == '__main__':
    # loading model in saved model format
    model = tf.saved_model.load('./saved_model')
    # mapping signature names to functions
    infer = model.signatures["serving_default"]

    exec_time = []
    # create random input for testing
    x = np.random.randn(1, 512).astype('float32')
    for idx in range(1010):
        # run timer
        start_time = time.time()
        # infer one block
        y = infer(tf.constant(x))['lambda_2']
        exec_time.append((time.time() - start_time))
    # ignore the first ten iterations
    print('Execution time per block: ' +
          str(np.round(np.mean(np.stack(exec_time[10:])) * 1000, 2)) + ' ms')