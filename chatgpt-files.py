import streamlit as st
import openai
import time
import os

def setup_openai():
    api_key = "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"
    openai.api_key = api_key

def load_training_data_from_folder(folder_path):
    training_text = ""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                training_text += content + "\n\n"  # Adicione uma quebra de linha entre cada arquivo para separar o conteúdo
    return training_text

def chat_with_openai_with_throttling(prompt, model="text-davinci-003", max_tokens=300, temperature=0.8, stop_sequences=None):
    time.sleep(2)  # Aguarde 2 segundos entre as chamadas
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop_sequences
    )
    return response.choices[0].text.strip()

def main():
    setup_openai()
    st.title("Bem-vindo(a) ao Chat GIS!")

    folder_path = "/files/"  # Substitua pelo caminho da sua pasta
    additional_training_data = load_training_data_from_folder(folder_path)

    st.write("Digite sua pergunta abaixo:")
    user_input = st.text_area("")

    if st.button("Enviar"):
        st.subheader("Sua pergunta:")
        st.write(user_input)

        esri_products = [
            "ArcGIS Desktop", "ArcGIS Online", "ArcGIS Pro"
            # Adicione outros produtos aqui, se necessário
        ]
        esri_prompt = f"Produtos ESRI: {', '.join(esri_products)}\n\nVocê: {user_input}\nChatbot:"

        response = chat_with_openai_with_throttling(esri_prompt + additional_training_data, max_tokens=2048)
        st.subheader("Resposta:")
        st.write(response)

if __name__ == "__main__":
    main()
