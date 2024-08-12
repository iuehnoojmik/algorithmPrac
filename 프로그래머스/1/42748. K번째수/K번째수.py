def solution(array, commands):
    answer = []
    
    for num_list in commands:
        temp_list = sorted(array[num_list[0]-1:num_list[1]])
        answer.append(temp_list[num_list[2]-1])
    
    return answer