from db_utils import execute_query,execute_batch_query
import json
def temp():
    import time
    start_time = time.time()
    res=execute_query(
        '''
select count(*) from products where (metadata->>'price')::int=1000;
'''
    )
    end_time = time.time()
    print(f"Query executed in {end_time - start_time:.2f} seconds")

    print(res)
if __name__=="__main__":
    temp()