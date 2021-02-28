import telethon.sync

import Config as Cfg
import MyntUpdater as Mu
import PeerMgr as Pm

if Cfg.enable_proxy:
    connection = telethon.connection.ConnectionTcpMTProxyRandomizedIntermediate
    proxy = Cfg.proxy
else:
    connection = telethon.connection.ConnectionTcpFull
    proxy = None

client = telethon.TelegramClient(
    session=Cfg.session_name, api_id=Cfg.api_id, api_hash=Cfg.api_hash,
    connection=connection,
    proxy=proxy)
client.start()


@client.on(telethon.events.NewMessage(chats=Cfg.in_id))
async def new_message_listener(event):
    if event.message.message.find(Cfg.msg_filter_str) > -1:
        print(event.message.message)
        Pm.extract_add_proxy(event.message.message)
        Mu.update_mynt()
