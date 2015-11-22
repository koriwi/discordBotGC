import discord
import copy
import joke
import answer



client = discord.Client()
client.login('kilian2798+bot@gmail.com', '')
channel = discord.Channel()
talk = None
server = discord.Server()
botengine = 1


@client.event
def on_message(message):

    global talk
    global channel
    global botengine

    if message.content.startswith('?bot'):

        answertext = answer.getAnswer(message.content[4:],botengine)
        client.send_message(message.channel, answertext, tts=talk)

    if message.content.startswith('!bot'):
        sender = message.author
 
        if len(message.content) == 4:
	        client.send_message(message.channel, 'Ja ?',tts=talk)
	        return 0
        
        role = discord.utils.find(lambda r: r.name == 'admins', sender.roles)

        if 'joke' in message.content:
                joketext = joke.getJoke()
                client.send_message(message.channel,joketext, tts=talk)

        if role:
            print('he is admin')
            print(message.content)
            

            if 'tts_off' in message.content:
                talk = False
                print(talk)
                client.send_message(message.channel, 'Ok, bin ruhig',tts=talk)
            
            if 'tts_on' in message.content:
                talk = True
                print(talk)
                client.send_message(message.channel, 'Ok, TTS aktiviert',tts=talk)
            
            if 'default_channel' in message.content:
                tempchannel = discord.Channel
                tempchannel = discord.utils.find(lambda c: c.name == message.content[21:], server.channels)
        
                if tempchannel:
                    
                    client.send_message(channel, "Ok, ich schreibe jetzt in "+tempchannel.name)
                    
                    channel = tempchannel

            if 'botengine' in message.content:
                botengine = message.content[14:]
                client.send_message(message.channel,"Ok, Botengine ist "+str(botengine),tts=talk)

@client.event
def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    global channel 
    channel = discord.utils.find(lambda c: c.name == 'bot', client.servers[0].channels)
    print('default channel is ' + channel.name)
    
    global talk
    talk = False
    
    global server
    server = copy.deepcopy(client.servers[0])

@client.event
def on_message_edit(b,a):

    if a.content != b.content:
        client.send_message(a.channel, 'Da hat sich jemand verschrieben')

@client.event
def on_voice_state_update(member):

    print(member.name)
    
    global server
    oldmember = discord.utils.find(lambda o: o.name == member.name, server.members)
    print("debug 00")
    print((member.voice_channel== None) != (oldmember.voice_channel==None))
    print("old:"+oldmember.name)
    if (member.voice_channel== None) != (oldmember.voice_channel==None):
        print("debug 01: ")
        print(member.voice_channel!=None)
        if member.voice_channel!=None:
            print(member.name+" came on")  
            client.send_message(channel, member.name + ' ist da',tts=talk)
        else:
            client.send_message(channel, member.name + ' ist abgehauen',tts=talk)
        server = copy.deepcopy(client.servers[0])

client.accept_invite('https://discord.gg/0ZpO4yiQuM8YaQ8Z')
client.run()
