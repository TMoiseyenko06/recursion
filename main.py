tasks = [{
    'id':1,
    'name':'clean room',
    'subtasks':[{
    'id':2,
    'name':'clean room',
    'subtasks':[{
    'id':4,
    'name':'clean room',
    'subtasks':[],
    'priority':3
},{
    'id':5,
    'name':'clean room',
    'subtasks':[],
    'priority':3
}],
    'priority':5
}],
    'priority':2
},{
    'id':3,
    'name':'clean room',
    'subtasks':[],
    'priority':3
}]

def schedule_tasks(tasks):
    scheduled = []
    def traverse(tasks):
        for task in tasks:
            scheduled.append({
                'id':task['id'],
                'name':task['name'],
                'priority':task['priority']
            })
            if 'subtasks' in task and task['subtasks']:
                traverse(task['subtasks'])

    traverse(tasks)
    scheduled.sort(key=lambda x: x.get('priority',0),reverse=True)
    print(scheduled)

    
    
# The time and space complexity are both O(n) becasue the amount of tasks increase linearly and do nott effect each other in any way (the sort function has a seperate time complexity that i am not counting in this equation)
schedule_tasks(tasks)
