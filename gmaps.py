import json, requests, os, time

lines = []
with open("pubs.csv", "r") as f:
    for l in f.readlines():
        lines.append(l.split(",")[0])
pubs = [l.replace("'", "").replace("\"", "").replace(" ", "+") + "+Oxford+UK" for l in lines]

pubDicts = {}
for pub in pubs:
    pubDicts[pub] = {}

addresses = set()

most = 5

for row in range(0, len(pubs), most):
    for col in range(0, len(pubs), most):
        origins = pubs[row:row+most]
        dests = pubs[col:col+most]
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
        url += "key=" + os.environ['GMAPS_KEY'] + "&"
        url += "mode=walking&"
        url += "origins=" + "|".join(origins) + "&"
        url += "destinations=" + "|".join(dests)

        r = requests.get(url)
        j = r.json()

        with open("{},{}.json".format(row, col), "w") as f:
            f.write(json.dumps(j, sort_keys=True, indent=4))

        rows = j["rows"]
        for r in range(0, len(rows)):
            for c in range(0, len(rows[r]["elements"])):
                if "distance" in rows[r]["elements"][c]:
                    pubDicts[origins[r]][dests[c]] = rows[r]["elements"][c]["distance"]["value"]
                else:
                    print("Error on {},{}".format(pubs[row + r], pubs[col + c]))
        time.sleep(1) # API rate limiting

data = json.dumps(pubDicts, sort_keys=True, indent=4)
with open("distances.json", "w") as f:
    f.write(data)
