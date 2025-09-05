import tensorflow as tf
from keras import layers, models
def build_unet(input_shape=(256,256,3)):
    inputs = layers.Input(shape=input_shape)
    c1 = layers.Conv2D(16, 3, activation='relu', padding='same')(inputs)
    c1 = layers.Conv2D(16, 3, activation='relu', padding='same')(c1)
    p1 = layers.MaxPooling2D((2,2))(c1)
    
    outputs = layers.Conv2D(3, 1, activation='softmax')(p1) 
    model = models.Model(inputs=[inputs], outputs=[outputs])
    return model

model = build_unet()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.save('models/segmentation_model.h5')
