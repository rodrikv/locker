import subprocess


def suspend(*args, **kwargs):
    return subprocess.Popen(
        "systemctl suspend",
        shell=True,
    )

def lock(*args, **kwargs):
    return subprocess.Popen(
        "loginctl lock-session",
        shell=True,
    )

def unlock(*args, **kwargs):
    return subprocess.Popen(
        f"loginctl unlock-session",
        shell=True,
    )

def get_session(*args, **kwargs):
    return subprocess.Popen(
        "cat /proc/self/sessionid",
        shell=True,
    )