import streamlit as st
from deep_translator import GoogleTranslator
import base64

# Função para definir imagem de fundo
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Aplicar background
set_background("background.png")  # Altere o nome para o arquivo que você quer usar

# Título do app
st.title("Professional Language Translator")

# Área de textos
texto = st.text_area("Digite sua frase em português:", 
                     "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial.")

# Seleção de idiomas
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Japonês": "ja"
}

idiomas_escolhidos = st.multiselect("Selecione os idiomas de destino:", list(linguas.keys()), ["Inglês", "Espanhol"])

# Traduzir
if st.button("Traduzir"):
    if texto.strip() == "":
        st.warning("Digite uma frase para traduzir!")
    else:
        for nome in idiomas_escolhidos:
            codigo = linguas[nome]
            traducao = GoogleTranslator(source='pt', target=codigo).translate(texto)
            st.subheader(f'➡ Tradução para {nome} ({codigo})')
            st.write(f'**Original:** {texto}')
            st.write(f'**Traduzido:** {traducao}')
            st.write("---")
