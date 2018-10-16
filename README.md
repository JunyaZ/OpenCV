# OpenCV
Configure a virtual environment with OpenCV
Goal
Use the conda package manager to configure an Anaconda virtual environment with OpenCV.

Background
The Python installations on our lab computers don’t support OpenCV. We’ll add a virtual environment and install it.

Procedure
1.	Open an Anaconda command window. Open a Python shell and import cv. You’ll probably get an error message. Exit the shell.
2.	OpenCV is not available in the default Anaconda distribution. So you’ll have to add a “channel.” Type conda config --add channels conda-forge (that’s a double-dash before the word “add”). You can find out more about conda-forge at conda-forge.org.
3.	Now create your virtual environment. You can name it anything you want but I suggest csc745. Type conda create --name csc745 (again, a double dash). Conda will ask you whether to proceed; type ‘y’. This will create an environment using the same version of Python as in your base environment. You can specify a different version by adding, for example, python=2.7 after the name of the environment.
4.	Activate your environment: activate csc745
5.	Install OpenCV: conda install opencv
6.	Check your installation; open a python shell and import cv2. If the import is successful, you should be able to use OpenCV in your programs.

