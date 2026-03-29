import pandas as pd
from sklearn.model_selection import train_test_split
from text_embedding import embed_labeled_training_data
from tensorflow import keras
from keras import layers


def model_construction():
    # Loading the entire training training_data set
    df_total = pd.read_csv("training_data/synthetic_character_dataset_realistic.csv")

    # Splitting the training_data set intro training and testing part and resetting the csv indexes
    df_train, df_test = train_test_split(df_total, test_size=0.10, random_state=42)
    df_train = df_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    print("Preview of training training_data:")
    print(df_train.head())

    # Embedding both the training and testing training_data frame
    X_train, y_train = embed_labeled_training_data(df_train)
    X_test, y_test = embed_labeled_training_data(df_test)

    # Loading the Keras model for model construction
    model_keras = keras.Sequential([
        layers.Input(shape=(384,)),  # SBERT embedding size
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),  # Prevents overfitting
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(4, activation="softmax")  # 4 archetypes → probabilities
    ])

    model_keras.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",  # Use this when y is integer labels
        metrics=["accuracy"]
    )

    model_keras.summary()

    # Training the model with our X_train embedded descriptions and y_train corresponding labels
    print("\nTraining model...")
    history = model_keras.fit(
        X_train, y_train,
        epochs=20,
        batch_size=32,
        validation_split=0.1,  # Holds out 10% of train training_data to monitor overfitting
        verbose=1
    )

    # Evaluating the created model with the X_test and y_test training_data
    print("\nEvaluating on test set...")
    test_loss, test_accuracy = model_keras.evaluate(X_test, y_test, verbose=0)
    print(f"Test accuracy: {test_accuracy:.4f}")
    print(f"Test loss    : {test_loss:.4f}")

    # Saving the model as a .keras file
    model_keras.save("training_data/model.keras")
    print("\nModel successfully saved!")

    return model_keras

model_construction()