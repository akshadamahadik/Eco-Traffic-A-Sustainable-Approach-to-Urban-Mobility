import numpy as np
import argparse
import cv2 as cv
import os
import time
from yolo_utils import infer_image

class YOLOObjectDetection:
    TARGET_OBJECTS = {'car', 'motorbike', 'bus', 'truck'}

    @staticmethod
    def process_images(folder_path, output_folder, net, layer_names, colors, labels):
        """Process all images in the given folder and detect target objects."""
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        results = {}

        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            img = cv.imread(image_path)

            if img is None:
                print(f"Error loading image: {image_name}")
                continue

            height, width = img.shape[:2]

            # Run YOLOv3 inference
            img, boxes, confidences, classidp, idxs = infer_image(
                net, layer_names, height, width, img, colors, labels, FLAGS
            )

            # Dictionary to store detected object counts
            object_counts = {}

            if idxs is not None:
                for i in idxs.flatten():
                    obj_name = labels[classidp[i]]

                    if obj_name in YOLOObjectDetection.TARGET_OBJECTS:
                        object_counts[obj_name] = object_counts.get(obj_name, 0) + 1

                    # Draw bounding boxes and labels
                    x, y, w, h = boxes[i]
                    color = [int(c) for c in colors[classidp[i]]]
                    cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    text = f"{obj_name}: {confidences[i]:.2f}"
                    cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Save processed image
            output_image_path = os.path.join(output_folder, image_name)
            cv.imwrite(output_image_path, img)

            results[image_name] = object_counts
            print(f"Processed {image_name} -> {object_counts}")

        return results

    @staticmethod
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-m', '--model-path', type=str, default='./yolov3-coco/', help='Model weights and config directory.')
        parser.add_argument('-w', '--weights', type=str, default='./yolov3-coco/yolov3.weights', help='YOLOv3 weights file.')
        parser.add_argument('-cfg', '--config', type=str, default='./yolov3-coco/yolov3.cfg', help='YOLOv3 config file.')
        parser.add_argument('-l', '--labels', type=str, default='./yolov3-coco/coco-labels', help='Path to COCO labels file.')
        parser.add_argument('-f', '--folder', type=str, default='./images/', help='Folder containing images.')
        parser.add_argument('-o', '--output', type=str, default='./output_images/', help='Folder to save processed images.')
        parser.add_argument('-c', '--confidence', type=float, default=0.5, help='Confidence threshold.')
        parser.add_argument('-th', '--threshold', type=float, default=0.3, help='Non-Max Suppression threshold.')

        global FLAGS
        FLAGS, _ = parser.parse_known_args()

        # Load labels
        labels = open(FLAGS.labels).read().strip().split('\n')

        # Initialize colors for each label
        colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

        # Load YOLOv3 model
        net = cv.dnn.readNetFromDarknet(FLAGS.config, FLAGS.weights)
        layer_names = net.getLayerNames()
        layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        # Process images
        results = YOLOObjectDetection.process_images(FLAGS.folder, FLAGS.output, net, layer_names, colors, labels)
        return results


