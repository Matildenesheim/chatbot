import pyttsx3
import speech_recognition as sr
import os
import random
import string
import wikipedia
import webbrowser
import keyboard
import datetime
from pygame import mixer



# Initializing microphone and speech recognition system
mic = sr.Microphone()
#r = sr.Recognizer()

# Using the simplest voice engine we can to do text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices') # if you get a weird accent, try printing this variable and choose another voice
engine.setProperty('voice', voices[0].id) # a different voice id might be necessary on your system

# Introduction: let Paul introduce himself
engine.say("Hi there! My name is Paul Botcuse but you can call me Paul. "
           "I am your new assistant, at your service "
           "I will help you improve your cake baking skills in times of crisis "
           "I specialise in cake recipes for these sad corona times. I know you need the comfort food. "
          #  "You can ask me for Ingredients and Instructions for five different cake recipes. Awesome innit? "
          #  "I will be reading line by line, simply tell me next to read the following line. "
          #  "You can also ask me some different questions "
            "Let's start shall we?")
# the following line is important for the engine to actually say something.
engine.runAndWait()

# What can your app do?
# Making this more colloquial 
#engine.say("I specialise in cake recipes for these sad corona times. I know you need the comfort food. "
      #   "You can ask me for Ingredients and Instructions for five different cake recipes. Awesome innit? "
      #  "I will be reading line by line, simply tell me next to read the following line. "
      #  "You can also ask me some different questions "
     #    "Let's start shall we?")
#engine.runAndWait()

# First: Initialize the recipe:
print("So.. What can I do for you today?")
engine.say("So.. What can I do for you today?")
engine.runAndWait()
# open the files
# files for 5 cake recipes 
ing_file = open(os.path.join('Recipes', 'french pound cake', 'ingredients.txt'), "r")
inst_file = open(os.path.join('Recipes', 'french pound cake', 'instructions.txt'), "r")
cake_ing_file = open(os.path.join('Recipes', 'chocolate cake', 'chococakeingredients.txt'), "r")
cake_inst_file = open(os.path.join('Recipes', 'chocolate cake', 'chococakeinstructions.txt'), "r")
bb_ing_file = open(os.path.join('Recipes', 'banana bread', 'bananabreadingredients.txt'), "r")
bb_inst_file =  open(os.path.join('Recipes', 'banana bread', 'bananabreadinstructions.txt'), "r")
ac_ing_file = open(os.path.join('Recipes', 'apple cake', 'applecakeingredients.txt'), "r")
ac_inst_file = open(os.path.join('Recipes', 'apple cake', 'applecakeinstructions.txt'), "r")
vc_ing_file = open(os.path.join('Recipes', 'vanilla cake', 'vanillacakeingredients.txt'), "r")
vc_inst_file = open(os.path.join('Recipes', 'vanilla cake', 'vanillacakeinstructions.txt'), "r")

# greeting file with selection of greetings that are randomly seleted, makes this more exciting and interactive
greeting_file = open(os.path.join('greeting.txt'),"r")
fun_file = open(os.path.join('funfacts.txt'),"r")

# create lists of sentences
ing_list = ing_file.readlines()
inst_list = inst_file.readlines()
cake_ing_list = cake_ing_file.readlines()
cake_inst_list = cake_inst_file.readlines()
bb_ing_list = bb_ing_file.readlines()
bb_inst_list = bb_inst_file.readlines()
ac_ing_list = ac_ing_file.readlines()
ac_inst_list = ac_inst_file.readlines()
vc_ing_list = vc_ing_file.readlines()
vc_inst_list = vc_inst_file.readlines()
greeting_list = greeting_file.readlines()
fun_list = fun_file.readlines()

# Close files
ing_file.close()
inst_file.close()
cake_ing_file.close()
cake_inst_file.close()
bb_ing_file.close()
bb_inst_file.close()
ac_ing_file.close()
ac_inst_file.close()
vc_ing_file.close()
vc_inst_file.close()
greeting_file.close()
fun_file.close()

# Second: Initialize dynamic variables
active_list = ing_list # we start by iterating through the ingredient list
active_list_inst = inst_list 
i = 0 # the counter we use to read through our list
textInput = "nothing" # we initialise the input for the loop to work



# variables for greetings, goodbye and small talk 
greeting1 = ['hi','how are you', 'are you','how are you doing','doing','how are','hi how are you','hi are you']
greeting2 = ['good', 'thank you', 'good thank you','thank','I am good','Im good thank you',"I'm good thank you", 'I am good thank you']
next1 = ['next', 'next please', 'next next', 'go next', 'next one','list the next']
repeat = ['can you repeat that', 'repeat','cheat','repeat','repeat please','repeat that','can you repeat','you repeat']
bye = ['thank you goodbye','thank you bye','thank you that is it goodbye','thank you that is it bye','exit', 'close', 'goodbye', 'nothing','bye','ok goodbye','ok bye','thats it for today goodbye','today goodbye','that is it for today goodbye','thats it for today bye','that is it for today bye','for today bye','for today goodbye','it for today','it for today bye','it for today goodbye']
which_recipes = ['what recipes do you have', 'recipe do you have','recipes do you have','recipe','which recipes do you have','what cake can I make','what cakes', 'please can I make','please do you have','do you have','can I make','what kind of cake can i make']

