# Machine Learning Education Projects

* ## Image Captioning Problem

### This repo comprises the steps in order to implement a Machine Learning model which writes a caption describing an image given. It delves into the Data Science, ETL and Machine Learning modeling to go through a relatively massive project locally. 
### model based on [Image Captioning with Keras](https://towardsdatascience.com/image-captioning-with-keras-teaching-computers-to-describe-pictures-c88a46a311b8)
### All data is acquired from [Common Objects in Context website](https://cocodataset.org/#download)

### I recommend using the Anaconda distro, that way you simply can take the [env file](env.yml) to replicate the conditions with which I implemented this project. Once you have Anaconda Installed, run in terminal this command: ```conda env create -f env.yml``` and activate it with ```conda activate tf ```

### First, go through the [Data Exploration](data_exploration.ipynb), where data collection, data exploration and data trasformations happen. As you might imagine [or already know], getting to know your data and making it strategically useful are fundamental steps for any Machine Learning project.

### I'm using an Nvidia GPU, so, the easiest way to get that up and running with TensorFlow 2.3 and Keras is to follow these steps by [Millan Sanchez](https://millansanchez.medium.com/install-tensorflow-2-with-gpu-support-dec-2020-for-windows-10-using-conda-e4c0d838d497). Otherwise, do everything on CPU, but it will take longer.
