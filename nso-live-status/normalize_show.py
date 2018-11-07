#!/usr/bin/python

import json

def main():

    with open("show_version_<device-name>.log", "r") as myfile:
        data = myfile.read()
        json_data = json.loads(data)
    with open("show_version_<device-name>.log", "w") as myfile:
        print(json_data["output"]["result"])
        myfile.write(json_data["output"]["result"])

    return

if __name__ == "__main__":
    main()

