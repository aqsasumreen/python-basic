lis = ['Cwh' , 'Sentdex' ,'clever pro', 'Mosh','Yt','Geo','Ary','Hum']
i=0
for  item  in lis:
    i=i+1
    if i%2== 0:
        print(i ,item)

        # amother way
for i , item in enumerate(lis):
    if (i+1) % 2 == 0:
        print(i, item)