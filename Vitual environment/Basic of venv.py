# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

# **** Creating a Virtual Environment ****
# Python has the built-in venv module for creating virtual environments.
 # Code = python -m venv myfirstproject



# **** Activate Virtual Environment ****
# To use the virtual environment, you have to activate it with this command:
# Code = myfirstproject\Scripts\activate


# **** Install Packages ****
# Once your virtual environment is activated, you can install packages in it, using pip.
# Code =  pip install cowsay


# **** Deactivate Virtual Environment ****
# To deactivate the virtual environment use this command
 # Code = deactivate



#  **** Delete Virtual Environment ****
# Another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted.
# Code = rmdir /s /q myfirstproject