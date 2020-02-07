# Machine and Deep Learning: Basic ML and DL model from Scratch in Python3

This project is my attempt of understanding and implementing some of the major Machine Learning and Deep Learning models and algorithm.

## Abstract and Disclaimer

I began this project with **two goals** : Use my recently acquired **knowledge on Python 3** on a concrete project and **learn more on Machine and Deep Learning**. I began with only basic Python 3 skills and little to no knowledge on Machine or Deep learning. I decided to go for a **"From Scratch" approach** as I wanted to focus more on **understanding the theory** and math behind those models, rather thant "just" spend time on learning how to use popular framework such as **TensorFlow or SKlearn**.

That said, don't expect the **best performances or accuracy** in those models. A lots of largely used **complex optimization and features engineering are not implemented/used**. I think it was crucial to understand the basic theory and see what a "basic implementation" can do to understand how each optimization helps the model.

>**Note:** This work is a solo project and I spent at the time only two weeks on it. Each model didn't had more than one or two iterations on it. Keep in my mind this is a student side project, but all the links in the "Ressources and Credits" are way better ressources if you are searching to get into Machine or Deep learning.

## How to Setup and Run

### **Step 1** : get a proper **Python 3.x** install.

I included in the "Ressources" directory, a **shell script** that get a **miniconda python** (current 3.7.4) and install it. But feel free to use any python 3.x install you like. But be aware I only used this one during all this project's developement.
`$> sh ./Ressources/Python3_installer.sh install-python`

![install_launch](./Ressources/Screenshots/py_install_1.png)
![install_done](./Ressources/Screenshots/py_install_2.png)

### **Step 2** : Install packages

Few external packages are used in those models :
- **pandas** : Mostly to get data from csv files
- **numpy** : Main package used to work with data and arrays
- **matplotlib** : Tool to display and plot data and results
- **colorama** : Just to make things fancy
- **sklearn** : (Optional), Only used in test.py files to see differences between my models and sklean ones.

> Install using pip : `$> pip install numpy pandas matplotlib sklearn colorama`

### **Step 3** : Run it !

Then simply going to one of the model directory and run it. In general every model will have :
- **The Model as a class** : Will get the data, be able to be train, the predict and display result.
- **Dataset** : I developped those model with toy dataset, some workaround could be needed to fit other ones. *(i.e Those model are my understanding and implementation of them, not a tool to be largely used on concrete ML/DL use case on a large scale)*
- **Tools functions** : Few functions or other class relevant for the model to work
- **A *test.py* file** : That get some data, and show how the model reacts to it. Basic steps if you want to play with it are : instanciate the model, then *fit* it, then make hime *predict*
![install_done](./Ressources/Screenshots/py_run.png)

>**Note**: Program was built on **macOS Mojave** and I know there is some **workaround to do to run on Linux** as well (mostly for python3 installer)

## Models and Features

### Linear Regression

### Logistic Regression (for Classification problems)

### Decision tree (for Labels classification)

### Neural Network

## What's Next ?

I do had a **great time** getting into Machine and Deep Learning by doing this project. I know there is still **a lot to discover and implement** to improve my skill, knowledge and understanding on the subject. Thus I will probably **keep spending some time on it**, mostly toward **implementing a neural network** with the same "from scratch' mentality.

After implementing a neural network, I think I'll spend some time on **increasing accuracy and optimizing my models**. And try to learn **issues residing in those "basic" model** and finding **ways to improve them**, like with *regularization*. And the last step would be **to generalized to any types of inputs** to be able to use them more as a tool for any dataset. I also want to spend some time on all the concepts behind **Feature Engineering** as I think choosing the good dataset, and the good feature is a **key component of machine/deep learning**.

## Ressources and Credits

I obviously relied on a lot of really helpfull ressources to achieve this.
- **42AI association** : Association working toward a lot of ML and DL cool stuff @42 Paris, they provides nice BootCamps and ressources to get in AI and Python in general.
- **Coursera/Machine Learning course offer by Stanford University** : [Link here](https://www.coursera.org/learn/machine-learning). Real great "theory focused" machine and deep learning course
- **Python Official Doc** : [Python.org](https://www.python.org/) Really clear documentation about python and packages
- **SKlearn documentation** : [Website](https://scikit-learn.org/stable/). Cool ML/DL Framework with good documentation

## About Me

My name is **Nicolas** and I'm a curious 25 y/o **french engineer**. I **graduated on 2017** as an aeronautics engineer from **ESTACA** with the *"Avionics and Flight commands"* speciality. As I though **software developement** was also a key behind engineering to **push technologies** in a lot of fields,I integrated **42** in Paris since now 1.5 year to get some **C/C++ and Python skills**.

## Update

**Last Update** of this repository and README.md was made on 02/07/2020
