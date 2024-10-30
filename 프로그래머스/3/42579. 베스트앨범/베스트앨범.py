def solution(genres, plays):
    music_dict = {}
    
    for i in range(len(genres)):
        if genres[i] in music_dict:
            music_dict[genres[i]].append((plays[i], i))
        else:
            music_dict[genres[i]] = [(plays[i], i)]
    
    
    for key in music_dict.keys():
        sorted_data = sorted(music_dict[key], key=lambda x: (-x[0], x[1]))
        music_dict[key] = sorted_data
    
    plays_array = []
    for key in music_dict.keys():
        plays_sum = 0
        for play, num in music_dict[key]:
            plays_sum += play
        plays_array.append(plays_sum)
    
    keys_array = []
    for i in range(len(plays_array)):
        keys_array.append((plays_array[i], list(music_dict.keys())[i]))
    keys_array.sort(reverse=True)
    
    answer = []
    for _, key in keys_array:
        if len(music_dict[key]) < 2:
            answer.append(music_dict[key][0][1])
        else:
            answer.append(music_dict[key][0][1])
            answer.append(music_dict[key][1][1])
            
    return answer