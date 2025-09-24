import streamlit as st
from deep_translator import GoogleTranslator

def set_background_url(image_url):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# URL da imagem de fundo
image_url = "https://wallpaperscraft.com/image/street_city_buildings_198312_2560x1440.jpg"

# Aplicar o background
set_background_url(image_url)

# Título do app
st.title("Professional Language Translator")

# Área de texto para entrada
texto = st.text_area(
    "Digite sua frase em português:",
    "Olá! Estou aprendendo a programar em Python e a usar modelos de inteligência artificial."
)

# Dicionário de idiomas suportados
linguas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Japonês": "ja"
}

# Seleção de idiomas para tradução
idiomas_escolhidos = st.multiselect(
    "Selecione os idiomas de destino:",
    list(linguas.keys()),
    ["Inglês", "Espanhol"]
)

# Botão para realizar tradução
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

