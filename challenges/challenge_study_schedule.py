def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    
    repeat_times = 0

    for student_permanence in permanence_period:
        if not type(student_permanence[0]) is int or not type(student_permanence[1]) is int:
            return None
        
        if student_permanence[0] <= target_time <= student_permanence[1]:
            repeat_times += 1

    return repeat_times
