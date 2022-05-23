from random import randint
from json import load, dump
from os.path import isfile
Configuration_Filename = "KeyGenerator.Configuration.json"
Configuration_Default = {"AskForKeyStart": False, "AskForKeysCount": False, "Vocabulary": "ABCDEF0123456789", "KeyChunksCount": 5, "KeyChunksLength": 5, "KeyChunksSeparatorChar": "-"}
def Configuration_LoadDefaults(Message):
    print(Message)
    Configuration_File = open(Configuration_Filename, "w")
    with open(Configuration_Filename, "w") as Configuration_File:
        dump(Configuration_Default, Configuration_File, ensure_ascii=False, indent=4)
if (not(isfile(Configuration_Filename))):
    Configuration_LoadDefaults("No configuration file was found, so a new one was created.")
    Configuration = Configuration_Default
else:
    Configuration = load(open(Configuration_Filename))
    if (not(("AskForKeyStart" in Configuration) and ("AskForKeysCount" in Configuration) and ("Vocabulary" in Configuration) and ("KeyChunksCount" in Configuration) and ("KeyChunksLength" in Configuration) and ("KeyChunksSeparatorChar" in Configuration))):
        Configuration_LoadDefaults("The found configuration does not have some fields, so it was overwritten with the standard one.")
        Configuration = Configuration_Default
    else:
        if (len(Configuration["KeyChunksSeparatorChar"]) > 1):
            Configuration_LoadDefaults("\"KeyChunksSeparatorChar\" is a single character. The configuration is overwritten with the standard one.")
            Configuration = Configuration_Default
VocabularyLength = len(Configuration["Vocabulary"])
if (Configuration["AskForKeyStart"]):
    KeyStart = input("Key begins with:\n").upper()
else:
    KeyStart = ""
if (Configuration["AskForKeysCount"]):
    KeysCount = int(input("Keys count:\n"))
else:
    KeysCount = 1
print("Result:")
for KeyIndex in range(KeysCount):
    KeyChunks = []
    KeyStartLength = len(KeyStart)
    CharIndex = 0
    for Chunk in range(Configuration["KeyChunksCount"]):
        KeyChunk = ""
        for Char in range(Configuration["KeyChunksLength"]):
            if (CharIndex < KeyStartLength):
                KeyChunk = KeyChunk + KeyStart[CharIndex]
            else:
                KeyChunk = KeyChunk + Configuration["Vocabulary"][randint(0, VocabularyLength - 1)]
            CharIndex+=1
        KeyChunks.append(KeyChunk)
    print('-'.join(KeyChunks))
input()
