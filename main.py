# python3

import string


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}

    for cur_query in queries:
        if (cur_query.type == 'add'):
            contacts[cur_query.number] = cur_query.name
        elif (cur_query.type == 'del'):
            if (cur_query.number in contacts):
                del contacts[cur_query.number]
        elif (cur_query.type == 'find'):
            if (cur_query.number in contacts):
                text = str(contacts[cur_query.number])
                #result.append(contacts[cur_query.number])
                #result.append(text)
            else:
                text += ' not found'
                #result.append(str(contacts.get(cur_query.number)) + ' not found')
            
            result.append(text)
    for i in range(len(result)):
        if(i < len(result) - 1 and result[i] + ' not found' == result[i+1]):
            result.pop(i)
            
    #print(contacts)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

