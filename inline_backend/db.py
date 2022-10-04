import config
import redis

redis_db = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
