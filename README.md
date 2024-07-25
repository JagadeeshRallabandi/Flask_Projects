# Flask Projects with Haar Cascades and OpenCV

This repository contains several Flask projects that utilize Haar Cascades and OpenCV for face detection, face and eye detection, and video streaming. The frontend is built using HTML and CSS.

## Projects Included
1. **Face Detection**
2. **Face and Eye Detection**
3. **Video Streaming**

## Getting Started

### Prerequisites
- Python 3.x
- `virtualenv` package

### Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/flask-opencv-projects.git
    cd flask-opencv-projects
    ```

2. **Create a virtual environment**
    ```sh
    python3 -m venv venv
    ```

3. **Activate the virtual environment**
    - **On Windows**
        ```sh
        venv\Scripts\activate
        ```
    - **On macOS/Linux**
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Projects

1. **Face Detection**
    ```sh
    cd face_detection
    python app.py
    ```

2. **Face and Eye Detection**
    ```sh
    cd face_eye_detection
    python app.py
    ```

3. **Video Streaming**
    ```sh
    cd video_streaming
    python app.py
    ```

### Folder Structure

```plaintext
flask-opencv-projects/
│
├── face_detection/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── haarcascades/
│
├── face_eye_detection/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── haarcascades/
│
├── video_streaming/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── haarcascades/
│
└── requirements.txt
```
