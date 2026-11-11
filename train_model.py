"""
Optional starter training script.

Dataset layout:
dataset/
  Healthy/
    leaf1.jpg
  Tomato___Early_blight/
    leaf2.jpg
  Tomato___Late_blight/
    leaf3.jpg

Run on a computer with TensorFlow installed:
  pip install tensorflow
  python train_model.py dataset

This is a starter classifier, not a validated agricultural diagnostic model.
Evaluate it on separate, real-world images before relying on predictions.
"""
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python train_model.py <dataset_folder>")

    data_dir = Path(sys.argv[1])
    if not data_dir.is_dir():
        raise SystemExit(f"Dataset folder not found: {data_dir}")

    try:
        import tensorflow as tf
    except ImportError:
        raise SystemExit("Install TensorFlow first: pip install tensorflow")

    image_size = (224, 224)
    batch_size = 32

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="training", seed=123,
        image_size=image_size, batch_size=batch_size
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir, validation_split=0.2, subset="validation", seed=123,
        image_size=image_size, batch_size=batch_size
    )

    class_names = train_ds.class_names
    normalization = tf.keras.layers.Rescaling(1.0 / 255)
    train_ds = train_ds.map(lambda x, y: (normalization(x), y)).prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.map(lambda x, y: (normalization(x), y)).prefetch(tf.data.AUTOTUNE)

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(224, 224, 3)),
        tf.keras.layers.Conv2D(32, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(128, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(len(class_names), activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    model.fit(train_ds, validation_data=val_ds, epochs=10)
    model.save("plant_disease_model.keras")
    Path("class_names.txt").write_text(
        "\n".join(class_names) + "\n", encoding="utf-8"
    )
    print("Saved plant_disease_model.keras and class_names.txt")

if __name__ == "__main__":
    main()
