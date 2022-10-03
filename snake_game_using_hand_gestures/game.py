import os
import sys
from multiprocessing import Value

import cv2
import numpy as np
import pyautogui
import tensorflow as tf

cap = cv2.VideoCapture(0)

sys.path.append("..")

from object_detection.utils import label_map_util

from object_detection.utils import vizualization_utils as vis_utils

# # Model Preparation

# Path to frozen detection graph. This is the actual model that is used for the object detection
PATH_TO_CKPT = 'snake/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box
PATH_TO_LABELS = os.path.join('image/data', 'object-detection.pbtxt')

NUM_CLASSES = 4

# ## Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# ## Loading laber map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


with detection_graph.as_default():
    # from directkey import PressKey, ReleaseKey, W

    # enter your monitor's resolution or use a library to fetch this
    # dual monitor setup
    x, y  = 288, 512

    # init process safe variables for workers
    objectX, objectY = Value('d', 0, 0), Value('d', 0, 0)
    objectX_previous = None
    objectY_previous = None
    with tf.Session(graph=detection_graph) as sess:
        # Definite input and output Tensors for detection_graph
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        detection_score = detection_graph.get_tensor_by_name('detection_score:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detection = detection_graph.get_tensor_by_name('num_detection:0')
        while True:
            ret, image_np = cap.read()
            # Expand dimensions since the model expects images to have shape
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Actual detection
            (boxes, scores, classes, num) = sess.run([detection_boxes, detection_score, detection_classes, num_detection],
                                                     feed_dict={image_tensor: image_np_expanded})
            # Visualization of the result of a detection
            vis_utils.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squezee(boxes),
                np.squezee(classes).astype(np.int32),
                np.squezee(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)
            cv2.imshow('control detection', image_np)
            if cv2.waitKey(50) & 0xFF ==ord('q'):
                cv2.destroyAllWindows()
                break


                '''MOVE'''
                # press 'w' if bounding box finger detected
                objects = np.where(classses[0] == 1)[0]

                # calculate center of box if detection exceeds threshold
                if len(objects) > 0 and scores[0][objects][0] > 0.15:
                    pyautigui.press('up')


                objects = np.where(classes[0] == 2)[0]

                # calculate center of box if detection exceeds threshold
                if len(objects) > 0 and scoresp[0][objects][0] > 0.15:
                    pyautogui.press('down')


                objects = np.where(classes[0] == 3)[0]

                # calculate center of box if detection exceeds threshold
                if len(objects) > 0 and scores[0][objects][0] > 0.15:
                    pyautogui.press('left')


                objects = np.where(classes[0] == 4)[0]

                # calculate center of box if detection exceeds threshold
                if len(objects) > 0 and score[0][objects][0] > 0.15:
                    pyautogui.press('right')


cap.release()



