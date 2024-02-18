import pyttsx3
import speech_recognition as sr

# provide access to TTS
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# defining the voice
engine.setProperty('voice', voices[1].id)

class SmartHome:
    def __init__(self):
        self.doors = ["main door"]
        self.lights = ["main light"]
        self.temperature = 25  # Default

    # add door name to the list
    def add_doors(self, door):
        self.doors.append(door)

    # add light name to the list
    def add_lights(self, light):
        self.lights.append(light)
    
    # for open the door
    def open_door(self):
        for door in self.doors:
            door.door_open()

    # for close the door
    def close_door(self):
        for door in self.doors:
            door.door_close()

    # for on the light
    def turn_on_lights(self):
        for light in self.lights:
            light.turn_on()
    
    # for off the light
    def turn_off_lights(self):
        for light in self.lights:
            light.turn_off()

    # set temperature
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature} °C")

    # get current temperature
    def get_temperature(self):
        return self.temperature

# class for lights on / off
class Light:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} Lights are turned on...")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} Lights are turned off...")

# class for door open / close
class Door:
    def __init__(self, name):
        self.name = name
        self.is_open = True

    def door_open(self):
        self.is_open = True
        print(f"{self.name} Door is opened...")

    def door_close(self):
        self.is_open = False
        print(f"{self.name} Door is closed...")

# for speak words
def speak_audio(audio):
    engine.say(audio)
    engine.runAndWait()

# getting commands from microphone
def take_command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except Exception as e:
        print(e)
        speak_audio("I didn't understand.")
        return "None"
    return query

def main():
    home = SmartHome()

    while True:
        query = take_command().lower()

        if "hello voice assistant" in query:
            speak_audio("Yes, I am here. How can I help you?")

        if "adding" in query:
            if "door" in query:
                door_name = query.split("adding")[1].strip()
                home.add_doors(door_name)
                speak_audio(f"{door_name} added successfully.")

        if "open" in query:
            for door in home.doors:
                if door in query:
                    speak_audio(f"{door} Door is opened")
                    home.open_door()
                    break
        if "on" in query:
            for light in home.lights:
                if light in query:
                    speak_audio(f"{light} is turned on")
                    home.turn_on_lights()
                    break

        if "temperature" in query:
            if "set" in query:
                temperature = int(query.split("set")[1].strip().split("degrees")[0])
                home.set_temperature(temperature)
                break

        elif "bye" in query:
            speak_audio("Ok, bye")
            exit()

if __name__ == "__main__":
    main()
