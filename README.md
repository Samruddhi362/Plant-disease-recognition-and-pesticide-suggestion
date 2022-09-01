# Plant-disease-recognition-and-pesticide-suggestion
A farming application helps to recognize the plant disease and suggest the suitable pesticide for the crop.
PROBLEM STATEMENT

Solving a problem of by proposing a web-based application for automatic system for leaf diseases detection through the developed system.  An expert must monitor the leaves of the plant very often. This may cost high when considering large number of farms. In some of the villages in India, farmers do not have proper facilities. The consulting experts are time consuming and cost will be high. In this type of conditions, the suggested technique seems to be beneficial for the farmers.     

OBJECTIVES
		
The main objective of the system is to provide a reliable security system which can predict the disease the plant has got and predict the fertilizer for it.

•	The objective of this study is to detect plant diseases by an automated system based on image processing.
•	We use image processing algorithms to detect diseases on plants.
•	To recognize abnormalities that occur on plants in their Greenhouse or Natural Environment  
•	To suggest fertilizer based on diseases
•	To Classify the disease using CNN Classifier and suggest pesticide.

 Software specification
	
1)	Tools - Python IDE
2)	Programming Language - Python
3)	Software Version - Python 3.7

The proposed system starts with Data collection of leaves through some steps and then finally detect the diseases from image. The steps involved are as follows:-
•	Data Collection
•	Image Pre-processing
•	Feature Extraction
•	Classification

Dataset

Plant dataset consists of around 1503 images of different plant leaves which are divided into various classes. The dataset consists of 5-6 types of plant species and various types of plant diseases. The dataset contains both healthy and diseased crop images. Each class consists of three fields i.e. name of the plant and name of the diseases and Fertilizer for plant. Each of the images are resized and segmented for preprocessing and further classification.

Pre-processing

Pre-processing is a very important step in CNN as the images in the dataset may have some inconsistency which may affect the accuracy of the system. The images in the dataset have noise and non-uniform lighting which needs to be rectified in this step. We do so by applying segmentation on the images to get rid of uneven backgrounds. Through segmentation we extract the relevant part of the images which in this case are the image of leaves. Hence, after segmentation we have the images of leaves with black background. Now to rectify the non-uniform lighting we convert the images to grayscale images and send it for further processing.






Feature Extraction

As we get the greyscale images from the previous step, we take the image and convert it into reduced variables. Basically, each pixel of the images is taken and are converted into matrix for performing convolutions. The process runs across all the pixels where the convolution matrix is simply multiplied with each pixel matrix. Also, we mention the number of strides which refers to the shifting of pixel matrix. Once all the values are obtained by multiplication, we then perform Pooling on the matrix. Here we are using Max pooling for our system for better accuracy and extraction of features .Both the process i.e. Convolution and Pooling form an epoch. Now to improve the system accuracy we perform a few epochs, but this may cause to increase in the number of parameters. Hence, through following these steps we get to extract unique features from the images. These unique features are then sent for further processes.

	
	Classification

Detection of disease is performed in three steps i.e. detection of the type of crop and detection of type of disease and at last prediction of fertilizer. This takes place with the help of Convolutional Neural Network. We will be using Transfer Learning for building the Model. It is a technique where the pertained models are used to create the current models. Classification also acts as fully connected classifiers which are formed using various learnings done by the model. We do the following by flattening of images which convert the pooled images to single dimension vectors. Once the images are converted to the vectors it gets quite easy to classify the images. Through the trained model we get certain numerical values with respect to various classes. When the leaf is healthy and there is no classification the results are shown as healthy and when there is a disease which when grey scaled shows black spots, it classifies them so they are shown as which disease they are and the confidence of the classification. Classification takes place between two numerical arrays. If the numerical arrays match, then it is a healthy or a diseased leaf, depending upon the dataset provided. Classification is a simple but relevant procedure which gives a proper result and is used in plant disease detection. 


 
ALGORITHM

Convolutional Neural Networks
CNN or the convolutional neural network (CNN) is a class of deep learning neural networks. In short think of CNN as a machine learning algorithm that can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image, and be able to differentiate one from the other.

CNN works by extracting features from the images. Any CNN consists of the following:

The input layer which is a grayscale image
•	The Output layer which is a binary or multi-class labels
•	Hidden layers consisting of convolution layers, ReLU (rectified linear unit) layers, the pooling layers, and a fully connected Neural Network

It is very important to understand that ANN or Artificial Neural Networks, made up of multiple neurons is not capable of extracting features from the image. This is where a combination of convolution and pooling layers comes into the picture. Similarly, the convolution and pooling layers can’t perform classification hence we need a fully connected Neural Network. Before we jump into the concepts further let’s try and understand these individual segments separately.

The role of CNN is to reduce the images into a form that is easier to process, without losing features critical towards a good prediction. This is important when we need to make the algorithm scalable to massive datasets.

The challenge with images having multiple color channels is that we have huge volumes of data to work with which makes the process computationally intensive. In other worlds think of it like a complicated process where the Neural Network or any machine learning algorithm has to work with three different data (R-G-B values in this case) to extract features of the images and classify them into their appropriate categories
CNN goes through different techniques such as: -
•	Convolutional Layer
•	Pooling / Sampling Layer
•	ReLU Layer
•	Fully Connected Layer
Step 1: Convolution Operation
The first building block in our plan of attack is convolution operation. In this step, we will touch on feature detectors, which basically serve as the neural network's filters. We will also discuss feature maps, learning the parameters of such maps, how patterns are detected, the layers of detection, and how the findings are mapped out.
Step 1(b): ReLU Layer:- 
The second part of this step will involve the Rectified Linear Unit or ReLU. We will cover ReLU layers and explore how linearity functions in the context of Convolutional Neural Networks. Not necessary for understanding CNN's, but there's no harm in a quick lesson to improve your skills.

Step 2: Pooling
In this part, we'll cover pooling and will get to understand exactly how it generally works. Our nexus here, however, will be a specific type of pooling; max pooling. We'll cover various approaches, though, including mean (or sum) pooling. This part will end with a demonstration made using a visual interactive tool that will definitely sort the whole concept out for you. 

Step 3: Flattening
This will be a brief breakdown of the flattening process and how we move from pooled to flattened layers when working with Convolutional Neural Networks.

Step 4: Full Connection
In this part, everything that we covered throughout the section will be merged together. By learning this, you'll get to envision a fuller picture of how Convolutional Neural Networks operate and how the "neurons" that are finally produced learn the classification of images.








