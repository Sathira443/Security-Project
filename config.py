from configparser import ConfigParser
import hashlib

# Get the configparser object
config_object = ConfigParser()

def writeConfig():
    password = "yasiru"
    hs_pass = hashlib.md5(password.encode('utf-8'))
    encoded = hs_pass.digest()

    config_object["USERINFO"] = {
        "user_name": "Yasiru",
        "hashed_password": str(encoded),
    }

    # Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

def readConfig():
    config_object.read("config.ini")

    #Get the password and username stored in the config file
    userinfo = config_object["USERINFO"]
    return {
        "user_name": str.format(userinfo["user_name"]),
        "hashed_password": str.format(userinfo["hashed_password"]),
    }

# writeConfig()
# result = readConfig()
# print(result)
