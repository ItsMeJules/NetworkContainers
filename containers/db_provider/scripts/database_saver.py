from databases import *
from uuid import UUID


def save_data(db, redispy):
    mapped_values = {}

    for name, uuid in redispy.hgetall(REDIS_UUID_LOOKUP_HSET).items():
        mapped_values[name.decode('utf-8')] = UUID(uuid.decode("utf-8"))

    found_names = [doc[MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD] for doc in db[MONGODB_UUID_LOOKUP_COLLECTION].find(
        {MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD: {'$in': list(mapped_values.keys())}})]
    found_names_len = len(found_names)

    if found_names_len != 0:
        filter_found = {MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD: {'$in': found_names}}
        documents_to_update = [
            {'$set': {MONGODB_UUID_LOOKUP_COLLECTION_UUID_FIELD: str(mapped_values[name]) for name in found_names}}]
        db[MONGODB_UUID_LOOKUP_COLLECTION].update_many(filter_found, documents_to_update)

    if found_names_len != len(mapped_values.keys()):
        documents_to_insert = [{MONGODB_UUID_LOOKUP_COLLECTION_NAME_FIELD: name,
                                MONGODB_UUID_LOOKUP_COLLECTION_UUID_FIELD: str(mapped_values[name])} for name in
                               set(mapped_values.keys()) - set(found_names)]
        db[MONGODB_UUID_LOOKUP_COLLECTION].insert_many(documents_to_insert)
