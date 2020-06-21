# Simple Backup-er

Sometime if I code, I put my own utilities like shell script or my own settings.
Those files is not supposed to be put into organizations git repository, but I
also need that file to be backup somewhere. I add something in the prefix of the 
file so that it will be ignored by git (put that settings in git global ignore)
for example arfancode_my_tools.sh 

With this script I can copy those file and put it in a folder.

## How to use

Create file default.json as your settings, use sample-default.json as your reference
to create that file.

Sample-default.json
```json
{
  "backup_list": [
    {
      "root_dir": "/home/user/folder",
      "target_dir": "backup_location"
    }
  ],

  "backup_condition": {
    "contains": ["yourpattern"],
    "exactly": ["exact_file.txt"]
  }
}
```

Run the script
```
$ python main.py [default.json]
```


