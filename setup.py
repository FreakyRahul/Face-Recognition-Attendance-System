import cx_Freeze
import sys
import os

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r"C:\Users\RAHUL SHARMA\AppData\Local\Programs\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\RAHUL SHARMA\AppData\Local\Programs\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face Recognition.py", base=base, icon="face-scan.ico")]

cx_Freeze.setup(
    name = "Facial Recoginition Software",
    options = {"build_exe": {"packages":["tkinter","os"],"include_files":["face-scan.ico","tcl86t.dll","tk86t.dll","Images",'Data','Attendance_report','Database','haarcascade_frontalface_default.xml','Classifier.xml']}},
    version = "1.0",
    description = "Face Recognition Attendance System | Developed By Rahul Sharma",
    executables = executables
    )

