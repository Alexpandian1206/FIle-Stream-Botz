# (c) github - @Illegal_Developer ,telegram - https://telegram.me/Illegal_Developer
# removing credits dont make you coder 

from Adarsh.vars import Var
from Adarsh.bot import StreamBot
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.file_properties import get_file_ids
from Adarsh.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp
import re
import random
from jinja2 import Environment, FileSystemLoader

async def render_page(id, secure_hash):

def render_template():
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('req.html')

    # Data to pass into the template
    data = {
        'title': 'Aklinksz',
        'site_name': 'Aklinksz',
        'home_submenu': [
            {'id': 'welcome', 'name': 'WELCOME', 'active': True},
            {'id': 'channels', 'name': 'CHANNELS & BOTZ', 'active': False},
            {'id': 'talk', 'name': 'LET\'S TALK', 'active': False},
        ],
        'home_sections': [
            {'id': 'welcome', 'content': 'This is the Welcome content.', 'active': True},
            {'id': 'channels', 'content': 'This is the Channels & Botz content.', 'active': False},
            {'id': 'talk', 'content': 'This is the Let\'s Talk content.', 'active': False},
        ],
        'about_submenu': [
            {'id': 'welcomeAbout', 'name': 'WELCOME', 'active': True},
            {'id': 'channelsAbout', 'name': 'CHANNELS & BOTZ', 'active': False},
            {'id': 'talkAbout', 'name': 'LET\'S TALK', 'active': False},
        ],
        'about_sections': [
            {'id': 'welcomeAbout', 'content': 'This is the About Welcome content.', 'active': True},
            {'id': 'channelsAbout', 'content': 'This is the About Channels & Botz content.', 'active': False},
            {'id': 'talkAbout', 'content': 'This is the About Let\'s Talk content.', 'active': False},
        ]
    }

    # Render the template with the data
    html_output = template.render(data)

    # Save or output the rendered HTML
    with open('output.html', 'w') as file:
        file.write(html_output)

# Call the function to execute it
render_template()

    
    # Get file data based on ID
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))

    # Validate the hash
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'Link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with ID {id}")
        raise InvalidHash

    # Construct source URL and file tag
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    tag = file_data.mime_type.split('/')[0].strip()

    # Original button links
    download_link = [f'{Var.ADS_LINK_1}', f'{src}', f'{Var.ADS_LINK_2}']

    # Randomize button links
    download_link = random.sample(download_link, len(download_link))

    # Telegram button links only
    telegram_links = [f'{Var.ADS_LINK_1}', f'{Var.ADS_LINK_2}', f'https://telegram.me/{Var.SECOND_BOTUSERNAME}?start=file_{id}']

    # Randomize Telegram button links
    telegram_links = random.sample(telegram_links, len(telegram_links))

    # Read and format HTML template
    async with aiofiles.open('Adarsh/template/req.html') as r:
        heading = 'Watch {}'.format(file_data.file_name)
        html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)

    # Create the download button HTML
    download_button_html = f'''
    <style>
        .button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }}
        .button-container button {{
            background-color: #FFC107; /* Bootstrap warning color */
            color: black;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            margin: 10px 0; /* Margin for vertical spacing */
            width: 200px;
        }}
        .button-container button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
    </style>
    <div class="button-container">
        <button onclick="window.location.href='{download_link[0]}'">sᴇʀᴠᴇʀ 1</button>
        <button onclick="window.location.href='{download_link[1]}'">sᴇʀᴠᴇʀ 2</button>
        <button onclick="window.location.href='{download_link[2]}'">sᴇʀᴠᴇʀ 3</button>
    </div>
    '''

    # Create the Telegram button HTML
    telegram_button_html = f'''
    <style>
        .telegram-button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }}
        .telegram-button-container button {{
            background-color: #FFC107; /* Bootstrap warning color */
            color: black;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            margin: 8px 0;
            width: 80%;
            max-width: 300px;
        }}
        .telegram-button-container button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
    </style>
    <div class="telegram-button-container">
        <button onclick="window.location.href='{telegram_links[0]}'">Telegram Server 1</button>
        <button onclick="window.location.href='{telegram_links[1]}'">Telegram Server 2</button>
        <button onclick="window.location.href='{telegram_links[2]}'">Telegram Server 3</button>
    </div>
    '''

    # Insert the download and telegram button HTML into the template
    html = html.replace('{download_button}', download_button_html)
    html = html.replace('{telegram_button}', telegram_button_html)

    return html





