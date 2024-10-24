import redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def get(self, key):
        # Retrieve the value from Redis and deserialize the JSON string back into a dictionary
        cached_data = self.client.get(key)
        if cached_data:
            return json.loads(cached_data)  # Convert the JSON string back to a dictionary
        return None

    def set(self, key, value, ex=None):
        # Serialize the dictionary into a JSON string before storing it in Redis
        self.client.set(key, json.dumps(value), ex=ex)  # Convert dict to JSON string

    def delete(self, key):
        """Delete data from Redis cache."""
        self.client.delete(key)
