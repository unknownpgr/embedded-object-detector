import cv2
import os
import time

# Set this to `true` and run this script to collect images of target
# Set this to `false` and run this script to collect images for background
MODE = "true"

# Make `dataset` directory if not exist
if not os.path.exists("dataset-{}/".format(MODE)):
    os.makedirs("dataset-{}/".format(MODE))

# Open camera
cap = cv2.VideoCapture(0)

WIDTH = 1280
HEIGHT = 720

BOX_WIDTH = 480
BOX_HEIGHT = 640

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Copy frame
    displayframe = frame.copy()

    # Draw box at center
    cv2.rectangle(
        displayframe,
        (WIDTH // 2 - BOX_WIDTH // 2, HEIGHT // 2 - BOX_HEIGHT // 2),
        (WIDTH // 2 + BOX_WIDTH // 2, HEIGHT // 2 + BOX_HEIGHT // 2),
        (0, 255, 0),
        2,
    )

    # Display
    cv2.imshow("frame", displayframe)

    # Wait for key
    key = cv2.waitKey(1) & 0xFF

    # If key == q, exit
    if key == ord("q"):
        break

    # If key == s, save image in box to `dataset` directory
    if key == ord("s"):
        # Crop image
        cropped = frame[
            HEIGHT // 2 - BOX_HEIGHT // 2 : HEIGHT // 2 + BOX_HEIGHT // 2,
            WIDTH // 2 - BOX_WIDTH // 2 : WIDTH // 2 + BOX_WIDTH // 2,
        ]

        # Save image with timestamp
        cv2.imwrite("dataset-{}/{}.jpg".format(MODE, int(time.time())), cropped)
