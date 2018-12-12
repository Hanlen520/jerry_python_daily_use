from multiprocessing.dummy import Pool as ThreadPool
import random,time
# 设置并发数量
threadNum = 3

# 修改为从数据库中读取用例列表
def get_caes_list():
    return [i for i in range(1,20)]

# 具体的执行方法
def run_case(case_id):
    run_time = random.randrange(1,10)
    time.sleep(run_time)
    print('run case: %d, result is pass, run time is : %d seconds' %(case_id, run_time))

# 设置多线程执行
pool = ThreadPool(threadNum)
pool.map(run_case, get_caes_list())
pool.close()
pool.join()