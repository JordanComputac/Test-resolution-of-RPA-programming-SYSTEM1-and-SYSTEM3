
This test is designed to be completed by the UiPath tool, but here it is implemented using Python (free-of-charge) and many libraries, including Selenium for Python, which provides a very useful pack to automate tasks.

Here you can visualize how it's done using only open-source projects.

The detailed process flow can be visualized below:

![image](https://github.com/JordanComputac/teste-sbk/assets/122910793/1a930ea4-b594-410e-a2cb-0db83e1b2f9b)

To have access to the systems that might be automated, visit "https://acme-test.uipath.com/login" and register.

The executed project is set in a venv environment, so when cloning to your repository, also configure your own venv environment.
Install all required libraries; they are listed in "requirements.txt".
Also, when executing the main.py code, make sure to have all directories set up in the ".env" file:

PATH_SYSTEM3="substitute_directory"

CHROMEDRIVER_PATH="substitute_directory"

EMAIL = "substitute_email"
PASSW = "substitute_password"

DATA_PATH = "substitute_directory"
PDF_PATH = "substitute_directory"
IMAGE_PATH = "substitute_directory"

The generated data files in ".csv" format represent the compilation of all the client information gathered from PDFs and System1.
For compact purposes, the downloaded files are excluded as soon as the information is stored in a safe place (.csv files), which reduces the need for memory for such archives.


![image](https://github.com/JordanComputac/teste-sbk/assets/122910793/9271c990-51f2-4f23-a78a-4deb1f73cd0e)


The last observation is that the automation of the desktop app System3 is not fully implemented due to a lack of time. It's done using pywinauto and deals with System3 to look for clients that weren't found in System1.
