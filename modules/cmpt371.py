
def cmpt371(word):
    words = {
        'forwarding':"move packets from router's input to appropriate router output" ,
        'routing':"determine route taken by packets' from source of destination\nEx. Routing algorithm",
        'data plane':"* local, per-router function\n* determines how datagram arriving on router input port is forwarded to router output port\n*forwarding function",
        'control plane':"* network-wide logic\n* determines how datagram is routed among routers along end-end path from source host to destination host",
        'traditional routing algorithm':"implemented in routers",
        'sdn':"(Software-defined networking) implemented in (remote/centralized) servers",
    }
    if word in words:
        return "{}:\n{}".format(word,words[word])
    else:
        return "I'm not sure what you want to define. Please try again"
