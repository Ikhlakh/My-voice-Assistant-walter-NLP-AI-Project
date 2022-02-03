

Listner = sr.Recognizer()

# Use pyttsx3 to speak audio by robot that it tell about herself
engine = pyttsx3.init()
engine. setProperty("rate", 150)
engine.say("I am Walter your Assistant ")
engine.runAndWait()

def engine_talk(text)   :
    engine.say(text)
    engine.runAndWait()


# Function For Weather



def user_commands():
    try:
        with sr.Microphone() as source:
            print(" Sir Please Start Speaking ")
            voice =Listner.listen(source)

            # listen command which we tell ,convert into text ,and also conver into
            # lower text .

            command = Listner.recognize_google(voice)
            command = command.lower()
            if "walter" in command:
                command = command.replace("walter","")
                print(command)
    except:
        pass
    return command

def action_walter():
    command = user_commands()
    if 'play' in command:
        command =command.replace("play","")
        engine_talk('playing' +command)
        # print('playing' +command)

        # now use pywhatkit for playing music ,send msg etc.
        pywhatkit.playonyt(command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        engine_talk("the current time is " +time)

    # elif 'shutdown' in command:
    #     command = command.replace("shutdown","")
    #     command = command.replace("laptop","")
    #     command = command.replace("in","")
    #     command = command.replace("second","")
    #     command = command.replace("my", "")
    #     command = command.replace("this", "")
    #     command = command.replace("system", "")
    #     engine_talk('going to shutdown' +command)
    #     pywhatkit.shutdown(10)


    elif 'screenshot' in command:
        command = command.replace("take", "")
        engine_talk('wait i am taking ' + command)
        pywhatkit.take_screenshot(command , 5)

    # Using wwikipedia Library here
    elif 'what is' in command:
        command = command.replace("what is", "")
        info = wikipedia.summary(command,1)
        print(info)
        engine_talk(info)

    elif 'who is' in command:
        command = command.replace("who is", "")
        info = wikipedia.summary(command, 1)
        print(info)
        engine_talk(info)

    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())


    elif 'weather' in command:

        def weather(location):
            user_api = "de4b710a52e8cc76c1987c26e553cab7"

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            # create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            print("-------------------------------------------------------------")
            print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
            print("-------------------------------------------------------------")

            print("Current temperature is: {:.2f} deg C".format(temp_city))
            print("Current weather desc  :", weather_desc)
            print("Current Humidity      :", hmdt, '%')
            print("Current wind speed    :", wind_spd, 'kmph')


            engine_talk("weather of " + command)
            engine_talk(("Current temperature is: {:.2f} deg C".format(temp_city)))
            engine_talk(("Current weather desc  :", weather_desc))
            engine_talk(("Current Humidity      :", hmdt, '%'))
            engine_talk(("Current wind speed    :", wind_spd, 'kmph'))

            return location

        command = command.replace("weather", "")
        command = command.replace("in", "")
        command = command.replace("of", "")
        command = command.replace("today", "")
        print(command)

        weather(command)


    else:
        print("i Could not hear Properly")


action_walter()