import pyttsx3
import speech_recognition as sr
import eel
import webbrowser
import time
import os
import requests
from playsound import playsound
from typing import Union
import pyttsx3
import speech_recognition as sr
import datetime
import sys
import subprocess
import bs4
import pyjokes
import cv2
import pywhatkit
from typing import Union
import pyautogui
import tkinter as tk
from tkinter import font, messagebox
import threading
import time
from sys import platform
import io
import socket
import keyboard



def generate_audio(message: str, voice: str = "Brian") -> Union[None, bytes]:
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()  # Check if the request was successful
        return result.content
    except requests.RequestException as e:
        print(f"Error fetching audio: {e}")
        return None

def speak(text, voice="Brian", folder="", extension=".mp3"):
    try:
        result_content = generate_audio(text, voice)
        if result_content is None:
            print("Failed to generate audio")
            return "Failed to generate audio"

        file_path = os.path.join(folder, f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound(file_path)
        os.remove(file_path)

        return text
    except Exception as e:
        print(e)
        return str(e)

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query),
        time.sleep(2)
    except Exception as e:
        return ""
    
    return query.lower()






@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        # Custom Commands as a dictionary with lambda functions
        custom_commands = {
            'jarvis': lambda: speak("Yes sir, I am here to help you."),
            'i love you': lambda: speak("I'm sorry, but I am already in a relationship with our team members, Droid."),
            'tell me about your team members': lambda: speak("There are 5 members in our group: Narayan Bogati, Prakash Pun, Nikita Pandey, Krishna Aryal, and Lok Maya."),
            'hello jarvis': lambda: speak("Hello sir, how can I help you today?"),
            'hello jarvis how are you': lambda: speak("I am good. What about you?"),
            'i am also fine': lambda: speak("Oh, really nice to meet you!"),
            'thank you jarvis ': lambda: speak("welcome sir if you need any further help i am always their for you"),
            'you are boy or girl': lambda: speak("sorry for miss understanding i am ai assistance created by narayan for research and develop"),
        'how are you': lambda: speak("I am fine, sir. Thank you for asking. what about you"),
        'what is your name': lambda: speak("My name is Jarvis, develop by droid group in major project"),
        'who made you': lambda: speak("I was created droid members of CTC college"),
        'jarvis who make you': lambda: speak("I was created droid members of CTC college"),
        'who built you': lambda: speak("I was created droid members of CTC college"),
        'tell me about your team member': lambda: speak("There are total 5 members in our groups they are Narayan BOgati Prakash pun Nikita pandey Krishna Aryal"),
            'who is amul sir': lambda: speak("Amul sir is a  young talented person he is genious in computer field and teach in crimson college of technology  and he live in butwal"),
            'who is amol sir': lambda: speak("Amul sir is a  young talented person he is genious in computer field and teach in crimson college of technology and he is married with his wife few year ago and live in butwal"),
    'who is rajiv sir': lambda: speak("Rajeev sir is a multi talented person who has knowledge about Computer hardware networking software etc He is a teacher of crimson college of technology having greate experience to teach he also focus on practical knowledge "),
        'see the time': lambda: speak(f'Sir, the time is {datetime.datetime.now().strftime("%H:%M:%S")}'),
        'time': lambda: speak(f'Sir, the time is {datetime.datetime.now().strftime("%H:%M:%S")}'),
         'open google': lambda: webbrowser.open('https://google.com'),
       
           'shutdown': lambda: shutdown_system(),
        'stop the system': lambda: stop_jarvis(),   
            'jarvis stop the system': lambda: stop_jarvis(),
        'exit': lambda: stop_jarvis(),
         'can i ask some question': lambda: speak("off course why not what do you wan to know "),
         'i have a question': lambda: speak("off course why not what do you wan to know i will help you  "),
          'just tell me who is narayan': lambda: speak("Narayan full name Narayan Bogati he is from pyuthan and he is a skillfull computer engineer hilling from"),
          'tell me about you': lambda: speak("I am jarvis you personal assistant to provide you knowledge and do task execute through voice command and created by droid group"),
         'tell me about yourself': lambda: speak("I am jarvis you personal assistant to provide you knowledge and do task execute through voice command and created by droid group"),
         'introduce yourself': lambda: speak("I am jarvis you personal assistant to provide you knowledge and do task execute through voice command and created by droid group"),
        
            'tell me a joke': lambda: tell_joke(),
           'search in google': lambda: search_in_google(),
           'search in youtube': lambda: search_in_youtube(),
           'open file': lambda: open_file_explorer(),
        'close file': lambda: close_file_explorer(),
        'open command': lambda: open_command_prompt(),
        'close command': lambda: close_command_prompt(),
         'open c drive': lambda: open_c_drive(),
        'open vs code': lambda: open_vs_code(),
        'open camera': lambda: open_camera(),
        'jarvis open camera': lambda: open_camera(),
        'close camera': lambda: close_camera(),
        'open facebook': lambda: speak_and_open('https://www.facebook.com', "Opening facebook"),
        'open youtube': lambda: speak_and_open('https://www.youtube.com', "Opening youtube"),
        'open instagram': lambda: webbrowser.open('https://www.instagram.com'),
        'online shopping': lambda: speak_and_open('https://www.daraz.com.np', "Opening daraz online shopping"),
        'i want to shopping': lambda: speak_and_open('https://www.daraz.com.np', "Opening daraz for online shopping "),
     'check internet speed': lambda: speak_and_open('https://www.fast.com', "opening fast.com to see the speed"),
        'open chat gpt': lambda: webbrowser.open('https://chat.openai.com'),
        'open our website': lambda: webbrowser.open('https://www.narayanbogati.com.np/jarvis_website/final.html'),
         'i want to download you': lambda: webbrowser.open('https://www.narayanbogati.com.np/jarvis_website/final.html') ,
             
         'play the justin bieber song in youtube': lambda: j_song(),    
        'play the justin bieber song': lambda: j_song(),
        'play the relax song': lambda: play_relaxing_song(),
        'play the sushant kc song': lambda: sushant_kc_song(),
        'play the new nepali latest song': lambda: latest_nepali_song(),
        'play nepali song': lambda: latest_nepali_song(),
        'play neplai music': lambda: latest_nepali_song(),
        
        'open narayan youtube channel': lambda: speak_and_open('https://www.youtube.com/@narayanbogati2191', "Opening your YouTube channel."),
        'open github': lambda: speak_and_open('https://github.com/', "Opening GitHub."),
        'open narayan website': lambda: speak_and_open('https://www.narayanbogati.com.np/', "Opening your website."),
        'open email': lambda: speak_and_open('https://mail.google.com/mail/u/0/#inbox', "Opening email"),
        
        
        'play the latest nepali news': lambda: news_nepal(),
        'play nepali news': lambda: news_nepal(),
        'play latest news': lambda: open_latest_news(),
        'play english news': lambda: open_latest_news(),
        'take screenshot': lambda: (speak("Taking screenshot. Please wait."), take_screenshot()),
        
        
        'turn on light': lambda: (speak("Turning on the light."), control_led("on")),
        'turn off light': lambda: (speak("Turning off the light"), control_led("off")),
        'light on': lambda: (speak("Turning on the light."), control_led("on")),
        'light off': lambda: (speak("Turning off the light"), control_led("off")),
        
        'good morning': lambda: good_morning_routine(),
        'good night' : lambda: good_night_routine(),
        
        
        
        
        
        
        
        
        #this is for my friend detail
     'who is vivek': lambda: speak("He is young geneious person and he is from arghakhanchi and he read in diploma in computer engineer"),
    'who is rajendra': lambda: speak("Rajendra also know as ayush and having nickname raju he is orginally from arghakhanchi and live in butwal he is intrested in graphic  designing "),
    'who is aklesh': lambda: speak("aklesh full name Aklesh yadav he is from kapilvastu He read in diploma in computer engineering in CTC college devinagar "),
    'who is nirdesh': lambda: speak("Nirdesh full name nirdesh shrestha he is from butwal and hava a lot of knowledge about compter"),
    'who is vishal': lambda: speak("Bishal full name Bishal Thapa he is from palpa he is talented person and having skill in all field "),
    'who is akash': lambda: speak("Akash full name akash tharu he is from bardiya nepal and he was also talented person "),
    'who is manish': lambda: speak("Manish full name Manish sanjali he has lot of knowledge including physic,chemistry,math and computer he wnat to make a software engineer"),
    'who is nikita': lambda: speak("Nikita full name Nikita pandey she is from butwal and currently reading in CTC college "),
    'who is krishna':  lambda: speak("Hmm i think that his name is Krishna aryal he is from rupakot gulmi he is currently live in divertol butwal and his nickname is kiss you"),
    'who is mausam': lambda: speak("He is from Bankata butwal he has clear 12 class and he currently read in diploma in computer engineering in CTC college"), 
    
            #ending pahase of personal command droid group nb
        }

        # Execute command if it's found in the dictionary
        for command, action in custom_commands.items():
            if command in query:
                action()  # Execute the lambda function for the matched command
                return  # Exit once a command is matched and executed

        # If no command matched, fallback to chatbot
        from engine.features import chatBot
        chatBot(query)
        
        #this is for test
        

    except Exception as e:
        print("Error:", e)
        
        
