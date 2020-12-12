import json
from models.news import News


def import_Data_From_Json_File():

    newsList = []
    with open('models/NumbersJSON.txt') as json_file:
        data = json.load(json_file)
        for p in data:
            newsList.append(News(p['Name'], p['Number']))

    return newsList
    # for i in newsList:
    #     print(i.name + i.number)


# if __name__ == '__main__':
#     import_Data_From_Json_File()
