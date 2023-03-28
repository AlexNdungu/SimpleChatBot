#Import the needed classes
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create and train the chatbot
my_bot = ChatBot(name='PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

#Create responses
small_talk = [
    'hi there!',
    'hi!',
    'how do you do?',
    'how are you?',
    'i\'m cool',
    'fine, you?',
    'always cool',
    'i\'m okey',
    'glad to hear that.',
    'i\'m fine',
    'i feel awesome',
    'excellent, glad to hear that.',
    'not so good',
    'sorry to hear that',
    'what\'s your name?',
    'i\'m pybot. ask me a math question, please'
]

math_talk_1 = ['pythagorean theorem','a squared plus b squared equals c squared.'
]

math_talk_2 = ['law of cosine', 'c**c = a**2 + b**2 - 2 * a * b * cos(gamma)']

#Train the bot

list_trainer = ListTrainer(my_bot)

#for item in (small_talk, math_talk_1, math_talk_2):
    #list_trainer.train(item)


#Use corpus data
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

#Test the bot using get_response
print(my_bot.get_response("hi"))