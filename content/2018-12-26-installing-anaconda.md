Title: How to Install Anaconda
Date: 2018-12-26 2:30 PM
Category: Python  

![Minions Meme](/images/2018-12-26/minions-meme.jpg){:width='500px'}
## What is Anaconda?
A open-source distribution of Python that simplifies package management. It
comes with applications such as Jupyter Notebook, the Conda environment manager,
and Pip for package installation and management.  

Anaconda also comes with hundreds of Python packages such as matplotlib, NumPy,
and scikit-learn.

It eliminates the need to install common applications separately and will make
installing Python on your computer much easier.  

#### Download & Installation  
[Download Anaconda](https://www.anaconda.com/). I downloaded the Python 3.7
version for 64-Bit Graphical Installer. If you're using Windows, type this in
the command prompt to see your version of Windows:  
```
cmd> wmic os get osarchitecture
```    
While installing, check the box that will "Add Anaconda to my PATH environment
variable". The message says this is not recommended but we check it anyway. It
will save us the step of setting our PATH manually. If you have a previous
version of Python installed, checking this will supersede your previous
installation.  

![Add Anaconda to Path](/images/2018-12-26/anaconda-install-screen.PNG)

The installation process might take some time. It took about 30 minutes on my
machine.  

#### Check your installation  
Open a new command prompt and type the following:
```
cmd> where python
```
The output should point to where the python.exe file where Anaconda was
installed.

```
cmd> python
```
This will open up the Python interactive shell.  

Happy developing!
