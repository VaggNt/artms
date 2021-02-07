import csv

class Adjacency(object):
    def __init__(self,object_id,priority,distance,tier,attempts,hosr):
        self.object_id=object_id
        self.priority=priority
        self.distance=distance
        self.tier=tier
        self.attempts=attempts
        self.hosr=hosr


       
def parse_csv(filename):
    adj_list = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        for i in reader:
            adj_list.append(Adjacency(i['object_id'], i['priority'], i['distance'], i['tier'], i['attempts'], i['hosr']))
    return adj_list

adjacency_list = parse_csv('adjacencies.csv')

def sort_adjacency(adj_list):
    #First level sort on priority attribute
#     adj_list.sort(key=lambda x: x.priority)

    for i in adj_list:
        if i.priority == 1:
            adj_list.sort(key=lambda x: x.distance).reversed()
        elif i.priority == 2:
            adj_list.sort(key=lambda x: x.tier).reversed()
        elif i.priority == 3:
            adj_list.sort(key=lambda x: x.attempts).reversed()
        elif i.priority == 4:
            adj_list.sort(key=lambda x: x.hosr ).reversed()
    return adj_list



def create_csv():
    result_list = sort_adjacency(adjacency_list)

    with open('result.csv', 'w+') as res:
        writer = csv.writer(res)
        writer.writerow(['object_id', 'priority', 'distance', 'tier', 'attempts', 'hosr'])

        for i in result_list:
            writer.writerow([i.object_id, i.priority, i.distance, i.tier, i.attempts, i.hosr])

if __name__ == '__main__':
    create_csv()
