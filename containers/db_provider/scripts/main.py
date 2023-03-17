import signal
import sys

from constants import *
from autosaver import *
from channel_handler import *
from databases import *

def gracefully_stop(signum, frame):
    print("gracefully quitting program...")
    if (redispy is not None):
        redispy.close()
        mongo.close()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, gracefully_stop)

    print("connecting to mongodb...")
    mongo = pymongo.MongoClient("mongodb", 27017)
    init_mongodb(mongo)

    print("connecting to redis...")
    redispy = redis.Redis("redis", 6379, password="")
    pubsub = init_pubsub(redispy)

    print("starting autosaver thread...")
    repeating_thread = init_autosave()
    repeating_thread.start()

    print("listening for messages...")
    pubsub_listener(pubsub, mongo)

    repeating_thread.join()