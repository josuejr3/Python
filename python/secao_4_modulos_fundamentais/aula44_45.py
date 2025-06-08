import subprocess
import sys

print(sys.platform)

cmd = ['ping', '127.0.0.1']
encod = 'utf-8'
system = sys.platform

if system == 'win32':
    cmd = ["dir"]
    encod = "cp850"

proc_ping = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encod,
    shell=True,
)

# Printa os argumentos do comando
#print(proc_ping.args)
# Printa o erro, se ocorreu algum
#print(proc_ping.stderr)
# Printa a saída se ocorreu alguma
#print(proc_ping.stdout.decode('cp852'))

# Se usarmos um text=True
print(proc_ping.stdout)

# Printa o código de retorno, 0 se deu certo
#print(proc_ping.returncode)