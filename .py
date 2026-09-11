def tre():
    with open("C:/Users/HONOR/Downloads/26_19256.txt", "r") as f:
        n = int(f.readline())
        solutions = []
        for _ in range(n):
            student_id, task_id = map(int, f.readline().split())
            solutions.append((student_id, task_id))
    student_tasks = {}
    for student_id, task_id in solutions:
        if student_id not in student_tasks:
            student_tasks[student_id] = set()  
        student_tasks[student_id].add(task_id)

    best_student_id = -1
    max_consecutive_tasks = 0
    for student_id, tasks in student_tasks.items():
        tasks = sorted(list(tasks))  
        current_consecutive_tasks = 0
        max_current_consecutive_tasks = 0
        
        if not tasks:
            continue
        
        current_consecutive_tasks = 1
        max_current_consecutive_tasks = 1

        for i in range(1, len(tasks)):
            if tasks[i] == tasks[i-1] + 1:
                current_consecutive_tasks += 1
            else:
                max_current_consecutive_tasks = max(max_current_consecutive_tasks, current_consecutive_tasks)
                current_consecutive_tasks = 1
        
                max_current_consecutive_tasks = max(max_current_consecutive_tasks, current_consecutive_tasks)

                if max_current_consecutive_tasks > max_consecutive_tasks:
                    max_consecutive_tasks = max_current_consecutive_tasks
                    best_student_id = student_id
                elif max_current_consecutive_tasks == max_consecutive_tasks and student_id < best_student_id:
                    best_student_id = student_id

    print(best_student_id, max_consecutive_tasks)
tre()
