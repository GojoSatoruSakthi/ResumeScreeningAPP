#

import redis
import pickle
r = redis.Redis(
  host='redis-17990.c11.us-east-1-2.ec2.cloud.redislabs.com',
  port=17990,
  password='u0cxsqUjfX2ROjJ8yFnDnbMFcAf5vdX4')


data ={
            "a":1,
            "c":2
        }
data_bytes =pickle.dumps(data)
r.set("key",data_bytes)
ans =r.get("key")
ans2= pickle.loads(ans)
print(ans)
#print(r.hgetall("key"))