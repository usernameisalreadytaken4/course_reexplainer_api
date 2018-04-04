import redis


class RedisDict:

    def __init__(self, **redis_kwargs):
        self.__db = redis.Redis(**redis_kwargs)
        self.__keys = set()

    def __len__(self):
        return self.__keys.__len__()

    def __setitem__(self, key, value):
        self.__keys.add(key)
        self.__db.set(key, value)

    def __getitem__(self, key):
        return self.__db.get(key).decode()

    def __contains__(self, item):
        return item in self.__keys

    def expire(self, key, time):
        self.__db.expire(key, time)

    def pop(self, key):
        self.__keys.remove(key)
        return self.__db.delete(key)