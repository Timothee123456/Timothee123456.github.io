# Uploading Your Module to PyPI

This guide will walk you through the process of uploading your Python module to the Python Package Index (PyPI). Follow these steps to ensure a smooth upload and testing experience.

## Step-by-Step Instructions
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
