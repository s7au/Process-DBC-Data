import csv

def parseLaneOnlyData(laneDataWords, raceTime):
    print(laneDataWords)
    if len(laneDataWords) <= 2:
        raise Exception("Should not be passed incomplete row")
    teamNameList = []
    teamNameStart = 0
    hasPreRaceSeed = 0
    for j in range(1,len(laneDataWords)-2):
        indexAfter = j
        if laneDataWords[j][0] == "(":
            hasPreRaceSeed = 1
            break
        if teamNameStart == 0:
            if laneDataWords[j][0].isnumeric():
                continue
            else:
                teamNameStart = 1
        if teamNameStart == 1:
            teamNameList.append(laneDataWords[j])

    return [raceTime,laneDataWords[0],' '.join(teamNameList),laneDataWords[indexAfter] if hasPreRaceSeed == 1 else '',laneDataWords[len(laneDataWords)-2],laneDataWords[len(laneDataWords)-1]]


with open('2018Base.txt', 'r') as in_file:
    #stripped = (line.strip() for line in in_file)
    inFileLines = [line.strip().split(" ") for line in in_file if line]
    with open('output.csv', 'w') as out_file:
        writer = csv.writer(out_file)

        raceTime = ''
        i = 0
        while i < len(inFileLines):
            #print(i)
            if inFileLines[i][0] == "RACE":
                #close previous race
                i += 1
                # sometimes there is random text before first race
                while not inFileLines[i][0][0].isnumeric():
                    i += 1
                # lane one wait for now as need raceTime
                laneOneRow = inFileLines[i]
                # lane two
                i += 1
                raceTime = ' '.join([inFileLines[i][0],inFileLines[i][1]])
                # lane one
                if len(laneOneRow) > 3:
                    writer.writerow(parseLaneOnlyData(laneOneRow[1:], raceTime))
                if len(inFileLines[i]) > 4:
                    writer.writerow(parseLaneOnlyData(inFileLines[i][2:], raceTime))
            elif len(inFileLines[i]) > 2 and inFileLines[i][0].isnumeric() and int(inFileLines[i][0]) < 2000:
                writer.writerow(parseLaneOnlyData(inFileLines[i],raceTime))
            i += 1





