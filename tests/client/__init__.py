import time
import subprocess32 as subprocess

STATE = {}


def setup_package():
    if STATE.get('process'):
        return
    STATE['process'] = subprocess.Popen(['localstack', 'start'])
    time.sleep(10)


def teardown_package():
    # TODO implement "stop" command in LocalStack!
    # subprocess.check_call('localstack stop', shell=True)
    STATE['process'].terminate()
    time.sleep(2)
