import streamlit as st
import requests

# URL del archivo JSON en GitHub (modifica con tu URL)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main/preguntas_neuro.json"

@st.cache_data
def cargar_preguntas():
    response = requests.get(GITHUB_RAW_URL)
    response.raise_for_status()
    return response.json()

def main():
    st.title("Quiz de Neurociencias")

    preguntas = cargar_preguntas()

    # Inicialización de estados
    if "indice" not in st.session_state:
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.mostrar_retro = False
        st.session_state.respuesta_correcta = False

    if st.session_state.indice < len(preguntas):
        pregunta_actual = preguntas[st.session_state.indice]

        st.write(f"**Pregunta {st.session_state.indice + 1}:** {pregunta_actual['pregunta']}")

        opciones = pregunta_actual['opciones']
        seleccion = st.radio("Selecciona una opción:", opciones, key=f"radio_{st.session_state.indice}")

        if st.button("Responder"):
            correcta = pregunta_actual['respuesta_correcta']
            if opciones.index(seleccion) == correcta:
                st.session_state.puntaje += 1
                st.session_state.respuesta_correcta = True
                st.success("¡Respuesta correcta!")
            else:
                st.session_state.respuesta_correcta = False
                st.error("Respuesta incorrecta.")

            st.session_state.mostrar_retro = True

        if st.session_state.mostrar_retro:
            st.write(f"**Explicación:** {pregunta_actual['explicacion']}")
            if st.session_state.respuesta_correcta:
                if st.button("Siguiente pregunta"):
                    st.session_state.indice += 1
                    st.session_state.mostrar_retro = False
                    st.session_state.respuesta_correcta = False
            else:
                if st.button("Intentar de nuevo"):
                    st.session_state.mostrar_retro = False

    else:
        st.write("### ¡Has completado el quiz!")
        st.write(f"Puntaje final: {st.session_state.puntaje} / {len(preguntas)}")
        if st.button("Reiniciar"):
            st.session_state.indice = 0
            st.session_state.puntaje = 0
            st.session_state.mostrar_retro = False
            st.session_state.respuesta_correcta = False

if __name__ == "__main__":
    main()
