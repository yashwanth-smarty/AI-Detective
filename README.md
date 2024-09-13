# AI Detective

AI Detective project is a face recognition system that uses a webcam to identify known faces from a set of pre-saved images. When a known face is detected, the system captures an image of the detected face and sends a notification with the image and details like current location of the camera, image name via Telegram. It can be integrated with CCTV cameras, making it suitable for security and monitoring applications.

## An illustration demonstrating the working of AI Detective
![Project Workflow](https://github.com/yashwanth-smarty/AI-Detective/blob/main/An%20illustration%20demonstrating%20the%20working%20of%20AI%20Detective%20project.jpeg?raw=true)

## Features

- Real-time face recognition using a webcam.
- Detection and recognition of faces from pre-saved images.
- Automatic saving of detected images.
- Notification sent to a Telegram chat with the detected image and details when a face is recognized a specific number of times.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- `face_recognition` library
- `telepot` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/face-recognition-system.git
    cd face-recognition-system
    ```
2. **Install Visual Studio with C++ Libraries (Windows Only):**

   If you are on Windows, you need to install Visual Studio with C++ development tools to compile the `dlib` library, which is a dependency of `face_recognition`.

   - Download and install Visual Studio Community from [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/).
   - During the installation, select **Desktop development with C++** under the **Workloads** tab.
   - Ensure that the **Windows 10 SDK** and **C++ CMake tools for Windows** are selected in the right-side panel.
3. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Telegram bot token and chat ID:

    ```env
    TELEGRAM_BOT_TOKEN=your_bot_token_here
    TELEGRAM_CHAT_ID=your_chat_id_here
    ```

## File Descriptions

- **`app.py`**: The main application script for real-time face recognition and processing.
- **`send.py`**: Contains the function to send notifications with the detected image via Telegram.
- **`requirements.txt`**: Lists the dependencies needed to run the project.

## Usage

1. **Prepare Images**:
   - Place the images you want to use for face recognition in the `images` directory. Ensure that the images are named appropriately as the script uses these names for recognition.

2. **Run the Application**:

    ```bash
    python app.py
    ```

   The application will start the webcam and process video frames for face recognition. When a recognized face is detected the specified number of times, an image will be saved and a notification will be sent via Telegram.

3. **Stop the Application**:
   - To stop the application, press `q` while the webcam window is open.

## Troubleshooting

- Ensure that your webcam is connected and functioning properly.
- Verify that the Telegram bot token and chat ID are correct and properly set in the `.env` file.
- If you encounter issues with face recognition, check the images in the `images` directory and ensure they are clear and properly formatted.

## Future Improvements

### Integration with CCTV Cameras

This face recognition system can be enhanced to work with CCTV cameras for real-time surveillance applications. Instead of using a standard webcam, the project can be integrated with CCTV cameras, including IP cameras and USB-connected CCTV cameras, by modifying the video capture source.

To integrate with CCTV cameras:

1. **Identify the Camera Stream URL**:
   - **IP Cameras**: Use the RTSP URL format, typically structured as:
     ```
     rtsp://username:password@ip_address:port/stream_path
     ```
   - **USB CCTV Cameras**: Use the appropriate device ID (e.g., `cv2.VideoCapture(1)`).

2. **Modify the Video Capture**:
   Replace the default webcam capture line in `app.py`:
   
   ```python
   cap = cv2.VideoCapture(0)

## Acknowledgments

- Thanks to the developers of [face_recognition](https://github.com/ageitgey/face_recognition) and [OpenCV](https://opencv.org/) for providing the libraries that made this project possible.
- Special thanks to [telepot](https://github.com/nickoala/telepot) for the Telegram bot integration.
