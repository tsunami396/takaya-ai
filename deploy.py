import subprocess
res = subprocess.call('ls')
#=> lsコマンドの結果
print res
#=> コマンドが成功していれば 0