async def media_watch(id):
    # Get file data based on ID
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))

    # Validate the hash
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'Link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with ID {id}")
        raise InvalidHash

    # Construct source URL and file tag
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    tag = file_data.mime_type.split('/')[0].strip()

    # Original button links
    download_link = [f'{Var.ADS_LINK_1}', f'{src}', f'{Var.ADS_LINK_2}']

    # Randomize button links
    download_link = random.sample(download_link, len(download_link))

    # Telegram button links only
    telegram_links = [f'{Var.ADS_LINK_1}', f'{Var.ADS_LINK_2}', f'https://telegram.me/{Var.SECOND_BOTUSERNAME}?start=file_{id}']

    # Randomize Telegram button links
    telegram_links = random.sample(telegram_links, len(telegram_links))

    # Read and format HTML template
    async with aiofiles.open('Adarsh/template/req.html') as r:
        heading = 'Watch {}'.format(file_data.file_name)
        html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)

    # Create the download button HTML
    download_button_html = f'''
    <style>
        .button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }}
        .button-container button {{
            background-color: #FFC107; /* Bootstrap warning color */
            color: black;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            margin: 10px 0; /* Margin for vertical spacing */
            width: 200px;
        }}
        .button-container button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
    </style>
    <div class="button-container">
        <button onclick="window.location.href='{download_link[0]}'">sᴇʀᴠᴇʀ 1</button>
        <button onclick="window.location.href='{download_link[1]}'">sᴇʀᴠᴇʀ 2</button>
        <button onclick="window.location.href='{download_link[2]}'">sᴇʀᴠᴇʀ 3</button>
    </div>
    '''

    # Create the Telegram button HTML
    telegram_button_html = f'''
    <style>
        .telegram-button-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }}
        .telegram-button-container button {{
            background-color: #FFC107; /* Bootstrap warning color */
            color: black;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            margin: 8px 0;
            width: 80%;
            max-width: 300px;
        }}
        .telegram-button-container button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
    </style>
    <div class="telegram-button-container">
        <button onclick="window.location.href='{telegram_links[0]}'">Telegram Server 1</button>
        <button onclick="window.location.href='{telegram_links[1]}'">Telegram Server 2</button>
        <button onclick="window.location.href='{telegram_links[2]}'">Telegram Server 3</button>
    </div>
    '''

    # Insert the download and telegram button HTML into the template
    html = html.replace('{download_button}', download_button_html)
    html = html.replace('{telegram_button}', telegram_button_html)
    
    return html

# (c) github - @Rishikesh-Sharma09 ,telegram - @Rk_botz
async def batch_page(message_id):
    # Get message with list of IDs
    GetMessage = await StreamBot.get_messages(chat_id=Var.BATCH_CHANNEL, message_ids=message_id)
    message_ids = GetMessage.text.split(" ")
    print(f"Message IDs: {message_ids}")

    links_with_names = []
    for message_id in message_ids:
        file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(message_id))
        secure_hash = file_data.unique_id[:6]
        link = f"{Var.URL}watch/{message_id}"
        file_name = re.sub(r'[-_.]', ' ', file_data.file_name).title()
        links_with_names.append((file_name, link))

    # Read and format batch HTML template
    async with aiofiles.open('Adarsh/template/batch.html') as r:
        template = await r.read()

    buttons_html = ''
    for file_name, link in links_with_names:
        buttons_html += f'<li>' \
                        f'<form action="{link}" method="get" style="text-align: center;">' \
                        f'<button class="button" type="submit" style="text-align: center;">' \
                        f'<div class="file-name" style="text-align: center;">' \
                        f'<p id="myDiv" style="text-align: center;">' \
                        f'<h4 style="color:#F33A6A; text-align: center;">File Name:</h4><br> ' \
                        f'<span style="color:white; text-align: center;">{file_name}</span></p></div></button></form>' \
                        f'</li><br><p>&nbsp;</p>'

    html_code = template.replace('{links_placeholder}', buttons_html)
    return html_code

