# --------------------------
# 1. Import required libraries
#    - OS, IO, requests, time
#    - datetime for timestamps
#    - Pillow for image handling (Image, ImageDraw, ImageFont)
#    - HF_API_KEY from config
# --------------------------

# --------------------------
# 2. Define constants
#    - MODEL name (facebook/detr-resnet-50)
#    - API endpoint URL
# --------------------------

# --------------------------
# 3. Function: ask_image()
#    - Prompt user for image path
#    - Validate if file exists
#    - Open file as bytes
#    - Return path + bytes
# --------------------------

# --------------------------
# 4. Function: infer()
#    - Send image bytes to Hugging Face API (POST request)
#    - Include Authorization header with API key
#    - Retry if model is warming up (status 503)
#    - Return detections as JSON response
# --------------------------

# --------------------------
# 5. Function: draw()
#    - Take image + detections
#    - For each detection:
#         - Check confidence score threshold
#         - Extract bounding box coordinates
#         - Draw rectangle on image
#         - Write label + confidence above box
#    - Return annotated image
# --------------------------

# --------------------------
# 6. Function: main()
#    - Call ask_image() to get path + bytes
#    - Call infer() to get detections
#    - Open image in Pillow
#    - Call draw() to annotate
#    - Save annotated image with timestamp
#    - Print confirmation / error messages
# --------------------------

# --------------------------
# 7. Entry point
#    - Run main() only if script is executed directly
# --------------------------
