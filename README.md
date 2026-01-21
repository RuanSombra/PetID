# 🐾 Identificador de Raças de Pets 

Este projeto é uma aplicação capaz de identificar **37 raças de cães e gatos** a partir de uma imagem. O sistema utiliza uma Rede Neural Convolucional (MobileNetV2) treinada via Transfer Learning e Fine-Tuning para classificar os animais e fornece dicas de cuidados e temperamento.

---

## 📋 Funcionalidades

* **Classificação de Raças:** Identifica 37 raças específicas (ex: Persa, Beagle, Pug, etc.).
* **Ficha Técnica:** Exibe informações sobre o comportamento e necessidades do animal.
* **Interface Web:** Aplicação interativa desenvolvida com **Streamlit**.
* **Flexibilidade:** Pode ser executado na nuvem (Google Colab) ou localmente.

---

## 🛠 Tecnologias

* **Linguagem:** Python 3.x
* **IA/ML:** TensorFlow, Keras, TensorFlow Lite
* **Interface:** Streamlit
* **Utils:** OpenCV, PIL, NumPy

---

## 🐶 Raças Suportadas

O modelo foi treinado no **Oxford-IIIT Pet Dataset**.

**Gatos:**
Abyssinian, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, Maine Coon, Persian, Ragdoll, Russian Blue, Siamese, Sphynx.

**Cachorros:**
American Bulldog, American Pit Bull Terrier, Basset Hound, Beagle, Boxer, Chihuahua, English Cocker Spaniel, English Setter, German Shorthaired, Great Pyrenees, Havanese, Japanese Chin, Keeshond, Leonberger, Miniature Pinscher, Newfoundland, Pomeranian, Pug, Saint Bernard, Samoyed, Scottish Terrier, Shiba Inu, Staffordshire Bull Terrier, Wheaten Terrier, Yorkshire Terrier.

---

## Informações sobre o app.py

O **app.py** possui duas estruturas:

**Tópicos 1 e 2:** O treinamento para identificar se é cachorro ou gato com o Dataset **"CatVSDog"**.
  
- **Nota:** O código referente à primeira estrutura mencionada está comentado por padrão. Para testá-lo, basta remover os comentários.
- **Aviso Importante:** A execução deste trecho depende do download automático do dataset através de um link externo (Microsoft). Caso o servidor de origem esteja instável ou o link tenha sido alterado, o download falhará e a aplicação não rodará.
  
**Tópicos 3 até 6.3:** O treinamento para identificação de raças de gatos e cachorros utilizou a arquitetura **MobileNetV2**. Aplicamos **Transfer Learning** para aproveitar o conhecimento prévio da rede e realizamos o **Fine-Tuning** utilizando o dataset **Oxford-IIIT Pet**. Esse processo ajustou a **rede neural** para reconhecer características visuais **específicas** e **detalhadas** (como formato da orelha e textura da pelagem), garantindo alta precisão na classificação das raças.
- **Nota sobre o Tópico 5:** Este trecho de código foi mantido comentado por padrão para não interromper o fluxo de execução automática ("Run All") do notebook. Ele serve para testes isolados da aplicação dentro do ambiente Google Colab. Para utilizá-lo, basta descomentar as linhas.
- **Aviso Importante:** A execução deste trecho depende do download automático do dataset através de um link externo (Microsoft). Caso o servidor de origem esteja instável ou o link tenha sido alterado, o download falhará e a aplicação não rodará.

**OBS:** Utilizaremos para o projeto apenas a segunda estrutura, por isso, caso dê uma olhada no app.py verá alguns códigos comentados para que não impeça a execução do código quando for utilizado o **"Executar Tudo"**.

> As informações acima são apenas para conhecimento de como está estruturado o projeto.

---

## 🚀 Como Rodar o Projeto

Escolha a opção que preferir:

### Opção 1: Site Hospedado
Deixei o site hospedado só no ponto de testar a aplicação:

Link: https://pet-identificador-de-racas.streamlit.app/

> **Dica:** Lembre-se que o modelo foi treinado com 37 raças, deixei disponibilizado no repositório algumas fotos de gatos e cachorros caso queira testar.

****

### Opção 2: Google Colab 
Ideal para testar rápido sem configurar nada no computador.

1.  Baixe o arquivo `.ipynb` deste repositório.
2.  Abra no [Google Colab](https://colab.research.google.com/) e faça upload do arquivo.
3.  Vá em **Ambiente de Execução** > **Executar tudo**.
4.  **Importante:** Na última célula do código, cole seu token gratuito do Ngrok (pegue em [dashboard.ngrok.com](https://dashboard.ngrok.com)).
5.  Clique no link gerado (`xxxx.ngrok-free.app`) para usar.

**Você pode utilizar o meu token para rodar a aplicação que já está no projeto, mas queira pode substituir.**

---

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

---

## ⚠️ Solução de Problemas Comuns

* **Erro "Dimension Mismatch (Expected 160 but got 224)":**
    * Verifique se a variável `IMG_SIZE_APP` no arquivo `app.py` é igual a **160**.

* **Aviso "Update pip" (Texto amarelo):**
    * Se aparecer um aviso amarelo pedindo para atualizar o pip, você pode ignorar. O projeto roda bem na versão atual.

* **Erro ao abrir imagem:**
    * O App aceita JPG, PNG, WEBP, BMP, TIFF e JFIF. Se der erro, tente converter a imagem para JPG padrão.

---

## Autor: Desenvolvido por Ruan Pactrick de Sousa e Sousa
