# Machine and Deep Learning: Basic ML and DL model from scratch in Python 3

This project is my attempt to understanding and implementing some of the major Machine Learning and Deep Learning models and algorithms.

## Abstract and Disclaimer

I began this project with **two goals**: Use my recently acquired **knowledge on Python 3** on a concrete project and **learn more on Machine and Deep Learning**. I began with only basic Python 3 skills and little to no knowledge of Machine or Deep learning. I decided to go for a **" From Scratch" approach** as I wanted to focus more on **understanding the theory** and math behind those models, rather than "just" spend time on learning how to use popular frameworks such as **TensorFlow or SKlearn**.

That said, don't expect the **best performances or accuracy** in those models. A lot of largely used **complex optimization and features engineering are not implemented/used**. I think it was crucial to understand the basic theory and see what a "basic implementation" can do to understand how each optimization helps the model.

>**Note:** This work is a solo project and I spent at the time only two weeks on it. Each model didn't have more than one or two iterations on it. Keep in my mind this is a student side project, but all the links in the "Ressources and Credits" are way better resources if you are searching to get into Machine or Deep learning.

## How to Setup and Run

### **Step 1** : get a proper **Python 3.x** install.

I included in the "Ressources" directory, a **shell script** that gets a **miniconda python** (current 3.7.4) and install it. But feel free to use any python 3.x install you like. But be aware I only used this one during all this project's development.
`$> sh ./Ressources/Python3_installer.sh install-python`

![install_launch](./Ressources/Screenshots/py_install_1.png)
![install_done](./Ressources/Screenshots/py_install_2.png)

### **Step 2** : Install packages

Few external packages are used in those models :
- **pandas** : Mostly to get data from CSV files
- **numpy**: The main package used to work with data and arrays
- **matplotlib**: Tool to display and plot data and results
- **Colorama**: Just to make things fancy
- **sklearn** : (Optional), Only used in test.py files to see differences between my models and sklearn ones.

> Install using pip : `$> pip install numpy pandas matplotlib sklearn colorama`

### **Step 3** : Run it !

Then simply going to one of the model directories and run it. In general, every model will have :
- **The Model as a class**: Will get the data, be able to be trained, then predict and display results.
- **Dataset**: I developed those models with toy datasets, some workaround could be needed to fit other ones. *(i.e Those models are my understanding and implementation of them, not a tool to be largely used on concrete ML/DL use case on a large scale)*
- **Tools functions**: Few functions or other class relevant for the model to work
- **A *test.py* file**: That get some data, and show how the model reacts to it. Basic steps if you want to play with it are: instantiate the model, then *fit* it, then make him *predict*
![install_done](./Ressources/Screenshots/py_run.png)

>**Note**: Program was built on **macOS Mojave** and I know there is some **workaround to do to run on Linux** as well (mostly for python3 installer)

# Models and Features

## *Machine Learning* : Linear Regression

- **Model:**
For this linear regression, the goal is to use training data to train our model (cf. *Gradient Descent* part below), then predict output *Y* for new input *X* by using our trained *H* function (cf. *Hypothesis* part below)

![General Model](./Ressources/Screenshots/Model.png)

-  **Hypothesis and Prediction:**

As an accurate prediction from the model is our main goal, making a good hypothesis is crucial. The hypothesis refers to the *H* function in the model presented. Training the model will tweak values in it, that will define our hypothesis coefficient, but not the *"form"* of it. For a single feature linear regression, we can assume our prediction will follow a line of the equation :

![ax+b](./Ressources/Screenshots/math/ax+b.gif)

To suit our model we introduce the theta matrix. Theta is the matrix our model will change over iteration while training. And then use its coefficients in the *H* function. We then have

![h_single](./Ressources/Screenshots/math/h_single.gif)

Going further, we will add a theta coefficient for each feature to end with

![h_multi](./Ressources/Screenshots/math/h_multi.gif)

Where X matrix is the value for each feature in one example of our Dataset.
In the future, we will use a vectorized form of ***H***

![h_vec](./Ressources/Screenshots/math/h_vec.gif)

>**Note:** Benchmarking and choosing the good hypothesis in a model is a huge part of its performance. Using **polynomial factors** or more complex ones can greatly **improve accuracy**. I did read a lot toward those, and also the problem of **overfitting** and the ***" bias-variance"*** problem. But didn't implemented them is this project. As I feel like this his something related to a precise model on a precise dataset and **I wanted a more generic model**.

-  **Cost function and Fitting:**

After defining what is our hypothesis, we'll introduce the **Cost Function**. The idea behind it is to quantify the error of our model to be able to train it afterward. And to do that, our cost function will be the **Mean Squared Error** between prediction and real example from the dataset.

![cost](./Ressources/Screenshots/math/cost.gif)

Thus, **fitting** or *"training"* the model will result in trying to modify theta to reach a minimum for the cost function of the model.

-  **Linear Gradient Descent:**

