def main():
    #initializing data structure
    student_info = {
        'name' : 'Max',
        'student_id': '10270829', 
        'pizza_toppings':['bacon' , 'pepperoni', 'double cheese'],
        'movies':[
            {'title':['Over the Hedge', 'Lone Survivor']
            },
            {'genre':[
                'comedy',
                'thriller']
            }
        ]
      }
#adding a new movie to the list
    student_info['movies'][0]['title'].append('Baby Driver')
    student_info['movies'][1]['genre'].append('action')
#adding new toppings to the list
    moreToppings = ('pineapple', 'peppers', 'green onions')
    add_toppings(student_info,moreToppings)
    #printing my sentence
    new_sentence(student_info)

def add_toppings(student_info, toppings): #adding new toppings to list
    for i in toppings:
        student_info['pizza_toppings'].append(i)
    print('\n')
    student_info['pizza_toppings'] = sorted(student_info['pizza_toppings'])

def new_sentence(student_info): # making a sentence
    print('Hello there, my name is ', student_info['name'],', and my student ID is ',student_info['student_id'],'.',sep = '') #First Line

    print('My favourite pizza has ',end='') #Second Line
    for i in range(len(student_info['pizza_toppings'])):
        print(student_info['pizza_toppings'][i],end=', ')
    print('\n')

    print('I love to watch ',end='') #Third Line
    for i in range(len(student_info['movies'][1]['genre'])):
        print(student_info['movies'][1]['genre'][i],end=', ')
    print('\n')

    
    print('Some of my absolute favourites are ',end='') #Fourth Line
    for i in range (len(student_info['movies'][0]['title'])):
        print(student_info['movies'][0]['title'][i],end=', ')
    print('\n')

main()


