# Face-Recognition-Attendance-System

This repository hosts the code for a Face Recognition Attendance System. Developed with Tkinter, OpenCV, and MySQL, the system captures student details, trains a face recognition model, and marks attendance based on recognized faces. Key features include real-time face detection, model training, and database integration.

## Files

### 1. `train.py`

- **Description:** This script is responsible for training the LBPH Face Recognizer using the captured photos of students. The trained model is utilized for subsequent face recognition.

### 2. `student.py`

- **Description:** `student.py` contains the class definition for a Student. It includes methods for capturing student details and saving their photos.

### 3. `help.py`

- **Description:** `help.py` provides helper functions that are used across different modules of the Face Recognition Attendance System.

### 4. `face_recognizer.py`

- **Description:** `face_recognizer.py` encapsulates the logic for recognizing faces using the trained LBPH Face Recognizer.

### 5. `Face Recognition.py`

- **Description:** This script is the main entry point for the Face Recognition Attendance System. It includes the GUI created using Tkinter and orchestrates the overall flow of the application.

### 6. `developer.py`

- **Description:** `developer.py` contains information about the developer(s) contributing to the Face Recognition Attendance System.

### 7. `attendance.py`

- **Description:** `attendance.py` manages the marking of attendance in the MySQL database based on recognized faces.

### 8. `Ensure`

- **Description:** Ensure the Classifier (Classifier.xml) , Haar Cascade Classifier XML file (haarcascade_frontalface_default.xml) is present in the project directory, and all the necessory directory and file as well.

## Usage

1. Run the `Face Recognition.py` script to launch the Face Recognition Attendance System.

2. Interact with the Tkinter GUI to capture student details, train the face recognition model, and mark attendance.

3. Refer to specific files (`train.py`, `student.py`, etc.) for detailed implementation and functionality.

4. Also go through files and import or install required libraries.

## Contributions

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to create issues or pull requests.