The more features, the higher the dimensions our matrices grow. Thus using a gradient to define *" which way "* values of theta need to go to aim for the needed minimum of our cost function yield good results. Our ***fit*** function will then be defined by

![fit](./Ressources/Screenshots/math/fit.gif)

or the vectorized form :

![fit_vec](./Ressources/Screenshots/math/fit_vec.gif)

>**Note:** We see that alpha and Ncycle will have a big impact on the training process. But they also introduce the problem of under and overfitting. So even if they will be hardcoded values in the test files, playing with them and knowing their relations to the model is key.

- **The Dataset**

For this linear regression, I will be using a toy dataset with spacecraft prices as Y output and a 3 feature input X (Age of the spacecraft, Thrust power, and Covered distance). The model will do three single feature fitting then fit overall features.

- **Single Feature Results**

![SingleVariable LGD](./Ressources/Screenshots/Single_LGD_run.png)
![SingleVariable LGD Plot](./Ressources/Screenshots/Single_LGD_plot.png)

- **Multiple Feature Results**

![MultiVariable LGD](./Ressources/Screenshots/Multi_LGD_run.png)
![MultiVariable LGD Plot](./Ressources/Screenshots/Multi_LGD_plot.png)

## *Machine Learning* : Logistic Regression (for Classification problems)

- **Logistic vs Linear Regression: Model and Design differences:**

The main difference between logistic and linear regression is in the use case we want to solve. Logistic regression will be used for what is called *"Classification"* problem. Here the output is a 1/0 value (True/False). The goal of the training process is to define a decision boundary, a hypothetical bound between clusters of "True" values and "False" ones. One example, widely used in the documentation, is the determination of the benign/malignant status of a tumor regarding different *"features"*. The model is close to linear regression but the hypothesis and cost function will change to match the boolean nature of our output. The goal as seen in the image below is to better fit the model than a linear regression for a True/False output

![Model comparison](./Ressources/Screenshots/LogRegModel.png)

- **Logistic vs Linear Regression: Math and Implementation differences:**

The first difference between those models is the use of the **sigmoid** function. The function output is mostly real close to one or zero by nature, thus suiting our model quite well. The hypothesis used in the logistic regression model will then be the sigmoid of the linear regression hypothesis

![Sigmoid](./Ressources/Screenshots/math/sigmoid.gif)

Then we assume that our output is the probability for the model that a given example is 1 or 0. For example, a 0.7 output means that the probability for the input to be 1 is 70%.

The decision boundary is the line that separates the area where y=0 and where y=1. It is created by our hypothesis function. An example would be :

![Decision](./Ressources/Screenshots/math/decision.gif)

We cannot use the same cost function that we use for linear regression because the Logistic Function will cause the output to be wavy, causing many local optima. In other words, it will not be a convex function. Instead, our cost function for logistic regression looks like:

![Cost function](./Ressources/Screenshots/math/cost_log.gif)

With all that, we get the same model for gradient descent, but with the new cost and hypothesis functions.

-  **Result without regularization:**

![LogReg](./Ressources/Screenshots/LogReg.png)
![LogRegPlot](./Ressources/Screenshots/LogRegPlot.png)

-  **Result with regularization:**

![RegLogRed](./Ressources/Screenshots/Regularized_LogReg.png)
![RegLogRegPlot](./Ressources/Screenshots/Regularized_LogRegPlot.png)

> **Regularization**: For both linear and logistic regression we can handle part of the overfitting problem by using regularization. I only implemented it on my Logistic Regression model but can be done for linear regression in the same way. The goal is to reduce overfitting but keep all the features. Regularization works well when we have a lot of slightly useful features. It reduces the magnitude of thetas parameters in the computation. Overfitting introduces the problem of balance needed between bias and variance. We want our model to fit well the train data, but not a the cost at too much variance in the prediction due to high polynomial order or quadratic function.

## *Machine Learning* : Decision tree (for Labels classification)

- **Decision tree definition**

A decision tree classifier takes a dataset and builds a tree by choosing what question to ask to split labels in the remaining dataset. The dataset will contain several examples with their corresponding labels and *value* for each chosen features. The goal of the model is to find boolean questions to split the dataset and ultimately end up with * leaves* containing only one type of label. Then while asking the same sequence of questions to a new entry, ending to a leaf and thus predict the label of the entry. The model will use several criteria and math equations to quantify label mixing and how a question is relevant at a given time to split the dataset.

![MultiVariable LGD Plot](./Ressources/Screenshots/DecTree.png)

-  **Pros and Cons of Decision tree classifier**
    - ***Pros***
        -  This is a *"White Box"* model, where you can show, see, and easily understand how the trained model makes predictions
        - Works with numerical and categorical features
        - Requires little data processing
        - No assumption needed about the shape of the data
        - *Automatic* feature selection: the more important the feature, the more it will influence the model.
    - ***Cons***
        - More complexity on the model
        - It tends to overfit, can be mitigated by limiting tree depth
        - Takes time to build, but fast at predicting

