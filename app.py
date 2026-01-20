import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image

# --- CORREÇÃO AQUI ---
# Seu modelo pede 160, então vamos dar 160 pra ele.
IMG_SIZE_APP = 160
# Confirme se o nome do arquivo abaixo é o que está na sua pasta
MODEL_PATH = 'modelo_racas_pro.tflite'

# (O resto do código continua igual...)
RACAS = [
    'Abyssinian', 'American Bulldog', 'American Pit Bull Terrier', 'Basset Hound',
    'Beagle', 'Bengal', 'Birman', 'Bombay', 'Boxer', 'British Shorthair',
    'Chihuahua', 'Egyptian Mau', 'English Cocker Spaniel', 'English Setter',
    'German Shorthaired', 'Great Pyrenees', 'Havanese', 'Japanese Chin',
    'Keeshond', 'Leonberger', 'Maine Coon', 'Miniature Pinscher', 'Newfoundland',
    'Persian', 'Pomeranian', 'Pug', 'Ragdoll', 'Russian Blue', 'Saint Bernard',
    'Samoyed', 'Scottish Terrier', 'Shiba Inu', 'Siamese', 'Sphynx',
    'Staffordshire Bull Terrier', 'Wheaten Terrier', 'Yorkshire Terrier'
]

def get_info(raca):
    infos = {
        'Persian': "🐱 PERSA\nCuidados: Escovação diária.\nTemperamento: Calmo.",
        'Siamese': "🐱 SIAMÊS\nCuidados: Atenção constante.\nTemperamento: Falante.",
        'Boxer': "🐶 BOXER\nCuidados: Muito exercício.\nTemperamento: Brincalhão.",
        'Beagle': "🐶 BEAGLE\nCuidados: Passeios longos.\nTemperamento: Curioso.",
    }
    return infos.get(raca, f"Raça: {raca}\nRecomendação: Mantenha vacinação em dia e muito amor.")

# --- INTERFACE VISUAL ---
st.set_page_config(page_title="Pet ID", page_icon="🐾")
st.title("🐾 Identificador de Pets")
st.write("Formatos: JPG, PNG, WEBP, BMP, TIFF, JFIF.")

uploaded_file = st.file_uploader(
    "Escolha uma imagem...",
    type=["jpg", "png", "jpeg", "webp", "bmp", "tiff", "tif", "jfif"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem carregada', use_column_width=True)

        with st.spinner('Processando...'):
            image = image.convert('RGB')
            img_array = np.array(image)

            # REDIMENSIONANDO PARA 160 (Para bater com o modelo)
            img_resized = cv2.resize(img_array, (IMG_SIZE_APP, IMG_SIZE_APP))

            input_data = np.expand_dims(img_resized, axis=0).astype(np.float32)
            input_data = (input_data / 127.5) - 1

            interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()

            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])

            idx = np.argmax(output_data)
            raca_detectada = RACAS[idx]
            confianca = 100 * np.max(output_data)

        st.success(f"Resultado: **{raca_detectada.upper()}**")
        st.progress(int(confianca))
        st.caption(f"Confiança: {confianca:.1f}%")
        st.info(get_info(raca_detectada))

    except Exception as e:
        st.error(f"Erro técnico: {e}")
