import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from app.models import ImagePath
from lables import lable
#importing tensorflow libelary

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as Image
import numpy as np

# Create your views here.
def home(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        try:
            folder = 'media/images/'
            image = request.FILES['cd']
            print('image name is: ',image.name)

            file_name = str(image.name)
            fs = FileSystemStorage(location = folder)
            name = fs.save(image.name, image)

            media_path = folder + "{}"
            file_path = os.path.join(media_path).format(name)
            print('the file path is ',file_path)

            #Loading the model
            print('model is loding............')
            model = tf.keras.models.load_model('fruits.h5')
            print('model is loaded! ')
            image = Image.load_img(file_path, target_size= (32,32))
            image = Image.img_to_array(image)
            image = np.expand_dims(image, axis = 0)

            #Prediction

            result = model.predict(image)
            print(result)
            print(np.argmax(result))
            img_path = ImagePath()
            img_path.path = file_path

            return render(request, 'results.html',  {'image_source': img_path})

        except Exception as e:
            print('error is', e )

    else:
        return render(request, 'index.html')