
import tensorflow as tf
from keras.models import load_model
#global graph, model, output_list
import keras
graph = tf.get_default_graph()
#(graph)
model = keras.models.load_model('models/newNeu_model50e.h5')

output_dict = {
               '-Gray leaf spot[Corn leaf]':'Gray leaf spot[Corn leaf]' ,
               '-Common Rust[Corn leaf]': '-Common Rust[Corn leaf]',
               '-No disease affected [Healthy Corn leaf]':'-No disease affected [Healthy Corn leaf]',
               '-Northern leaf blight[Corn leaf]':'-Northern leaf blight[Corn leaf]',
               '-Black rot[Grape leaf]':'-Black rot[Grape leaf]',
               '-Black measles [Grape leaf]':'-Black measles [Grape leaf]',
               '-No disease affected [Healthy Grape leaf]':'-No disease affected [Healthy Grape leaf]' ,
               '-Leaf blight [Grape leaf]':'-Leaf blight [Grape leaf]',
               '-Leaf rust [Wheat leaf]':'-Leaf rust [Wheat leaf]' ,
               '-Bacterial spot[Bell pepper leaf]': '-Bacterial spot[Bell pepper leaf]',
               '-No disease detected [Healthy Bell pepper leaf]':'-No disease detected [Healthy Bell pepper leaf]' ,
               '-Early blight [Potato leaf]':'-Early blight [Potato leaf]' ,
               '-No disease detected [Healthy Potato leaf]': '-No disease detected [Healthy Potato leaf]' ,
               '-Late blight[Potato leaf]':'-Late blight[Potato leaf]' ,
               '-Powdery mildew[Wheat leaf]':'-Powdery mildew[Wheat leaf]' ,
               '-Septoria tritici blotch[Wheat leaf]':'-Septoria tritici blotch[Wheat leaf]' ,
               '-Soilborne mosaic [Wheat leaf] ':'-Soilborne mosaic [Wheat leaf] ' ,
               '-Stangonospora nodorum blotch [ Wheat leaf]':'-Stangonospora nodorum blotch [ Wheat leaf]' ,
               '-Stem rust [Wheat leaf]': '-Stem rust [Wheat leaf]',
               '-Stripe rust[Wheat leaf]':'-Stripe rust[Wheat leaf]' ,
               '-Bacterial spot [Tomato leaf]':'-Bacterial spot [Tomato leaf]' ,
               '-Early blight [Tomato leaf]':'-Early blight [Tomato leaf]' ,
               'No disease affect [Tomato leaf]':'No disease affect [Tomato leaf]',
               'Late blight [Tomato leaf]':'Late blight [Tomato leaf]',
               'Leaf mold [Tomato leaf]': 'Leaf mold [Tomato leaf]',
               'Septoria leaf spot [Tomato leaf]':'Septoria leaf spot [Tomato leaf]',
               'Spider mites [Tomato leaf]':'Spider mites [Tomato leaf]',
               'Target spot[Tomato leaf]':'Target spot[Tomato leaf]',
               'Mosaic virus [Tomato leaf]':'Mosaic virus [Tomato leaf]',
               'Yellow leaf curl [Tomato leaf]':'Yellow leaf curl [Tomato leaf]'
              
               }

output_dict1 = {'Azoxystrobin':'-Gray leaf spot[Corn leaf]',
               'Mancozeb': '-Common Rust[Corn leaf]',
               'None': 'No disease affected [Healthy Corn leaf]',
               'Delaro':'Northern leaf blight[Corn leaf]',
               'Ziram ':'-Black rot[Grape leaf]',
               'Fenhexamid':'-Black measles [Grape leaf]' ,
               'None': '-No disease affected [Healthy Grape leaf]',
               'Bordeaux mixture (1.0%)': '-Leaf blight [Grape leaf]',
               'Triazoles and Strobilurins': '-Leaf rust [Wheat leaf]',
               'Actigard ':'-Bacterial spot[Bell pepper leaf]',
               'None':'-No disease detected [Healthy Bell pepper leaf]',
               'Mancozeb and Chlorothalonil':'-Early blight [Potato leaf]' ,
               'None': '-No disease detected [Healthy Potato leaf]',
               'Penncozeb, Manzate and Dithane': '-Late blight[Potato leaf]',
               'Potassium bicarbonate':'-Powdery mildew[Wheat leaf]',
               'Chlorothalonil, Copper': '-Septoria tritici blotch[Wheat leaf]',
               'carboxin + ipconazole Rancona V100 ': '-Soilborne mosaic [Wheat leaf] ',
               'carboxin + ipconazole Rancona V100': '-Stangonospora nodorum blotch [ Wheat leaf]',
               'Foilar pesticide': '-Stem rust [Wheat leaf]',
               'carboxin + ipconazole Rancona V100': '-Stripe rust[Wheat leaf]',
               'cannot be cured':'-Bacterial spot [Tomato leaf]' ,
               'Bonide Liquid Copper pesticide': '-Early blight [Tomato leaf]',
               'None': 'No disease affect [Tomato leaf]',
               'Manzate and Dithane': 'Late blight [Tomato leaf]',
               'Chlorothalonil ': 'Leaf mold [Tomato leaf]',
               'Benomyl': 'Septoria leaf spot [Tomato leaf]',
               'Horticultural oils': 'Spider mites [Tomato leaf]',
               'Chlorothalonil': 'Target spot[Tomato leaf]',
               'Remove all infected plants': 'Mosaic virus [Tomato leaf]',
               'Imidacloprid': 'Yellow leaf curl [Tomato leaf]'
               }


output_list = list(output_dict.keys())
output_list1 = list(output_dict1.keys())

