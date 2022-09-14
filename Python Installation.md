# Installing Anaconda Distribution
- Use either Anaconda Distribution (full version), or the Mini Conda Distribution (minimized version). Let's install **Mini Conda Distribution** which will give us Jupyter Notebooks, which is enough to code in Python.
- Download the Windows 64 bit(or as per OS) MiniConda3 software from this website: [MiniConda3 Download](https://docs.conda.io/en/latest/miniconda.html)
- It downloads an `.exe` file. Run that file and it runs the installer.
- During installation, it might ask several questions such as:
    - Install for 'Just Me' or for 'Admin' -> Choose the 'Just Me' option
    - Check the radio button which says 'Add Anaconda3 to my PATH environment variable'. (Do this if you are installing Anaconda|MiniConda the first time, even though the installer says its not recommended to do so)
- Once installation is complete, open `Anaconda Prompt (miniconda3)` application from Windows search.
- Type the following command to open the **Jupyter Notebook** environment: `jupyter notebook`. This will open the Jupyter Notebook in `localhost:8888` or `localhost:8889` in the default browser using `C:` drive as the current directory.
- To open Jupyter Notebook in D drive (or any other drive), use the following command: `jupyter notebook --notebook-dir=D:`

> :warning: **Important Note:** MiniConda does not install any additional Python packages. So, we have to manually do a `pip install` whenever we try to work with other libraries.

# No installation options
- There are some online options to code in python notebooks, such as **Google Colab**.
- Google Colab is a popular option for Data Science and Machine Learning applications. The only limitation is that the RAM and Disk Size are limited.