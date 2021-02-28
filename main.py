import MyntUpdater as Mu
import PeerMgr as Pm
import Tg

for message in Tg.client.iter_messages(Tg.Cfg.in_id, search=Tg.Cfg.msg_filter_str, limit=Pm.max_peers):
    print(message.message)
    Pm.extract_add_proxy(message.message)

Mu.update_mynt()
Tg.client.run_until_disconnected()