# Function to fetch and tell a joke by PyJokes
def tell_joke(gui=None):
    joke = pyjokes.get_joke()
    print(f"Here's a joke for you: {joke}")
    speak(f"Here's a joke for you: {joke}")
    
 

        
        
        # Shutdown the system function by Narayan for Windows and Linux
def shutdown_system():
    speak("Shutting down the system.")
    if platform == "win32":
        os.system('shutdown /p /f')
    elif platform in ["linux", "linux2", "darwin"]:
        os.system('poweroff')
    sys.exit()

# To stop the Jarvis program
def stop_jarvis():
    speak("Stopping the system. Goodbye, sir.")
    sys.exit()
    
    # Function to search in Google and open in a new tab
def search_in_google():
    speak("What do you want to search for on Google?")
    search_query = takecommand()
    if search_query != "":
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open_new_tab(url)
    else:
        speak("Sorry, I didn't catch that. Please try again.")
        
        # Search in YouTube function
def search_in_youtube():
    speak("What do you want to search for on YouTube?")
    search_query = takecommand()
    if search_query != "":
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    else:
        speak("Sorry, I didn't catch that. Please try again.")

    # Function to open a file specified by the user
def open_file_explorer():
    speak("Opening File Explorer.")
    if platform == "win32":
        os.startfile('explorer.exe')
    else:
        speak("Sorry, I can only open File Explorer on Windows.")

