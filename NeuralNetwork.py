import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


def getTrainingData():
    data = []
    labels = []
    with open("./TrainingFiles/MaterialEntrenamiento.txt") as f:
        content = f.read().splitlines()
    for line in content:
        data.append(line[:-1])
        labels.append(int(line[-1:]))
    return data, labels


def dataToListOfLists(data):
    listOfLists = []
    for line in data:
        list = []
        for char in line:
            list.append(int(char))
        listOfLists.append(list)
    return listOfLists


def main():
    training_data, training_labels = getTrainingData()
    training_data = dataToListOfLists(training_data)
    data = np.array(training_data)
    labels = np.array(training_labels)
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(24, input_dim=42, activation='relu'))
    model.add(tf.keras.layers.Dense(7, activation='softmax'))

    model.compile(optimizer='adam',  # Para medir la exactitud de la red
                  # Para actualizar el modelo basado en los datos que ve y su loss function
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=['accuracy'])  # Para monitorear los training y testing steps

    model.fit(data.reshape(-1, 42), labels, epochs=10)  # Entrena la red

    # Se compara que tan buenos son los resultados
    test_loss, test_acc = model.evaluate(data,  labels, verbose=2)

    # La diferencia entre el % de training y el de testing es overfitting; cuando aprende cosas que no son utiles cuando ve cosas nuevas
    print('\nTest accuracy:', test_acc)


if __name__ == "__main__":
    main()
