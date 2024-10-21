from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os

# Define the path to save the model as .keras file (new recommended format)
model_save_path = os.path.join('models', 'snow_detection_model.keras')

# Data generators with augmentation for better generalization
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,  # 80% train, 20% validation
    horizontal_flip=True,  # Randomly flip images horizontally
    rotation_range=20      # Randomly rotate images by up to 20 degrees
)

# Train and validation generators
train_generator = train_datagen.flow_from_directory(
    os.path.join('..', 'dataset'),  # Dataset folder with 'SNOW' and 'NOSNOW' subfolders
    target_size=(224, 224),  # Resize images to 224x224
    batch_size=32,
    class_mode='binary',  # Binary classification: snow vs non-snow
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    os.path.join('..', 'dataset'),  # Dataset folder with 'SNOW' and 'NOSNOW' subfolders
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Load the ResNet50 base model without the top classification layer
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom classification layers
x = base_model.output
x = GlobalAveragePooling2D()(x)  # Global average pooling to reduce dimensionality
x = Dense(1024, activation='relu')(x)  # Fully connected layer
predictions = Dense(1, activation='sigmoid')(x)  # Binary output (0 or 1 for snow/no snow)

# Create the final model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model with Adam optimizer and binary crossentropy loss
model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks for early stopping and saving the best model
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint(model_save_path, monitor='val_loss', save_best_only=True, verbose=1)

# Train the model
model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10,  # Number of epochs (adjust as necessary)
    callbacks=[early_stopping, model_checkpoint]
)

# The best model is already saved by ModelCheckpoint in the .keras format.
