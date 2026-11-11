from functools import lru_cache
import numpy as np
import tensorflow as tf

IMG_SIZE = (224, 224)

@lru_cache(maxsize=2)
def load_model(path: str):
    return tf.keras.models.load_model(path)

def predict_image(model, pil_image, class_names):
    image = pil_image.convert("RGB").resize(IMG_SIZE)
    array = np.asarray(image, dtype=np.float32) / 255.0
    probs = model.predict(np.expand_dims(array, axis=0), verbose=0)[0]
    order = np.argsort(probs)[::-1][:3]
    top3 = [(class_names[int(i)], float(probs[i])) for i in order]
    return top3[0][0], top3[0][1], top3
