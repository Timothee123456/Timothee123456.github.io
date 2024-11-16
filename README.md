# Uploading Your Module to PyPI

This guide will walk you through the process of uploading your Python module to the Python Package Index (PyPI). Follow these steps to ensure a smooth upload and testing experience.

## Creating the files
### Creating the package files
You will now add files that are used to prepare the project for distribution. When you’re done, the project structure will look like this:
```
YOUR_MODULE_NAME/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── YOUR_MODULE_NAME
│       ├── __init__.py
│       └── YOUR_MODULE_NAME.py
└── tests/
```
Replace YOUR_MODULE_NAME with the name of your module.

### Creating Project.toml
Open `pyproject.toml and enter the following content.
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "YOUR_MODULE_NAME"
version = "0.0.1"
authors = [
  { name="Timothee" },
]
description = "YOUR_DESCRIPTION"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
```
Replace YOUR_MODULE_NAME with the name of your module and YOUR_DESCRIPTION with a small discription you would like to add.

### Creating README.md
Open `README.md` and enter the following content. You can customize this if you’d like.
```
# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```

### Creating a LICENSE
Open `README.md` and enter the following MIT licence.
```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Uploading the files to PyPi
### Step 1: Navigate to Your Module Directory
Open your terminal and change to the directory where your module is located. Replace YOUR_MODULE_NAME with the actual name of your module.
```bash
cd Python/modules/YOUR_MODULE_NAME
```

### Step 2: Build Your Package
Use the following command to build your package. This will create a distribution package in the dist directory.
```bash
python3 -m build
```

### Step 3: Upload to TestPyPI
Next, upload your package to TestPyPI for testing purposes. This step ensures that everything works correctly before you publish it to the main PyPI repository.
```bash
python3 -m twine upload --repository testpypi dist/*
```

### Step 4: Download Your Module
Visit TestPyPI and search for your module. Once you find it, you can **copy the installation command provided on the page**.

### Step 5: Test Your Package Installation
Open a new terminal window or tab and **run the following command** to install your package from TestPyPI:

Replace YOUR_MODULE_NAME with the name of your module.
### Step 6: Confirm Installation
Once installed, **test your module** to ensure everything is functioning as expected. You can do this by importing it in a Python shell or running any scripts that utilize it.

Feel free to reach out if you have any questions or need further assistance! Happy coding!
