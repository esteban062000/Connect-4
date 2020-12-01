import tensorflow as tf
from tensorflow import keras
import Constants
import matplotlib.pyplot as plt
import numpy as np
import os
import logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel(logging.ERROR)
# tf.autograph.set_verbosity(1)


class RNA:
    def __init__(self):
        training_data, training_labels = self.getTrainingData()
        training_data = self.dataToListOfLists(training_data)
        data = np.array(training_data)
        labels = np.array(training_labels)
        self.model = self.createNetwork()
        self.trainNetwork(data, labels)

    def getTrainingData(self):

        data = []
        labels = []
        with open("./TrainingFiles/MaterialEntrenamiento.txt") as f:
            content = f.read().splitlines()
        for line in content:
            data.append(line[:-1])
            labels.append(int(line[-1:]))
        return data, labels

    def dataToListOfLists(self, data):
        listOfLists = []
        for line in data:
            list = []
            for char in line:
                list.append(int(char))
            listOfLists.append(list)
        return listOfLists

    def createNetwork(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(
            24, input_dim=42, activation='relu'))
        model.add(tf.keras.layers.Dense(10, activation='relu'))
        model.add(tf.keras.layers.Dense(7, activation='softmax'))

        model.compile(optimizer='adam',  # Para medir la exactitud de la red
                      # Para actualizar el modelo basado en los datos que ve y su loss function
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(
                          from_logits=True),
                      metrics=['accuracy'])  # Para monitorear los training y testing steps
        return model

    def trainNetwork(self, data, labels):
        self.model.fit(data.reshape(-1, 42), labels,
                       epochs=10)  # Entrena la red

        # Se compara que tan buenos son los resultados
        test_loss, test_acc = self.model.evaluate(data,  labels, verbose=2)

        # La diferencia entre el % de training y el de testing es overfitting; cuando aprende cosas que no son utiles cuando ve cosas nuevas
        print('\nTest accuracy:', test_acc)

    def gameboardToNumpyArray(self, gameboard):
        list = []
        for r in range(len(gameboard)):
            for c in range(len(gameboard[r])):
                list.append(int(gameboard[r][c]))
        for i in range(len(list)):
            list[i] = tf.convert_to_tensor(list[i], dtype=tf.int64)
        return np.array(list)

    def predictNextMove(self, gameboard):
        input = self.gameboardToNumpyArray(gameboard)
        probability_model = tf.keras.Sequential([self.model,
                                                 tf.keras.layers.Softmax()])
        input = (np.expand_dims(input, 0))
        output = probability_model.predict(input)
        return output
