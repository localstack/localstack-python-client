import time
import subprocess32 as subprocess


def stop_docker():
    subprocess.check_call('docker stop localstack', shell=True)


def setup_package():
    subprocess.Popen('make docker-run-background', shell=True)
    time.sleep(10)


def teardown_package():
    print("Shutdown")
    stop_docker()


if __name__ == '__main__':
    setup_package()
    teardown_package()
