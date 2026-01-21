# 🐾 Identificador de Raças de Pets 

Este projeto é uma aplicação capaz de identificar **37 raças de cães e gatos** a partir de uma imagem. O sistema utiliza uma Rede Neural Convolucional (MobileNetV2) treinada via Transfer Learning e Fine-Tuning para classificar os animais e fornece dicas de cuidados e temperamento.

## 📋 Funcionalidades

* **Classificação de Raças:** Identifica 37 raças específicas (ex: Persa, Beagle, Pug, etc.).
* **Ficha Técnica:** Exibe informações sobre o comportamento e necessidades do animal.
* **Interface Web:** Aplicação interativa desenvolvida com **Streamlit**.
* **Flexibilidade:** Pode ser executado na nuvem (Google Colab) ou localmente.

## 🛠 Tecnologias

* **Linguagem:** Python 3.x
* **IA/ML:** TensorFlow, Keras, TensorFlow Lite
* **Interface:** Streamlit
* **Utils:** OpenCV, PIL, NumPy

## 🐶 Raças Suportadas

O modelo foi treinado no **Oxford-IIIT Pet Dataset**.

**Gatos:**
Abyssinian, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, Maine Coon, Persian, Ragdoll, Russian Blue, Siamese, Sphynx.

**Cachorros:**
American Bulldog, American Pit Bull Terrier, Basset Hound, Beagle, Boxer, Chihuahua, English Cocker Spaniel, English Setter, German Shorthaired, Great Pyrenees, Havanese, Japanese Chin, Keeshond, Leonberger, Miniature Pinscher, Newfoundland, Pomeranian, Pug, Saint Bernard, Samoyed, Scottish Terrier, Shiba Inu, Staffordshire Bull Terrier, Wheaten Terrier, Yorkshire Terrier.

## ℹ️ Informações sobre o Notebook

O arquivo `Aplicação_para_classificação_de_pets_(cachorro_e_gato).ipynb` possui duas estruturas principais:

### 1. Classificação Binária (Gato vs Cachorro)
* **Localização:** Tópicos 1 e 2.
* **Dataset:** "CatVSDog".
* **Estado Atual:** Comentado por padrão.
* **Nota:** Para testar, remova os comentários. A execução depende do download automático de um dataset externo (Microsoft).

### 2. Classificação de Raças (MobileNetV2)
* **Localização:** Tópicos 3 até 6.3.
* **Técnica:** Transfer Learning e Fine-Tuning no dataset **Oxford-IIIT Pet**.
* **Objetivo:** Reconhecer características visuais detalhadas (orelha, pelagem) para alta precisão.
* **Estado Atual:** Ativo (código principal do projeto).
* **Nota:** O **Tópico 5** (Teste isolado no Colab) está comentado para não interromper a execução automática ("Run All").

> **OBS:** O projeto foca na segunda estrutura. O código extra foi mantido para fins de documentação e estudo.

## 🚀 Como Rodar o Projeto

Escolha a opção que preferir:

### Opção 1: Site Hospedado
Deixei o site hospedado só no ponto de testar a aplicação:

Link: https://pet-identificador-de-racas.streamlit.app/

> **Dica:** Lembre-se que o modelo foi treinado com 37 raças, deixei disponibilizado no repositório algumas fotos de gatos e cachorros caso queira testar.

****

### Opção 2: Google Colab 
Ideal para testar na nuvem, sem precisar instalar nada no seu computador. Escolha o método que preferir:

- Nesta opção, você roda o arquivo .ipynb original, visualizando todo o processo de código (carregamento de dados, treinamento) até chegar na aplicação.

- Baixe o arquivo **Aplicação_para_classificação_de_pets_(cachorro_e_gato).ipynb** deste repositório.

- Acesse o Google Colab e faça o upload do arquivo.

- No menu superior, vá em Ambiente de Execução > Executar tudo.

- Role até a última célula. O código irá gerar um link público (ex: xxxx.ngrok-free.app ou similar).

- Clique no link para abrir o sistema.

**Nota:** Se o código pedir um token do Ngrok, você pode criar uma conta gratuita em ngrok.com e colar seu token.

> **Importante:** Já tem configurado o meu token então mude se preferir.

### Opção 3: VS Code 
Ideal para desenvolvimento e uso offline.

**Pré-requisitos:**
* Python instalado recomendo versão 3.12.
* Git instalado.

**Passo a Passo:**

1.  **Clone o repositório:**
    Abra o terminal e digite:
    ```bash
    git clone https://github.com/RuanSombra/PetID.git
    ```
    ```bash
    cd PetID
    ```

2.  **Crie um ambiente virtual (Recomendado):**
    * *Windows:*
      ```bash
      python -m venv venv
      ```
      ```bash
      .\venv\Scripts\activate
      ```
    * *Mac/Linux:*
      ```bash
      python3 -m venv venv
      ```
      ```bash
      source venv/bin/activate
      ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    > **Dica:** Aguarde terminar todas as instalações para prosseguir com o próximo passo.

4.  **Execute o App:**
    ```bash
    streamlit run app.py
    ```

    > **Dica:** Se aparecer uma pergunta sobre "Email" no terminal, apenas aperte **ENTER** para pular. O navegador abrirá automaticamente em `http://localhost:8501`.

## ⚠️ Solução de Problemas Comuns

* **Erro "Dimension Mismatch (Expected 160 but got 224)":**
    * Verifique se a variável `IMG_SIZE_APP` no arquivo `app.py` é igual a **160**.

* **Aviso "Update pip" (Texto amarelo):**
    * Se aparecer um aviso amarelo pedindo para atualizar o pip, você pode ignorar. O projeto roda bem na versão atual.

* **Erro ao abrir imagem:**
    * O App aceita JPG, PNG, WEBP, BMP, TIFF e JFIF. Se der erro, tente converter a imagem para JPG padrão.

## Autor: Desenvolvido por Ruan Pactrick de Sousa e Sousa
