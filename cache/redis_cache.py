import redis
import json

class RedisCache:
    """
    A simple wrapper for Redis caching with basic get, set, and delete operations.
    """
    def __init__(self, host='localhost', port=6379, db=0):
        """
        Initialize Redis connection.
        """
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def get(self, key):
        """
        Get data from Redis cache by key.
        """
        cached_data = self.client.get(key)
        if cached_data:
            return json.loads(cached_data)
        return None

    def set(self, key, value, ex=None):
        """
        Set data in Redis cache with an expiration time.
        """
        self.client.set(key, json.dumps(value), ex=ex)

    def delete(self, key):
        """
        Delete data from Redis cache by key.
        """
        self.client.delete(key)