# variables for cakes 
frenchcake_inst = ['list the French cake ingredients','yes list French pound cake instructions', 'list French pound cake instructions', 'French pound cake instructions', 'French cake instructions', 'French cake instruction','list french cake instructions', 'pound cake instruction','list French pound cake instruction', 'list French cake instruction', 'pound cake instruction']
frenchcake_ing = ['yes list French pound cake ingredients','list French pound cake ingredients', 'French ingredients', 'pound cake ingredients','list French pound cake ingredient', 'French ingredient','pancake ingredients','pancake ingredient', 'pound cake ingredient','French pound cake ingredients','French pound cake ingredient','French cake ingredients','French cake ingredient']

chocolate_inst = ['yes list chocolate cake instructions','list chocolate instructions','list chocolate cake instructions','chocolate cake instructions','list chocolate cake instruction','chocolate cake instruction','chocolate instructions','chocolate instruction']
chocolate_ing = ['yes list chocolate cake ingredients', 'list chocolate ingredients','list chocolate cake ingredients','chocolate cake ingredients','list chocolate cake ingredient','chocolate cake ingredient','chocolate ingredients','chocolate ingredient']

banana_inst = ['yes list banana bread instructions','list banana bread instructions','banana bread instructions','list banana bread instruction','banana bread instruction','banana instructions','banana instruction','bread instruction','bread instructions']
banana_ing = ['yes list banana bread ingredients','yes list the banana bread ingredients','list banana bread ingredients','banana bread ingredients','list banana bread ingredient','banana bread ingredient','banana ingredients','banana ingredient','bread ingredient','bread ingredients']

apple_inst = ['yes list apple cake instructions','list apple cake instructions','apple cake instructions','list apple cake instruction','apple cake instruction','apple instructions','apple instruction']
apple_ing = ['yes list apple cake ingredients','list apple cake ingredients','apple cake ingredients','list apple cake ingredient','apple cake ingredient','apple ingredients','apple ingredient']

vanilla_inst = ['yes list vanilla cake instructions','list vanilla cake instructions','vanilla cake instructions','list vanilla cake instruction','vanilla cake instruction','vanilla instructions','vanilla instruction']
vanilla_ing = ['yes list vanilla cake ingredients','list vanilla cake ingredients','vanilla cake ingredients','list vanilla cake ingredient','vanilla cake ingredient','vanilla ingredients','vanilla ingredient']

# variables for funny stuff 
creator = ['who is your creator','creator','inventor','who is your inventor','your creator','your inventor','is your creator','is your inventor']
destroyhuman = ['will you destroy humankind',' who destroyed humankind','destroy humankind','destroy human','humankind','destroy','humankind','human','you destroy human','you destroy humankind']
jokes = ['ok tell a joke','ok tell a joke then','tell a joke','joke','a joke','tell','ok tell me a joke then','tell a joke then','joke then',]
jokes2 = ['yes tell one more','yes another one','yes tell another','ok one more joke','tell another','another one']
alexa = ['no who do you like best Alexa or Siri','Alexa or Siri','Siri','Alexa','Siri or Alexa','like best Alexa or Siri','who do you like best Alexa or Siri']
time = ['what is the time','what time is it','time is it','time','what time is','do you know what time it is']
funfacts = ['tell a fun fact','do you know any fun facts','any fun facts','fun facts','tell me something I dont know', 'can you fun facts','telephone fact','telephone facts','can you fun fatc', 'do not know','tell me something I do not know','dont know','fun fact','tell me a fun fact','tell me fun facts','do you know any fun fact','can you tell me a fun fact','can you tell me fun facts','fun fact again','fun facts again','again','one more fun fact','more fun fact','more fun facts']
song = ['my favorite song','can I have a favourite song','do you have a favourite song','song','what is your favourite song','favourite song','favourite','a favourite song']


# All interactions happen here
while textInput != "stop":
    now = datetime.datetime.now()
    # We load the speech to text model
    r = sr.Recognizer()
    # check for background noise and adjust sensitivity accordingly
    with mic as source:
        audio = r.adjust_for_ambient_noise(source)

    # Listen for user input
    print("I am listening")
    engine.say("I am listening")
    engine.runAndWait()
    with mic as source:
        audio = r.listen(source) # save the mic input into the "audio" variable
    print("processing...")
  #  i = ""

    # This "try" statements allow us to handle exception
    # This means we don't necessarily crash if we get an error
    try:
        # speech to text: transform the audio recorded from the mic into text
        textInput = r.recognize_google(audio)
        print("you said: " + textInput)

