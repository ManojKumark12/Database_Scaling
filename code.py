from db_utils import execute_query,bulk_insert
def temp():
    import time
    start_time = time.time()
    res=execute_query(
        '''
select count(*) from products where (metadata->>'price')::int=1000;
'''
    )
    print(res)
    end_time = time.time()
    print(f"Query executed in {end_time - start_time:.2f} seconds")

    # print(bulk_insert())
if __name__=="__main__":
    temp()