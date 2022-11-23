import subprocess


def suspend(*args, **kwargs):
    return subprocess.Popen(
        "systemctl suspend",
        shell=True,
    )