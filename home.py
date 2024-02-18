import pyttsx3
import speech_recognition as sr

# provide access to TTS
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# defining the voice
engine.setProperty('voice', voices[1].id)

class SmartHome:
    def __init__(self):
        self.doors = []
        self.lights = []
        self.temperature = 25  # Default

    # add door object to the list
    def add_doors(self, door):
        self.doors.append(door)

    # add light object to the list
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
        speak_audio(f"Temperature set to {self.temperature} °C")

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
        speak_audio(f"{self.name} Lights are turned on...")

    def turn_off(self):
        self.is_on = False
        speak_audio(f"{self.name} Lights are turned off...")

# class for door open / close
class Door:
    def __init__(self, name):
        self.name = name
        self.is_open = True

    def door_open(self):
        self.is_open = True
        speak_audio(f"{self.name} is opened...")

    def door_close(self):
        self.is_open = False
        speak_audio(f"{self.name} is closed...")

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
        return 0

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
                door_object = Door(door_name)  # Create a Door object
                home.add_doors(door_object)
                speak_audio(f"{door_name} added successfully.")

        if "open" in query:
            home.open_door()

        if "on" in query:
            home.turn_on_lights()

        if "temperature" in query:
            if "set" in query:
                temperature = query.split("set")[1].strip().split("degrees")[0]
                home.set_temperature(temperature)

        elif "bye" in query:
            speak_audio("Ok, bye")
            exit()

if __name__ == "__main__":
    main()
