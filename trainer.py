import cv2
import numpy as np
import os
from preprocessor import preprocess

# Load images from `dataset-true` and `dataset-false` directories
true_images = []
false_images = []

# Construct training data
for filename in os.listdir("dataset-true"):
    true_images.append(preprocess(cv2.imread("dataset-true/" + filename)))

for filename in os.listdir("dataset-false"):
    false_images.append(preprocess(cv2.imread("dataset-false/" + filename)))

# Construct labels
true_labels = np.ones(len(true_images), dtype=np.int32)
false_labels = np.zeros(len(false_images), dtype=np.int32)

# Merge data and labels
images = np.concatenate((true_images, false_images), axis=0)
labels = np.concatenate((true_labels, false_labels), axis=0)

# Convert image to np.matrix of float32
print(images.shape)
images = np.matrix(images, dtype=np.float32)
labels = np.array(labels, dtype=np.int32)

# Train model
model = cv2.ml.SVM_create()
model.setType(cv2.ml.SVM_C_SVC)
model.setKernel(cv2.ml.SVM_LINEAR)
model.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
model.train(images, cv2.ml.ROW_SAMPLE, labels)

# Save model
model.save("model.xml")
print("Model saved to `model.xml`")
