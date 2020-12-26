import matplotlib.pyplot as plt

uni_file = open('unicode.txt', 'r')
uni_txt = uni_file.read()
uni_file.close()

uni_chars = uni_txt.split()
periodicity_found = []
periodicity = {}
processed_periodic_dict = {}

def to_cal_periodicity(char, index):
    count = 0
    temp = uni_chars[index+1:]
    for j in temp:
        if j == char:
            periodicity[char].append(count)
            count = 0
        else:
            count = count + 1

def to_process_dict(periodicity_dict):
    dict_keys = periodicity_dict.keys()
    
    for key in dict_keys:
        if len(periodicity_dict[key]) == 0:
            average = 0
        else:
            average = sum(periodicity_dict[key])/len(periodicity_dict[key])
        key = key.replace('U+', '')
        key = key[:1] + 'x' + key[1:]
        processed_periodic_dict[chr(int(key, 16))] = average 

def plot_bar(periodicity_dict):
    keys = list(periodicity_dict.keys())
    values = list(periodicity_dict.values())
    keys = [ hex(ord(i)).replace('x', '') for i in keys ]

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(keys, values)
    plt.show()


for i, char in enumerate(uni_chars):
    if char in periodicity_found:
        pass
    else:
        periodicity_found.append(char)
        periodicity[char] = []
        to_cal_periodicity(char, i)

to_process_dict(periodicity)
plot_bar(processed_periodic_dict)