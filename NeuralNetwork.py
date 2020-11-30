import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import Constants


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


def createNetwork():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(24, input_dim=42, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='relu'))
    model.add(tf.keras.layers.Dense(7, activation='softmax'))

    model.compile(optimizer='adam',  # Para medir la exactitud de la red
                  # Para actualizar el modelo basado en los datos que ve y su loss function
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=['accuracy'])  # Para monitorear los training y testing steps
    return model


def trainNetwork(model, data, labels):
    model.fit(data.reshape(-1, 42), labels, epochs=10)  # Entrena la red

    # Se compara que tan buenos son los resultados
    test_loss, test_acc = model.evaluate(data,  labels, verbose=2)

    # La diferencia entre el % de training y el de testing es overfitting; cuando aprende cosas que no son utiles cuando ve cosas nuevas
    print('\nTest accuracy:', test_acc)


def gameboardToNumpyArray(gameboard):
    list = []
    for r in range(len(gameboard)):
        for c in range(len(gameboard[r])):
            list.append(int(gameboard[r][c]))
    return np.array(list)


def predictNextMove(model, gameboard):
    input = gameboardToNumpyArray(gameboard)
    probability_model = tf.keras.Sequential([model,
                                             tf.keras.layers.Softmax()])
    input = (np.expand_dims(input, 0))
    output = probability_model.predict(input)
    print("Mi prediccion: *********")
    print(output)
    return output


def main():
    training_data, training_labels = getTrainingData()
    training_data = dataToListOfLists(training_data)
    data = np.array(training_data)
    labels = np.array(training_labels)

    model = createNetwork()
    trainNetwork(model, data, labels)
    gameboard = [
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         Constants.EMPTY_VAL, Constants.EMPTY_VAL, '1'],
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         Constants.EMPTY_VAL, '2', '1'],
        [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
         '2', '2', '1']
    ]
    predictNextMove(model, gameboard)
    print(gameboard)

    '''
    model.save('/tmp/modelDiosvier')
    del model

    model = tf.keras.models.load_model('/tmp/modelDiosvier')
    trainNetwork(model, data, labels)
    '''


if __name__ == "__main__":
    main()
