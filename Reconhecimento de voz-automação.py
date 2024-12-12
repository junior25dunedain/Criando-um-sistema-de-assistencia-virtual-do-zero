from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")
    os.system("start output.mp3")  # 'start' no Windows, 'open' no MacOS, 'xdg-open' no Linux


import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            text_to_speech(text)
            return text
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
        except sr.RequestError:
            print("Erro ao conectar-se ao serviço de reconhecimento de fala")


import webbrowser

def search_wikipedia(query):
    webbrowser.open(f"https://pt.wikipedia.org/wiki/{query}")



def open_youtube():
    webbrowser.open("https://www.youtube.com")



from geopy.geocoders import Nominatim
import folium

def find_nearest_pharmacy(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(location)
    map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)
    folium.Marker([location.latitude, location.longitude], popup="Você está aqui").add_to(map)

    # Exemplo fixo: adicionar um marcador de farmácia
    # Em uma aplicação real, você poderia integrar uma API que retorna farmácias próximas
    pharmacy_location = geolocator.geocode("farmácia mais próxima")
    folium.Marker([pharmacy_location.latitude, pharmacy_location.longitude], popup="Farmácia Mais Próxima").add_to(map)
    
    map.save("map.html")
    webbrowser.open("map.html")

# Função para abrir o Excel 
def open_excel(): 
    os.system("start excel") # 'start excel' no Windows, 'open -a "Microsoft Excel"' no MacOS 
# Função para abrir o Word 
def open_word(): 
    os.system("start winword") # 'start

def assistente_virtual():
    comando = speech_to_text()

    if comando:
        if "Wikipédia" in comando:
            query = comando.replace("Wikipedia", "").strip()
            print(query)
            search_wikipedia(query)
        elif "YouTube" in comando:
            open_youtube()
        elif "farmácia" in comando:
            find_nearest_pharmacy("sua localização atual ou fornecida")
        elif "Excel" in comando: 
            open_excel() 
        elif "Word" in comando: 
            open_word()

assistente_virtual()
