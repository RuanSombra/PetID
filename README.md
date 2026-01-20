# 🐾 Identificador de Raças de Pets (Deep Learning)

Este projeto é uma aplicação de Inteligência Artificial capaz de identificar **37 raças de cães e gatos** a partir de uma imagem. Além da classificação, o sistema fornece informações úteis sobre o temperamento e os cuidados necessários para a raça detectada.

O projeto foi desenvolvido utilizando **Transfer Learning** com a arquitetura **MobileNetV2** e otimizado com **TensorFlow Lite** para inferência rápida e leve.

## 📋 Funcionalidades

* **Identificação de Raças:** Classifica imagens entre 37 raças populares do *Oxford-IIIT Pet Dataset*.
* **Informações de Cuidado:** Exibe dicas de manejo, temperamento e saúde específicas para cada animal.
* **Suporte Multi-formato:** Aceita upload de imagens `.JPG`, `.PNG`, `.WEBP`, `.BMP`, `.TIFF` e `.JFIF`.
* **Interface Web:** Interface amigável construída com Streamlit.
* **Otimização Mobile:** Backend otimizado com TensorFlow Lite (`.tflite`).

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Machine Learning:** TensorFlow, Keras
* **Modelo Base:** MobileNetV2 (ImageNet weights)
* **Interface:** Streamlit
* **Processamento de Imagem:** OpenCV, PIL (Pillow)
* **Acesso Remoto (Colab):** PyNgrok

---

## 📊 Dataset e Raças Suportadas

O modelo foi treinado no **Oxford-IIIT Pet Dataset**.

**Gatos:**
Abyssinian, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, Maine Coon, Persian, Ragdoll, Russian Blue, Siamese, Sphynx.

**Cachorros:**
American Bulldog, American Pit Bull Terrier, Basset Hound, Beagle, Boxer, Chihuahua, English Cocker Spaniel, English Setter, German Shorthaired, Great Pyrenees, Havanese, Japanese Chin, Keeshond, Leonberger, Miniature Pinscher, Newfoundland, Pomeranian, Pug, Saint Bernard, Samoyed, Scottish Terrier, Shiba Inu, Staffordshire Bull Terrier, Wheaten Terrier, Yorkshire Terrier.

---

## 🚀 Como Executar o Projeto

Você pode rodar este projeto de duas formas: na nuvem (Google Colab) ou localmente no seu computador.

### Opção 1: Rodar no Google Colab (Sem instalação local)
Esta é a forma mais fácil se você não quiser configurar Python no seu PC.

1.  Baixe o arquivo `.ipynb` deste repositório.
2.  Acesse o [Google Colab](https://colab.research.google.com/) e faça o upload do notebook.
3.  No menu superior, clique em **Ambiente de Execução** > **Executar tudo**.
    * *Nota: O download do dataset e treinamento pode levar alguns minutos na primeira vez.*
4.  **Atenção ao Ngrok:** Na última célula do código, insira seu Authtoken gratuito do Ngrok (obtido em [dashboard.ngrok.com](https://dashboard.ngrok.com)) para gerar o link de acesso.
5.  Clique no link gerado (`xxxx.ngrok-free.app`) para abrir o App.

### Opção 2: Rodar Localmente (Windows/Linux/Mac)
Para rodar direto no seu computador:

**1. Clone o repositório ou baixe os arquivos:**
Certifique-se de ter os arquivos `app.py`, `modelo_racas_pro.tflite` e `requirements.txt` na mesma pasta.

**2. Instale as dependências:**
Abra o terminal na pasta do projeto e execute:
```bash
pip install -r requirements.txt
