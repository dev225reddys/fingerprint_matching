
# Python Criminal Identification System
Fingerprint recognition with SKimage and OpenCV

####  NOTE
Change 'rdir' location to current Root directory by replacing Text inside `rdir` variable. 

Link for Ref: 
https://www.learnopencv.com/install-opencv-3-and-dlib-on-windows-python-only/

Requirements:
- NumPy
- SKimage(scikit-image)
- OpenCV2
- Anaconda 3.7

Configuration with Anaconda 3.7
Step 1: 
	Install Anaconda (a python distribution)
	Download and install Anaconda 64-bit version from https://www.continuum.io/downloads.
	It is advised to install Anaconda for Python 3.
	While installing Anaconda make sure that you check both options:

Add Anaconda to my PATH environment variable
Register Anaconda as my default Python

Step 2 : Create Virtual Environment
Open the command prompt and execute the following command.

	conda create --name opencv-env python=3.6

Step 3 : Install OpenCV

3.1 Activate the environment

# See how the (opencv-env) appears before the prompt after this command. 
activate opencv-env

3.2. Install OpenCV and other important packages
Continuing from the above prompt, execute the following commands

	pip install numpy scipy matplotlib scikit-learn jupyter
	pip install opencv-contrib-python
	

To install Dlib:
	conda install -c conda-forge dlib

For PIL Installation:
	conda install -c anaconda PIL

To install SKimage
	conda install -c anaconda scikit-image

3.3. Test your installation
Open the python prompt on the command line by typing python on the command prompt

	import cv2
	cv2.__version__
	import dlib
	dlib.__version_

Installation of Required Libraries:
- to Install Scipy/Numpy w.r.to OS and Distros follow below link:
	https://scipy.org/install.html
- For Scikit
	http://scikit-image.org/docs/dev/install.html
- For OpenCV2
	in Windows:
		https://docs.opencv.org/3.3.1/d5/de5/tutorial_py_setup_in_windows.html
	in Linux/Ubuntu:
		sudo apt-get install opencv
-DLib with Anaconda
	conda install -c conda-forge dlib

Works by extracting minutiae points using harris corner detection.

Uses SIFT (ORB) go get formal descriptors around the keypoints with brute-force hamming distance and then analyzes the returned matches using thresholds.

Configuration:
Change os.chdir location to the installed location from run.py file.
Line:805

Usage:

1. Execute run.py
2. GUI will be provided with Either admin or User login.
3. to input fingerprints login with User Credentials and select `Input FP` 	   option and select fp through GUI.
4. After processing All fingerprints from Database, Results will be shown in 	GUI. 
