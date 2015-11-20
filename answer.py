from chatterbotapi import ChatterBotFactory, ChatterBotType
import HTMLParser

h = HTMLParser.HTMLParser()
factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'ea373c261e3458c6')
bot2session = bot2.create_session()

def getAnswer(question,engine):
	print("User asked: "+question)
	if engine == '2':
		s = question.encode('utf-8').strip()	
		s = bot2session.think(s)
		s = h.unescape(s).encode('utf-8').strip()
	else:
		s = question.encode('utf-8').strip()	
		s = bot1session.think(s)
		s = h.unescape(s).encode('utf-8').strip()

	print("Answered: "+s+"; with engine "+str(engine))
	return s

