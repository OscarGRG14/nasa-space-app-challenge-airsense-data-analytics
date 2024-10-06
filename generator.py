import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar conjunto de datos de entrenamiento
train_data = pd.read_csv('./dataset.csv')  # Asegúrate de tener un dataset de entrenamiento

# Verifica que las columnas existen en el DataFrame
print("Columnas disponibles en el dataset:", train_data.columns)

# Separar características y etiquetas
X = train_data[['mean_intensity', 'std_intensity', 'max_intensity']]
y_co2 = train_data['co2_emissions']
y_quality = train_data['air_quality']

# Entrenar modelo para emisiones de CO2
model_co2 = LinearRegression()
model_co2.fit(X, y_co2)

# Entrenar modelo para calidad del aire
model_quality = LinearRegression()
model_quality.fit(X, y_quality)

def analyze_image(image_array):
    """
    Analiza una imagen representada como un array para predecir emisiones de CO2 y calidad del aire.
    """
    # Extraer características de la imagen
    features = extract_features(image_array)
    
    # Convertir características a DataFrame con nombres de columnas
    feature_names = ['mean_intensity', 'std_intensity', 'max_intensity']
    features_df = pd.DataFrame(features, columns=feature_names)

    # Predicciones
    co2_emissions = model_co2.predict(features_df)
    air_quality = model_quality.predict(features_df)
    
    return {
        "co2_emissions": np.sum(co2_emissions),  # Sumar las emisiones de CO2 predichas
        "air_quality": np.mean(air_quality)       # Promediar la calidad del aire predicha
    }


def extract_features(image_array):
    """
    Extrae características de la imagen para el modelo de aprendizaje automático.
    """
    # Extraer características relevantes
    features = np.array([
        np.mean(image_array),
        np.std(image_array),
        np.max(image_array)
    ]).reshape(1, -1)  # Reshape para que sea 2D
    return features