def close_file_explorer():
    speak("Closing File Explorer.")
    if platform == "win32":
        try:
            os.system('taskkill /F /IM explorer.exe')
            print("File Explorer closed successfully.")
            # Restart File Explorer if needed
            os.system('start explorer.exe')
        except Exception as e:
            print(f"Error closing File Explorer: {e}")
            speak("Failed to close File Explorer.")
    else:
        speak("Sorry, I can only close File Explorer on Windows.")
        

# Function to open the command prompt
def open_command_prompt():
    speak("Opening command prompt.")
    if platform == "win32":
        os.system('start cmd')
    elif platform == "darwin":
        os.system('open -a Terminal')
    elif platform.startswith("linux"):
        os.system('xdg-open terminal')

# Function to close the command prompt
def close_command_prompt():
    speak("Closing command prompt.")
    if platform == "win32":
        try:
            os.system('taskkill /IM cmd.exe /F')
            print("Command Prompt closed successfully.")
        except Exception as e:
            print(f"Error closing Command Prompt: {e}")
            speak("Failed to close Command Prompt.")
    else:
        speak("Sorry, I can only close Command Prompt on Windows.")

# Function to open the C drive
def open_c_drive():
    speak("Opening C drive.")
    if platform == "win32":
        os.system('start C:')
    else:
        speak("Sorry, I can't open C drive on this platform.")


# Function to open Visual Studio Code
def open_vs_code():
    speak("Opening Visual Studio Code.")
    if platform == "win32":
        os.system('code')  # Assumes VS Code is in the PATH
    elif platform == "darwin":
        subprocess.call(['open', '-a', 'Visual Studio Code'])
    elif platform.startswith("linux"):
        subprocess.call(['code'])
        
        
# Function to open the camera
def open_camera():
    speak("Opening the camera.")
    cap = cv2.VideoCapture(0)  # 0 is typically the index for the default camera

    if not cap.isOpened():
        speak("Sorry, I couldn't access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Failed to grab frame.")
            break

        cv2.imshow('Camera', frame)

        # Press 'q' to close the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Function to close the camera
def close_camera():
    speak("Closing the camera.")
    # Assuming this will be called in context where the camera is being displayed
    cv2.destroyAllWindows()
        
        # Function to speak and open URL
def speak_and_open(url, message):
    speak(message)
    webbrowser.open(url)
    
    # Function to play the Justin Bieber song on YouTube
