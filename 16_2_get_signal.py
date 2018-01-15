import os
import sys
import signal
import time
import math
import random

child_processes = 3
dead_processes = 0

# 子プロセスを3 つ生成する
for i in range(child_processes):
    pid = os.fork()
    if pid == 0:
        # それぞれ3 秒間sleep させる
        time.sleep(3)
        os._exit(0)
    else:
        print("Spawned child with pid", pid)

# この後、親プロセスは重い計算処理で忙しくなるが、
# 子プロセスの終了は検知したい。
def wait_children(signum, frame):
    global dead_processes
    print("A child has died")
# 終了した子プロセスの情報をwaitpidで取得すれば、
# 生成した子プロセスのどれが終了したのかがわかる。
# ブロックせずにwaitpid をループさせることで、
# 子プロセスの終了を見逃さないようにする。
    try:
        while True:
            pid, exit_status = os.waitpid(-1, os.WNOHANG)
            if pid:
                dead_processes += 1
            else:
                break
            if dead_processes == child_processes:
                print("All children are dead")
                sys.exit()
    except OSError:
        pass

signal.signal(signal.SIGCHLD, wait_children)

while True:
    math.floor(math.sqrt(random.randint(1, 44) ** 8))
    time.sleep(1)
