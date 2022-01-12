import time
import subprocess

STATE = {}


def setup_package():
    if STATE.get('process'):
        return
    STATE['process'] = subprocess.Popen(['localstack', 'start', '-d'])
    subprocess.Popen(['localstack', 'wait']).wait()


def teardown_package():
    subprocess.Popen(['localstack', 'stop']).wait()
