def chatbot():
    respuestas = {
        "qué es la ia": "La IA es la simulación de la inteligencia humana en computadoras.",
        "quién inventó la ia": "El término 'IA' fue acuñado por John McCarthy en 1956.",
        "adiós": "¡Hasta luego!"
    }
    print("¡Hola! Soy un chatbot de IA. Pregúntame algo.")
    while True:
        pregunta = input("Tú: ").lower()
        for clave in respuestas:
            if clave in pregunta:
                print(f"Chatbot: {respuestas[clave]}")
                if clave == "adiós":
                    return
                break
        else:
            print("Chatbot: No entiendo tu pregunta.")

chatbot()
