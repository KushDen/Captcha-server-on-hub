from PIL import Image
from tensorflow import keras
import numpy as np
from tensorflow.keras import backend as K

characters = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

def encode_to_word(txt):
    dig_lst = []
    for index, idx in enumerate(txt):
        try:
            dig_lst.append(characters[idx])
        except:
            print(idx)
        
    return dig_lst

def show_result(image):
    
    image = image.resize((256, 64))
    img = np.array(image)*255
    for i in range(0, 19):
        for j in range(197, 256):
            img[i][j] = 0
    for i in range(19,21):
        for j in range(226, 228):
            img[i][j] = 0
    for i in range(19,21):
        for j in range(218, 220):
            img[i][j] = 0
    img = img.reshape(64, 256, 1)
    img = img/255
    image = img.reshape(1, 64, 256, 1)

    new_model = keras.models.load_model("modelForYandexCPU.h5", compile=False)
    #new_model.load_weights('actModelYandex.hdf5')
    
    #prediction = new_model.predict(image)

    #out = K.get_value(K.ctc_decode(prediction, input_length=np.ones(prediction.shape[0])*prediction.shape[1],
    #                         greedy=True)[0][0])
    
    #out_best = list(filter(lambda x : x != -1, out[0]))
    #K.clear_session()

    return "good" #''.join(encode_to_word(out_best))
