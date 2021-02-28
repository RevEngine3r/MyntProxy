import time

import pythonping

peers = []
max_peers = 30


# port = 1023
# secret = 'dd8b2394ad2ecef7e607d5f52b31a45768'


def extract_add_proxy(message_text):
    message_text = message_text.split('=')
    ip = message_text[1].split('&')[0]
    peers.append(ip)


def ping_sort():
    global peers
    __peer_ping = []
    for i in range(len(peers)):
        __peer_ping.append([peers[i], pythonping.ping(peers[i]).rtt_avg_ms])
        time.sleep(.2)

    peers = [peer[0] for peer in sorted(__peer_ping, key=lambda x: x[1])]
    peers = peers[:max_peers]
    print(f'{peers=}')


def get_best_5():
    b5 = list(set(peers))[:5]
    print(f'{b5=}')
    return b5
