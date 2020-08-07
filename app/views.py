import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

#importing tensorflow libelary

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as Image


# Create your views here.
def home(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        try:
            folder = 'media/images/'
            image = request.Files['cd']
            print('image name is: ',image.name)

            file_name = str(image.name)
            fs = FileSystemStorage(location = folder)
            name = fs.save(image.name, image)

            media_path = folder + {}
            file_path = os.path.join(media_path).format(name)
            print('the file path is ',file_path)

            #Loading the model
            model = load_model('fruits.h5')
            image = Image.load_img(file_path, target_size= (64,64))
            image = Image.img_to_array(image)
            image = np.expand_dims(image, axis = 0)
            print()


        except Exception as e:
            print('errir is', e )

