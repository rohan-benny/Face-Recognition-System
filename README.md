# 🎓 Face Recognition Attendance System

A comprehensive face recognition-based attendance system built with Python, OpenCV, and Firebase. This system provides an automated solution for student attendance tracking using facial recognition technology with an intuitive graphical user interface.

## 📷 Screenshots

### Login Screen
![Login Screen](screenshots/login.png)

### Main Dashboard
![Main Dashboard](screenshots/dashboard.png)

### Student Management
![Student Management](screenshots/student_management.png)

### Face Recognition in Action
![Face Recognition](screenshots/face_recognition.png)

### Attendance Records
![Attendance Records](screenshots/attendance.png)

## ✨ Features

- **User Authentication**: Secure login system with username and password protection
- **Student Management**: Add, update, delete, and manage student information with Firebase integration
- **Photo Capture**: Automated facial image capture system for training data collection
- **Face Recognition**: Real-time face detection and recognition using OpenCV and Haar Cascade classifiers
- **Training Module**: Train the face recognition model with captured student photos
- **Attendance Tracking**: Automatic attendance marking with timestamp when a face is recognized
- **Attendance Management**: View, export, and manage attendance records in CSV format
- **Modern GUI**: Clean and intuitive user interface built with Tkinter
- **Cloud Storage**: Firebase integration for secure data storage and management

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **OpenCV**: Computer vision library for face detection and recognition
- **Tkinter**: GUI framework
- **PIL (Pillow)**: Image processing
- **Firebase**: Cloud database for student data storage
- **NumPy**: Numerical computing
- **CSV**: Attendance record management

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

```bash
Python 3.x
pip (Python package manager)
```

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rohan-benny/Face-Recognition-System.git
   cd Face-Recognition-System
   ```

2. **Install required packages**
   ```bash
   pip install opencv-python opencv-contrib-python
   pip install pillow
   pip install numpy
   pip install firebase-admin
   ```

3. **Firebase Setup**
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Generate a service account key (JSON file)
   - Rename the file to match the import in `firebaseconfig.py` or update the filename
   - Place the JSON file in the project root directory
   - **Important**: Keep this file secure and never commit it to version control

4. **Configure Firebase**
   - Update the `firebaseconfig.py` file with your Firebase credentials
   - Ensure your Firebase Realtime Database rules are properly configured

## 📁 Project Structure

```
Face-Recognition-System/
│
├── Assets/                          # UI assets and button images
│   ├── background_image.png
│   ├── button_1.png - button_6.png
│   └── ...
│
├── Data/                           # Stored face images for training
│   └── user.[id].[count].jpg
│
├── screenshots/                    # Application screenshots for documentation
│   ├── login.png
│   ├── dashboard.png
│   └── ...
│
├── main.py                         # Main application entry point
├── login.py                        # Login system
├── student.py                      # Student management module
├── train.py                        # Model training module
├── face_recognition.py             # Face recognition module
├── attendance.py                   # Attendance management module
├── firebaseconfig.py               # Firebase configuration
├── haarcascade_frontalface_default.xml  # Haar Cascade classifier
├── classifier.xml                  # Trained face recognition model
├── Attendance.csv                  # Attendance records
└── README.md                       # Project documentation
```

## 🚀 Usage

1. **Start the Application**
   ```bash
   python login.py
   ```

2. **Login**
   - Enter your username and password
   - Default credentials can be set in the login module

3. **Student Management**
   - Click on "Student Details" button
   - Add new students with their information
   - Capture face samples (150 images per student recommended)

4. **Train the Model**
   - Click on "Train Data" button
   - Wait for the training process to complete
   - The trained model will be saved as `classifier.xml`

5. **Mark Attendance**
   - Click on "Face Recognition" button
   - The system will activate the camera
   - Recognized faces will automatically mark attendance with timestamp

6. **View Attendance**
   - Click on "Attendance" button
   - View, search, and export attendance records
   - Attendance data is saved in CSV format

## 📸 Face Capture Guidelines

For best results when capturing student photos:
- Ensure good lighting conditions
- Face should be clearly visible
- Capture from different angles (slightly left, center, slightly right)
- Maintain consistent distance from camera
- Capture 100-150 images per student for better accuracy

## 🔐 Security Considerations

- Firebase credentials are not included in the repository
- Keep your Firebase service account key secure
- Update login credentials from default values
- Implement proper user authentication for production use
- Regular backup of attendance data is recommended

## 🐛 Troubleshooting

**Camera not working:**
- Check if camera permissions are granted
- Ensure no other application is using the camera

**Face not detected:**
- Improve lighting conditions
- Ensure face is within camera frame
- Check if Haar Cascade file is present

**Firebase connection error:**
- Verify Firebase credentials
- Check internet connection
- Ensure Firebase database rules allow read/write access

**Training errors:**
- Ensure Data folder contains captured images
- Verify image file naming convention: `user.[id].[count].jpg`
- Check if sufficient training data is available

## 📝 Future Enhancements

- [ ] Multi-user role system (Admin, Teacher, Student)
- [ ] Email notifications for attendance reports
- [ ] Mobile application support
- [ ] Advanced analytics and reporting dashboard
- [ ] Integration with learning management systems
- [ ] Support for multiple camera sources
- [ ] Improved face recognition accuracy with deep learning models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Rohan Benny**
- GitHub: [@rohan-benny](https://github.com/rohan-benny)

## 🙏 Acknowledgments

- OpenCV community for excellent computer vision tools
- Firebase for cloud storage solutions
- Python community for extensive libraries and support

## 📞 Support

For support, please open an issue in the GitHub repository or contact the developer.

---

**Note**: This system is designed for educational and small-scale institutional use. For large-scale deployment, consider additional security measures and scalability improvements.
