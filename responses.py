import random
import discord

async def send_message(author, message, user_message):
    try:
        command = user_message[2:]
        if command.lower() == 'hello':
            await message.channel.send(f'Hello {message.author.mention}')
        else:
            response = get_response(author, command)
            await message.channel.send(response)

    except Exception as e:
        print(end='')

def get_response(username:str, message: str) -> str:
    p_message = message.lower()

    if message == 'roll':
        return '주사위(1~6): ' + str(random.randint(1, 6))
    
    if message == '잰추':
        return '쀽쀽!'
        
    else:
        return 'Command Error' 

