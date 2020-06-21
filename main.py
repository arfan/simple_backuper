import errno
import json
import os
import shutil
import sys


def read_configuration(file):
    with open(file, "r") as f:
        # Reading from file
        data = json.loads(f.read())

        backup_list = data.get("backup_list")
        contains = data.get("backup_condition").get("contains")
        exactly = data.get("backup_condition").get("exactly")

        return backup_list, contains, exactly


def check_contains(string, contains):
    for c in contains:
        if c in string:
            return True

    return False


def check_exactly(string, exactly):
    for c in exactly:
        if c == string:
            return True

    return False


def copy_backup(root_dir, target_dir, contains, exactly):
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            absolute_path = os.path.join(root, name)
            trimmed = absolute_path[len(root_dir):]

            if check_contains(trimmed, contains) or check_exactly(name, exactly):
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


def main():
    configuration_file = "default.json"
    if len(sys.argv) == 2:
        configuration_file = sys.argv[1]

    backup_list, contains, exactly = read_configuration(configuration_file)

    for backup in backup_list:
        copy_backup(backup.get("root_dir"), backup.get("target_dir"), contains, exactly)


if __name__ == "__main__":
    # execute only if run as a script
    main()
