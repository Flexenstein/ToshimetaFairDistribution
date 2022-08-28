import os
import json
from collections import deque

srcimageFolder = r"C:\Shift\pre-shift\images\\"
srcjsonFolder = r"C:\Shift\pre-shift\json\\"

destimageFolder = r"C:\Shift\shifted\images\\"
destjsonFolder = r"C:\Shift\shifted\json\\"

offset = 0 #0 will become value obtained from chainlink VRF (lower 10 digits) (Contract address: 0x76452F4e679Ce96e7dbDAa8191Bf887D43445584)
numberListLen = 21
numberList = []

for i in range(numberListLen):
    numberList.append(i)

newList = deque(numberList)
newList.rotate(offset)

shiftedList = list(newList)

listLen = len(shiftedList)


for i in range(listLen):
    listIndex = i
    listValue = shiftedList[i]

    imgsrc = srcimageFolder + str(listValue) + '.gif'
    imgdest = destimageFolder + str(listIndex) + '.gif'
    os.rename(imgsrc, imgdest)

    filesrc = srcjsonFolder + str(listValue) + '.json'
    json_file = open(filesrc, "r")
    json_obj = json.load(json_file)
    json_file.close()

    json_obj["name"] = "Toshimeta #" + str(listIndex)
    json_obj["image"] = "ipfs://NewUriToReplace/"+str(listIndex)+".png"
    json_obj["edition"] = listIndex

    json_file = open(filesrc, "w")
    json.dump(json_obj, json_file, indent=4)
    json_file.close()

    filedest = destjsonFolder + str(listIndex) + '.json'
    os.rename(filesrc, filedest)
    print(listIndex)