- **Gini impurity**

Gini impurity quantifies the *"purity"* of a remaining child dataset, i.e. our the labels are mixed in it. The goal will be to reduce this along the tree and aim with leaf with 0 Gini impurity (i.e. only one label in the leaf). It is defined by the ratio of occurrence of a given label in the dataset.

![gini](./Ressources/Screenshots/math/gini.gif)

> **Note:** Shanon entropy is another criterion that can be used to quantify the information within a dataset. My model can use Shanon entropy or Gini impurity but used Gini by default.

- **Information Gain**

Information Gain is the main metric used to build the tree. It quantifies how much a given question split the dataset reducing overall Gini impurity in the child branches. It is defined by the formula

![info_gain](./Ressources/Screenshots/math/info_gain.gif)

- **Node vs Leaf**

After each new question and splitting the remaining data into branches (true or false), we can be in one of the following cases: Node or Leaf. If no possible question can further split our data down the tree, we have a leaf, whether Gini impurity is 0 or not. Note that if we have a leaf where Gini is not 0, the dataset contains data with different labels with the same feature values (i.e. we need more or more accurate features), or the fit is not enough accurate. If a remaining possible question gets an information gain greater than 0, then we can still split the dataset, and we have a new node.

- **Fitting and Predicting**

Regarding what I explained before, we end up building the tree by finding the best question, then splitting the data into the initial recursion over it. You calculate the information gain of each possible question then take the best one to split the data. We then keep the node with a reference to the question, his true and false branch. If the best possible info gain is zero, this is a leaf. After that, we call the function again on the true and false branch until we reach on leaves or set maximum depth.

Prediction is then also done recursively. You start at the root node then ask the tree sequence of questions, going from node to node regarding the answer to each question. If the answer is true, you follow the reference to the true branch, else the false branch.

- **The Dataset**

For this example, I will use the iris dataset provided by Sckikit-learn. It is a 150 dataset of three iris type with four features: Sepal and Petal length and width. More on the official page [Scikit dataset info](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)

- **Results**

![Model launch](./Ressources/Screenshots/dtc_run.png)

Printing the Tree (True branch from the root)

![DecTreePrint](./Ressources/Screenshots/DecTreePrint.png)

Prediction on the test set (True branch from the root)

![DecTreePredict](./Ressources/Screenshots/DecTreeClassify.png)

- **Decision tree regression**

I might implement a Decision tree regression in the future. The goal is to use a decision tree to better fit the dataset than a linear regression by clustering input producing a *"staircase"* pattern. This is achieved by grouping data with similar output, thus setting thresholds for the three questions, and assigning the mean output to data under a given threshold.

![DecTreeRegression](./Ressources/Screenshots/DecTreeRegression.png)

## *Deep Learning*: Neural Network

**Work in Progress** I will update this section when my Multilayer Perceptron model will reach v1.0.

![MultilayerPerceptron](./Ressources/Screenshots/MultilayerPerceptron.png)

## What's Next?

I did have a **great time** getting into Machine and Deep Learning by doing this project. I know there is still **a lot to discover and implement** to improve my skill, knowledge, and understanding of the subject. Thus I will probably **keep spending some time on it**, mostly toward **implementing a neural network** with the same "from scratch' mentality.

After implementing a neural network, I think I'll spend some time on **increasing accuracy and optimizing my models**. And try to learn **issues residing in those "basic" model** and finding **ways to improve them**, like with *regularization*. And the last step would be **to generalized to any type of inputs** to be able to use them more as a tool for any dataset. I also want to spend some time on all the concepts behind **Feature Engineering** as I think choosing the good dataset, and the good feature is a **key component of machine/deep learning**.

## Ressources and Credits

I relied on a lot of really helpful resources to achieve this.
- **42AI association**: Association working toward a lot of ML and DL cool stuff @42 Paris, they provide nice BootCamps and resources to get in AI and Python in general.
- **Coursera/Machine Learning course offered by Stanford University** : [Link here](https://www.coursera.org/learn/machine-learning). Real great "theory focused" machine and deep learning course
- **Python Official Doc** : [Python.org](https://www.python.org/) Really clear documentation about python and packages
- **SKlearn documentation** : [Website](https://scikit-learn.org/stable/). Cool ML/DL Framework with good documentation
- **3Blue1Brown** : [YouTube Channel](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) Great playlist upon Neural Network Gradient Descent

## About Me

My name is **Nicolas** and I'm a curious 25 y/o **french engineer**. I **graduated in 2017** as an aeronautics engineer from **ESTACA** with the *"Avionics and Flight commands"* specialty. As I though **software development** was also a key behind engineering to **push technologies** in a lot of fields, I integrated **42** in Paris for now 1.5 years to get some **C/C++ and Python skills**.

## Update

**Last Update** of this repository and README.md was made on 02/11/2020
