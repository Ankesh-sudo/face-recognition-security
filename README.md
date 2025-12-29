# 🔐 Face Recognition Security System

A real-time Face Recognition–based Authentication System built using Python, OpenCV, and dlib, designed to securely identify and authenticate users through live webcam input.

This project demonstrates practical skills in computer vision, machine learning integration, dependency management, and secure system design.

## 🚀 Features

📸 Real-time face detection & recognition using webcam

👤 User registration by capturing face images

🧠 Face encoding & matching using dlib’s face recognition model

🔐 Authentication system with authorized / unauthorized detection

🟢 Green bounding box for authorized users

🔴 Red bounding box for unauthorized users

🪞 Mirrored camera preview for natural user experience

📦 Clean project structure with proper Git hygiene

## 🛠️ Tech Stack

Programming Language: Python 3.10

Computer Vision: OpenCV

Face Recognition: dlib, face_recognition

Data Handling: NumPy

Web Framework (future-ready): Flask

Version Control: Git & GitHub

## 📂 Project Structure
face-recognition-security/
│
├── backend/
│   ├── camera.py          # Webcam utility
│   ├── face_encode.py     # Generate face encodings
│   ├── face_auth.py       # Real-time face authentication
│   └── register_user.py   # Register new users
│
├── data/
│   ├── known_faces/       # User face images
│   └── encodings/
│       └── face_encodings.pkl
│
├── docs/
│   └── screenshots/
│       └── face_auth_success.png
│
├── static/                # (For future web UI)
├── templates/             # (For future web UI)
│
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Ankesh-sudo/Face-Recognition-Security.git
cd Face-Recognition-Security

2️⃣ Create Virtual Environment
python3.10 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


⚠️ Python 3.10 is required for stability with dlib and face_recognition.

## ▶️ How to Run
🔹 Register a New User
python backend/register_user.py

🔹 Generate Face Encodings
python backend/face_encode.py

🔹 Start Face Authentication
python backend/face_auth.py


Press Q to exit the camera window.

📸 Demo Screenshot

## 🧠 How It Works (High-Level)

User face images are captured and stored

Facial features are converted into numerical encodings

Live webcam feed is processed frame-by-frame

Face encodings are compared in real time

User is marked Authorized or Unauthorized

## 🔒 Security & Design Considerations

No full system scanning (safe & ethical design)

No real-time background monitoring

Designed as an authentication system, not antivirus

Virtual environment excluded from version control

Dependencies pinned for reproducibility

## 📈 Future Enhancements

🌐 Web-based login system using Flask

🗂 Authentication logs & access history

📊 Confidence score for face matching

👥 Multi-user role management

☁️ Cloud deployment

## 👤 Author

Ankesh Kumar Thakur
🎓 BCA Student | Aspiring Cybersecurity Professional
📍 Odisha, India
