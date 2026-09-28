An interactive computer vision project that brings the famous Harry Potter Invisibility Cloak to life using Python and OpenCV. The script captures a background scene, detects a specific color in real-time (configured for Red), and replaces it with the background to create an illusion of invisibility.

How It Works Background Capturing: The program captures several frames of the static environment and calculates the median background. Color Detection: The video stream converts the frames from BGR to HSV color space to distinguish the color of the cloak. Masking and Background Noise Removal: The morphological operations such as MORPH_OPEN and dilation helps in smoothing of the mask edges and removal of background noise. Segment Replacement: The pixels of the cloak segment are dynamically replaced by the captured background pixels. Prerequisites Ensure that you have Python installed, followed by the installation of the following dependencies: bash

pip install opencv-python numpy

How to Execute

Execute the Python script:

python cloak.py

Move away from the camera frame within a couple of seconds. The program will wait 3 seconds for capturing your background environment. After that, you will see "Got it. STEP BACK IN...". Then come back to the camera frame while wearing your colored cloak. Press 'q' at any point to quit the program. Customizing the Color
