import errno
import os
import shutil

backup_list = [
    {"root_dir": "/home/srlabs/srlabs/autobahn_manager", "target_dir": "backup_arfancode_autobahn_manager"},
]

contains = ["arfancode"]
exactly = [".env"]


def check_contains(str):
    for c in contains:
        if c in str:
            return True

    return False


def check_exactly(str):
    for c in exactly:
        if c == str:
            return True

    return False


def copy_backup(root_dir, target_dir):
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            absolute_path = os.path.join(root, name)
            trimmed = absolute_path[len(root_dir):]

            if check_contains(trimmed) or check_exactly(name):
                print(absolute_path)

                try:
                    shutil.copy(absolute_path, target_dir + trimmed)
                except IOError as e:
                    # ENOENT(2): file does not exist, raised also on missing dest parent dir
                    if e.errno != errno.ENOENT:
                        raise
                    # try creating parent directories
                    os.makedirs(os.path.dirname(target_dir + trimmed))
                    shutil.copy(absolute_path, target_dir + trimmed)


for backup in backup_list:
    copy_backup(backup.get("root_dir"), backup.get("target_dir"))