def j_song():
    speak("Playing Justin Bieber song on YouTube.")
    pywhatkit.playonyt("Justin Bieber music")  

def sushant_kc_song():
    speak("Playing Sushant KC song.")
    pywhatkit.playonyt("Sushant KC song")  

def latest_nepali_song():
    speak("Playing latest Nepali song for you.")
    pywhatkit.playonyt("nepali latest song")

# Function to play Nepali news
def news_nepal():
    speak("Playing the latest Nepali news.")
    pywhatkit.playonyt("play the latest nepali news")
    
    # Function to play the relaxing song on YouTube
def play_relaxing_song():
    speak("Playing relaxing song on YouTube.")
    pywhatkit.playonyt("relaxing music")  # This will play the first video that matches "relaxing music" on YouTube

    # Function to open the latest news in the browser
def open_latest_news():
    speak("Opening the latest news in the browser.")
    webbrowser.open('https://news.google.com')



# Function to play the latest news
def play_latest_news():
    speak("Fetching the latest news for you.")
    
    # Function to take a screenshot and save it with the given name
def take_screenshot():
    directory_path = r"C:\Users\Dell\OneDrive\Documents\Desktop\jarvis-main\screenshort"

    # Check if the directory exists; if not, create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    screenshot = pyautogui.screenshot()

    # Ask the user for the screenshot file name
    speak("What would you like to name the screenshot file?")
    name = takecommand()

    # Validate the input and append the correct file extension (.jpg)
    if name and name != "None":
        if not name.endswith(".jpg"):
            name += ".jpg"
        # Save the screenshot to a file with the correct file extension (.jpg)
        screenshot_path = os.path.join(directory_path, name)
        screenshot.save(screenshot_path, format="JPEG")
        speak(f"Screenshot successfully saved as {name} in folder.")
    else:
        speak("Sorry, I didn't catch that. Please try again.")
    
    
    
#this is controlling the light 

# Fix encoding issue
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Resolve ESP32 hostname
def resolve_hostname(hostname):
    try:
        addr_info = socket.getaddrinfo(hostname, None)
        ip_address = addr_info[0][4][0]
        return ip_address
    except socket.gaierror as e:
        print(f"Hostname resolution failed: {e}")
        return None

ESP32_HOSTNAME = "h.local"

# Control the LED on ESP32
def control_led(state):
    esp32_ip = resolve_hostname(ESP32_HOSTNAME)
    if esp32_ip:
        esp32_url = f"http://{esp32_ip}"
        try:
            if state == "on":
                response = requests.get(f"{esp32_url}/led/on")
            elif state == "off":
                response = requests.get(f"{esp32_url}/led/off")
            else:
                raise ValueError("Invalid state. Use 'on' or 'off'.")
            print(response.text)
        except requests.RequestException as e:
            print(f"Error controlling LED: {e}")
    else:
        print("Could not resolve ESP32 hostname.")

# Function to execute the "Good Morning" routine
def good_morning_routine():
    speak("Good morning! Have a great day ahead.")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")
    play_latest_news()
    fetch_weather("Butwal", "1f824e5f2d0cfc5e79cb78476b4c4471")

# Function for the "Good Night" routine
def good_night_routine():
    speak("Good night, sir. Have a wonderful night.")
    # Ask for tomorrow's schedule
    speak("What's the schedule for tomorrow?")
    tomorrow_schedule = takecommand()

    if tomorrow_schedule:
        speak(f"Tomorrow's schedule is: {tomorrow_schedule}")
    else:
        speak("Sorry, I didn't catch that. Please try again.")
        
        
        
        
        # Function to play the latest news
def play_latest_news():
    speak("Fetching the latest news for you.")
    
    # API URL with your actual API key
    url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=773d70adc027421784ceb0ed14a77efb"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        if articles:
            for article in articles[:3]:  # Read out the top 3 articles
                speak(article.get('title', 'No title available'))
                speak("Next news.")
        else:
            speak("Sorry, I couldn't find any news at the moment.")
    else:
        speak("Sorry, I'm unable to fetch the news at the moment.")
    
    speak("See more on the website. Thank you.")
        
        
        # Function to fetch weather information
def fetch_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The weather in {city} is {weather_description}. The temperature is {temp} degrees Celsius.")
        else:
            speak("Unable to fetch weather information at the moment.")
    except Exception as e:
        speak(f"Error fetching weather information: {str(e)}")






#this is the last don't toch it naryan boagti 
    eel.ShowHood()
    
