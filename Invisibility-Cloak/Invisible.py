#You will write every line of this yourself by 11pm.
import cv2
import numpy as np
import time

#Open camera
cap = cv2.VideoCapture(0)

#Allow camera to warm up
time.sleep(2)

print("STEP OUT OF FRAME! Capturing background in 3 seconds...")
time.sleep(3)

#Capture multiple frames and compute the median background
frames = []
for _ in range(30):
    ret, frame = cap.read()
    if ret:
        frames.append(frame)

background = np.median(frames, axis=0).astype(np.uint8)

print("Got it. STEP BACK IN with your cloth! (press q to quit)")
time.sleep(3)

#HSV range for RED color
lower1 = np.array([0, 120, 70])
upper1 = np.array([10, 255, 255])

lower2 = np.array([170, 120, 70])
upper2 = np.array([180, 225, 255])

#Morphological kernel
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for red color
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Replace cloak pixels with background
    frame[mask > 0] = background[mask > 0]

    # Show output
    cv2.imshow("Invisibility Cloak - Press q to quit", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Cleanup
cap.release()
cv2.destroyAllWindows()