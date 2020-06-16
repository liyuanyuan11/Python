scoreDict={"John":82,"Christina":96,"Johnson":100,"Marry":73,"Emily":88,"Justin":92}
scoreList=list(scoreDict.items())
print(scoreList.sort(key=lambda items: items[1]))
print(scoreList)