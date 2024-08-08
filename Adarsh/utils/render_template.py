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

            # Define button HTML separately
            download_buttons_html = ''.join(
                f'<button onclick="window.location.href=\'{links1[i]}\'">sᴇʀᴠᴇʀ {i + 1}</button>\n'
                for i in range(len(links1))
            )

            telegram_buttons_html = ''.join(
                f'<button onclick="window.location.href=\'{links2[i]}\'">sᴇʀᴠᴇʀ {i + 1}</button>\n'
                for i in range(len(links2))
            )

            # Define the HTML for direct display
            buttons_html = f'''
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
                    margin: 4px;
                    width: 200px;
                }}
                .button-container button:hover {{
                    background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    transform: translateY(-5px);
                }}
            </style>
            <div class="button-container">
                <h1>👇🏻 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙷𝙴𝚁𝙴👇🏻</h1>
                {download_buttons_html}
                <h1>👇🏻 𝙶𝙴𝚃 𝙷𝙴𝚁𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙄𝙇𝙴 👇🏻</h1>
                {telegram_buttons_html}
            </div>
            '''

            # Insert buttons HTML into the template
            html = html.replace('{download_buttons}', download_buttons_html)
            html = html.replace('{telegram_buttons}', telegram_buttons_html)
    else:
        html = '<h1>This is not a streamable file</h1>'
    
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

            # Define button HTML separately
            download_buttons_html = ''.join(
                f'<button onclick="window.location.href=\'{links1[i]}\'">sᴇʀᴠᴇʀ {i + 1}</button>\n'
                for i in range(len(links1))
            )

            telegram_buttons_html = ''.join(
                f'<button onclick="window.location.href=\'{links2[i]}\'">sᴇʀᴠᴇʀ {i + 1}</button>\n'
                for i in range(len(links2))
            )

            # Define the HTML for direct display
            buttons_html = f'''
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
                    margin: 4px;
                    width: 200px;
                }}
                .button-container button:hover {{
                    background: linear-gradient(to right, #ff758c, #ff7eb3); /* gradient from pink to violet */
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    transform: translateY(-5px);
                }}
            </style>
            <div class="button-container">
                <h1>👇🏻 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙷𝙴𝚁𝙴👇🏻</h1>
                {download_buttons_html}
                <h1>👇🏻 𝙶𝙴𝚃 𝙷𝙴𝚁𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙄𝙇𝙴 👇🏻</h1>
                {telegram_buttons_html}
            </div>
            '''

            # Insert buttons HTML into the template
            html = html.replace('{download_buttons}', download_buttons_html)
            html = html.replace('{telegram_buttons}', telegram_buttons_html)
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

