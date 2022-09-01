
import os
from keras.preprocessing import image
import numpy as np
from deeplearning import graph, model, output_list,output_list1
import cv2


import time



pic='dataset/train/Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot/02e6c80d-c86f-44ca-9d4c-4b100f92a839___RS_GLSp 4631.JPG'
myfile = pic



img = image.load_img(myfile, target_size=(150,150))
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = img/255

with graph.as_default():
    prediction = model.predict(img)
    
    

prediction_flatten = prediction.flatten()
var= (prediction_flatten[0])


max_val_index = np.argmax(prediction_flatten)

acc=(prediction_flatten[max_val_index])
acc=acc*100
print(acc)
result = output_list[max_val_index]
result1 = output_list1[max_val_index]

print (result,result1)


         
        

          
