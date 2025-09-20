import redis
import json
from src.config import settings

_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is None:
        try:
            _redis_client = redis.from_url(settings.REDIS_STRING_URL, decode_responses=True)
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Redis: {e}")
    return _redis_client

def set_cache(key, value):
    """
    Set a value in Redis cache.
    :param key: Cache key
    :param value: Value to cache (string, dict, list, etc.)
    :param ex: Expiry time in seconds (optional)
    :return: True if successful, False otherwise
    """
    try:
        client = get_redis_client()
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        return client.set(key, value)
    except Exception as e:
        # Optionally log the error
        return False

def get_cache(key):
    """
    Get a value from Redis cache.
    :param key: Cache key
    :return: Cached value (auto-deserialized if JSON), or None
    """
    try:
        client = get_redis_client()
        value = client.get(key)
        if value is None:
            return None
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value
    except Exception as e:
        # Optionally log the error
        return None

def clear_cache(key):
    """
    Clear a value from Redis cache.
    :param key: Cache key
    :return: True if successful, False otherwise
    """
    try:
        client = get_redis_client()
        return client.delete(key)
    except Exception as e:
        # Optionally log the error
        return False