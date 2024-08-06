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

async def render_page(id, secure_hash):
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
    links1 = [f'{Var.ADS_LINK_1}', f'{src}', f'{Var.ADS_LINK_2}']
    links2 = [f'{Var.ADS_LINK_1}', f'{Var.ADS_LINK_2}', f'https://telegram.me/{Var.SECOND_BOTUSERNAME}?start=file_{id}']

    # Randomize button links
    links1 = random.sample(links1, len(links1))
    links2 = random.sample(links2, len(links2))

    # Read and format HTML template
    async with aiofiles.open('Adarsh/template/req.html') as r:
        heading = 'Watch {}'.format(file_data.file_name)
        html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)

    # Add primary button with CSS and modal
    primary_button_html = f'''
    <style>
        .primary-button {{
            background-color: #FFC107; /* Bootstrap warning color */
            color: black;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .primary-button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
        .modal {{
            display: none; /* Hidden initially */
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.4);
        }}
        .modal-content {{
            background-color: #fefefe;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
            border-radius: 20px;
            position: relative;
        }}
        .modal-content h1 {{
            text-align: center;
            color: #333;
            font-weight: bold;
        }}
        .close {{
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }}
        .close:hover,
        .close:focus {{
            color: black;
            text-decoration: none;
            cursor: pointer;
        }}
        .button-container {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
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
            margin: 4px;
        }}
        .button-container button:hover {{
            background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }}
    </style>
    <div class="primary-button" onclick="document.getElementById('myModal').style.display='block'">
        OPEN - LINK
    </div>
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="document.getElementById('myModal').style.display='none'">&times;</span>
            <h1>👇🏻 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙷𝙴𝚁𝙴👇🏻</h1>
            <div class="button-container">
                <button onclick="window.location.href='{links1[0]}'">sᴇʀᴠᴇʀ 1</button>
                <button onclick="window.location.href='{links1[1]}'">sᴇʀᴠᴇʀ 2</button>
                <button onclick="window.location.href='{links1[2]}'">sᴇʀᴠᴇʀ 3</button>
            </div>
            <h1>👇🏻 𝙶𝙴𝚃 𝙷𝙴𝚁𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴 👇🏻</h1>
            <div class="button-container">
                <button onclick="window.location.href='{links2[0]}'">sᴇʀᴠᴇʀ 1</button>
                <button onclick="window.location.href='{links2[1]}'">sᴇʀᴠᴇʀ 2</button>
                <button onclick="window.location.href='{links2[2]}'">sᴇʀᴠᴇʀ 3</button>
            </div>
        </div>
    </div>
    '''

    # Insert primary button HTML into the template
    html = html.replace('{new_button}', primary_button_html)
    return html

async def media_watch(id):
    # Get file data based on ID
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    file_name, mime_type = file_data.file_name, file_data.mime_type
    secure_hash = file_data.unique_id[:6]
    src = urllib.parse.urljoin(Var.URL, f'{str(id)}')
    tag = file_data.mime_type.split('/')[0].strip()

    # Original button links
    links1 = [f'{Var.ADS_LINK_1}', f'{src}', f'{Var.ADS_LINK_2}']
    links2 = [f'{Var.ADS_LINK_1}', f'{Var.ADS_LINK_2}', f'https://telegram.me/{Var.SECOND_BOTUSERNAME}?start=file_{id}']

    # Randomize button links
    links1 = random.sample(links1, len(links1))
    links2 = random.sample(links2, len(links2))

    if tag == 'video':
        # Read and format HTML template
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Watch - {}'.format(file_name)
            html = (await r.read()).replace('tag', tag) % (heading, file_name, src)

            # Add primary button with CSS and modal
            primary_button_html = f'''
            <style>
                .primary-button {{
                    background-color: #FFC107; /* Bootstrap warning color */
                    color: black;
                    font-weight: bold;
                    text-align: center;
                    padding: 15px;
                    border-radius: 20px;
                    cursor: pointer;
                    transition: all 0.3s;
                }}
                .primary-button:hover {{
                    background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    transform: translateY(-5px);
                }}
                .modal {{
                    display: none; /* Hidden initially */
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    background-color: rgb(0,0,0);
                    background-color: rgba(0,0,0,0.4);
                }}
                .modal-content {{
                    background-color: #fefefe;
                    margin: 15% auto;
                    padding: 20px;
                    border: 1px solid #888;
                    width: 80%;
                    border-radius: 20px;
                    position: relative;
                }}
                .modal-content h1 {{
                    text-align: center;
                    color: #333;
                    font-weight: bold;
                }}
                .close {{
                    color: #aaa;
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                }}
                .close:hover,
                .close:focus {{
                    color: black;
                    text-decoration: none;
                    cursor: pointer;
                }}
                .button-container {{
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
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
                    margin: 4px;
                }}
                .button-container button:hover {{
                    background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    transform: translateY(-5px);
                }}
            </style>
            <div class="primary-button" onclick="document.getElementById('myModal').style.display='block'">
                OPEN - LINK
            </div>
            <div id="myModal" class="modal">
                <div class="modal-content">
                    <span class="close" onclick="document.getElementById('myModal').style.display='none'">&times;</span>
                    <h1>👇🏻 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙷𝙴𝚁𝙴👇🏻</h1>
            <div class="button-container">
                <button onclick="window.location.href='{links1[0]}'">sᴇʀᴠᴇʀ 1</button>
                <button onclick="window.location.href='{links1[1]}'">sᴇʀᴠᴇʀ 2</button>
                <button onclick="window.location.href='{links1[2]}'">sᴇʀᴠᴇʀ 3</button>
            </div>
            <h1>👇🏻 𝙶𝙴𝚃 𝙷𝙴𝚁𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴 👇🏻</h1>
            <div class="button-container">
                <button onclick="window.location.href='{links2[0]}'">sᴇʀᴠᴇʀ 1</button>
                <button onclick="window.location.href='{links2[1]}'">sᴇʀᴠᴇʀ 2</button>
                <button onclick="window.location.href='{links2[2]}'">sᴇʀᴠᴇʀ 3</button>
                    </div>
                </div>
            </div>
            '''

            # Insert primary button HTML into the template
            html = html.replace('{new_button}', primary_button_html)    
    else:
        html = '<h1>This is not a streamable file</h1>'
    
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

