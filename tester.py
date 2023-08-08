import cv2
import numpy as np
from preprocessor import preprocess

# Load model
model = cv2.ml.SVM_load("model.xml")

# Test model
cap = cv2.VideoCapture(0)
WIDTH = 1280
HEIGHT = 720
BOX_WIDTH = 240
BOX_HEIGHT = 320
STRIDE = 80

# Write video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
    filename="output.mp4", fourcc=fourcc, fps=25, frameSize=(WIDTH, HEIGHT)
)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Copy frame
    displayframe = frame.copy()

    # Slide box
    for y in range(0, HEIGHT - BOX_HEIGHT, STRIDE):
        for x in range(0, WIDTH - BOX_WIDTH, STRIDE):
            # Crop image
            cropped = frame[y : y + BOX_HEIGHT, x : x + BOX_WIDTH]

            # Preprocess image
            cropped = preprocess(cropped)

            # Predict
            prediction = model.predict(np.matrix(cropped))
            if prediction[1][0][0] == 1.0:
                # Draw box
                cv2.rectangle(
                    displayframe,
                    (x, y),
                    (x + BOX_WIDTH, y + BOX_HEIGHT),
                    (0, 255, 0),
                    2,
                )

    cv2.imshow("frame", displayframe)
    out.write(displayframe)

    # Wait for key
    key = cv2.waitKey(1) & 0xFF

    # If key == q, exit
    if key == ord("q"):
        break
