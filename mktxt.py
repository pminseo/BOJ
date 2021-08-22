import os
import json

width = 1920
height = 1080

for n in range(1, 4):
    files = os.listdir('labels/%d/'%n)
    files.sort()
    for file in files:
        lst = list(file.split("."))
        file_name = lst[0]
        with open("labels/%d/%s.json"%(n, file_name), 'r') as f:
            data = json.load(f)
        for p in data["objects"]:
            arr = p["points"]["exterior"]
            x, y = 0, 0
            tmp_w, tmp_h = list(), list()
            for i in range(len(arr)):
                x += round(arr[i][0] / width, 6)
                y += round(arr[i][1] / height, 6)
                tmp_w.append(arr[i][0] / width)
                tmp_h.append(arr[i][1] / height)
            x = round(x/len(arr), 6)
            y = round(y/len(arr), 6)
            w = round(max(tmp_w) - min(tmp_w), 6)
            h = round(max(tmp_h) - min(tmp_h), 6)
            if os.path.isfile("images/%s.txt"%(file_name)) == False:
                f = open("images/%s.txt"%(file_name), 'w')
                f.write("%f %f %f %f\n"%(x, y, w, h))
                f.close()
            else:
                with open("images/%s.txt"%(file_name), 'a') as f:
                    f.write("%f %f %f %f\n"%(x, y, w, h))


