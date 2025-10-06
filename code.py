import streamlit as st

# Preguntas definidas directamente en el código para evitar problemas de red
preguntas = [
    {
        "pregunta": "¿Cuál es la función principal de las neuronas?",
        "opciones": [
            "Producir hormonas",
            "Transmitir señales eléctricas y químicas",
            "Regular la presión sanguínea",
            "Almacenar grasas"
        ],
        "respuesta_correcta": 1,
        "explicacion": "Las neuronas son las células encargadas de la transmisión de señales eléctricas y químicas en el sistema nervioso."
    },
    {
        "pregunta": "¿Qué estructura cerebral está principalmente involucrada en la formación de recuerdos?",
        "opciones": [
            "Amígdala",
            "Tálamo",
            "Hipocampo",
            "Cerebelo"
        ],
        "respuesta_correcta": 2,
        "explicacion": "El hipocampo es fundamental para la formación y consolidación de nuevos recuerdos."
    },
    {
        "pregunta": "¿Cuál es el neurotransmisor más relacionado con la sensación de placer y recompensa?",
        "opciones": [
            "GABA",
            "Dopamina",
            "Serotonina",
            "Acetilcolina"
        ],
        "respuesta_correcta": 1,
        "explicacion": "La dopamina está estrechamente vinculada con los circuitos de recompensa y placer."
    },
    {
        "pregunta": "¿Qué es la plasticidad cerebral?",
        "opciones": [
            "La capacidad del cerebro para aumentar su tamaño",
            "La habilidad del cerebro para cambiar y adaptarse",
            "La resistencia del cerebro a enfermedades",
            "La producción de nuevas neuronas"
        ],
        "respuesta_correcta": 1,
        "explicacion": "La plasticidad cerebral se refiere a la capacidad del cerebro para reorganizarse y adaptarse."
    },
    {
        "pregunta": "¿Qué parte del sistema nervioso central está encargada de coordinar movimientos finos y el equilibrio?",
        "opciones": [
            "Médula espinal",
            "Cerebelo",
            "Corteza cerebral",
            "Tronco encefálico"
        ],
        "respuesta_correcta": 1,
        "explicacion": "El cerebelo es responsable de la coordinación motora y el equilibrio."
    },
    {
        "pregunta": "¿Cuál es el rol principal de las células gliales?",
        "opciones": [
            "Transmitir impulsos eléctricos",
            "Producir mielina, soporte y nutrición a las neuronas",
            "Producir neurotransmisores",
            "Detectar estímulos sensoriales"
        ],
        "respuesta_correcta": 1,
        "explicacion": "Las células gliales apoyan a las neuronas con funciones estructurales, nutricionales y protección."
    },
    {
        "pregunta": "¿Qué ocurre durante un potencial de acción en una neurona?",
        "opciones": [
            "Se libera serotonina al espacio sináptico",
            "La neurona genera un impulso eléctrico al cambiar su polaridad",
            "La neurona se divide para crear una nueva célula",
            "Se descompone la membrana neuronal"
        ],
        "respuesta_correcta": 1,
        "explicacion": "Un potencial de acción es un cambio rápido en la polaridad de la membrana neuronal que permite la transmisión de señales."
    },
    {
        "pregunta": "¿Cuál es la función del sistema nervioso autónomo?",
        "opciones": [
            "Controlar movimientos voluntarios",
            "Regular funciones involuntarias como la respiración y el ritmo cardíaco",
            "Procesar información sensorial visual",
            "Coordinar el aprendizaje y la memoria"
        ],
        "respuesta_correcta": 1,
        "explicacion": "El sistema nervioso autónomo controla funciones automáticas y no conscientes."
    },
    {
        "pregunta": "¿Qué es la sinapsis?",
        "opciones": [
            "La unión entre dos neuronas donde se transmite la señal",
            "El cuerpo principal de la neurona",
            "La vaina que recubre el axón",
            "Un tipo de célula glial"
        ],
        "respuesta_correcta": 0,
        "explicacion": "La sinapsis es la conexión funcional donde una neurona transmite información a otra."
    },
    {
        "pregunta": "¿Qué característica distingue a las neuronas sensitivas?",
        "opciones": [
            "Transmiten señales desde el cerebro a los músculos",
            "Transmiten señales desde los receptores sensoriales hacia el sistema nervioso central",
            "Son responsables de la memoria a largo plazo",
            "Regulan la presión arterial"
        ],
        "respuesta_correcta": 1,
        "explicacion": "Las neuronas sensitivas llevan información desde los órganos sensoriales al sistema nervioso central."
    }
]

def main():
    st.title("Quiz de Neurociencias")

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