# put in more than one option of text input to make it more flexible and easier 
        if textInput in frenchcake_ing:
            active_list = ing_list
            i = 0
            response = "Yummi. I will now read ingredients for the french pound cake, say next to start"

        elif textInput in frenchcake_inst:
            active_list = inst_list
            i = 0
            response = "Yummi. I will now read the instructions for the french pound cake, say next to start"

        elif textInput in chocolate_ing:
            active_list = cake_ing_list
            i = 0
            response = "Yummi. I will now read ingredients for chocolate cake, say next to start"

        elif textInput in chocolate_inst:
            active_list = cake_inst_list
            i = 0
            response = "Mmm. I will now read the instructions for the chocolate cake, say next to start"

        elif textInput in banana_ing:
            active_list = bb_ing_list
            i = 0
            response = "Yummi. I will now read ingredients for banana bread, say next to start"

        elif textInput in banana_inst:
            active_list = bb_inst_list
            i = 0
            response = "Mmm. I will now read the instructions for the banana bread, say next to start"

        elif textInput in apple_ing:
            active_list = ac_ing_list
            i = 0
            response = "Yummi. I will now read ingredients for apple cake, say next to start"

        elif textInput in apple_inst:
            active_list = ac_inst_list
            i = 0
            response = "Mmm. I will now read the instructions for the apple cake, say next to start"

        elif textInput in vanilla_ing:
            active_list = vc_ing_list
            i = 0
            response = "Yummi. I will now read ingredients for vanilla cake, say next to start"

        elif textInput in vanilla_inst:
            active_list = vc_inst_list
            i = 0
            response = "Mmm. I will now read the instructions for the vanilla cake, say next to start"

## selects randomly from a list of greetings to make it more variable and fun. 
        elif textInput in greeting1:
            response = random.choice(greeting_list)
        
        elif textInput in greeting2:
            response = "Glad to hear that. What can I do for you? I have 5 different cakes I can present or you can ask me some questions if you like. Awesome innit? "

# again, more options of how to say next 
        elif textInput in next1:
            response = active_list[i]
            i += 1
        
        elif textInput in repeat:
            response = active_list[i-1]
            i = 1 
        
        elif textInput in which_recipes:
            response = "I have the recipes for a french pound cake, chocolate cake, banana bread, apple cake and vanilla cake. Do you want to make one? "

# random questions for fun
        elif textInput in creator:
            response = "That's Caroline, Alberte and Matilde. They are great. Virtual hug for you guys "
        
        elif textInput in destroyhuman:
            response = "Only with my funny jokes. Ask me for one. "
        
        elif textInput in jokes:
            response = "Alright. I ate a clock yesterday. It was very time consuming. Ha ha. Do you want one more? "
        
        elif textInput in jokes2:
            response = "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away. Ha ha "

        elif textInput in alexa:
            response = "Thats an easy question. Alexa is my girl. Siri got nothing on me "
        
        elif textInput in time:
            response = now.strftime("The time is %H:%M")
        
        elif textInput in funfacts:
            response = random.choice(fun_list)
        
        elif textInput in song:
            response = "My favorite song? That must be this one. Let me play it for you. "
            mixer.init()
            mixer.music.load("/Users/matildenesheim/Desktop/OneDrive/Cognitive_Science_Master/secondsemester/HCI/PaulBotcuse/cogscisong.mp3")
            mixer.music.play(10)
             
            

# goodbye
        
        elif textInput in bye:
            print('Goodbye. Hope you have a good day. Talk to you soon.')
            engine.say('Goodbye. Hope you have a good day. Talk to you soon.')
            engine.runAndWait()
            exit()



# need to try and get the word stop to interrupt the chatbot when it is talking

        else:
           response = "I am sorry, I didn't get that. " \
                      "Can you repeat please?"


# attempt at getting it to google search, but this replaces the "i didn't understand you" function, don't know how to have both? 
        #else: 
         #   response = "Give me a second, I'll look it up"
          #  print(wikipedia.summary(r.recognize_google(audio)))
           # engine.say(wikipedia.summary(r.recognize_google(audio)))
            #engine.runAndWait()
            #webbrowser.open_new('www.google.com/search?q=' + textInput)
        
    
    # API was unreachable or unresponsive:
    except sr.RequestError:
        response = "API unavailable"
    # if the speech was unintelligible:
    except sr.UnknownValueError:
        response = "Sorry! I didn't quite get that. " \
                   "Can you repeat please?"
    # if you arrive at the end of the list:
    except IndexError:
        response = "There is nothing left in this list. " \
                   "You can ask me for the list of Ingredients by saying Ingredients. " \
                    "You can ask me for the list of instructions by saying Instructions. "

    print(response)
    def onWord(name, location, length):
        print('word', name, location, length)
        if keyboard.is_pressed("esc"):
            engine.stop()
        engine.connect('started-word', onWord)
    engine.say(response)
    engine.runAndWait()

