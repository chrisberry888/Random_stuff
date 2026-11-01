#this whole program describes every septatonic scale containing only major and minor thirds.

import itertools

def is_valid(arr):
    if sum(arr) != 12:
        return False
    if arr[0] + arr[-1] != 3 and arr[0] + arr[-1] != 4:
        return False
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] != 3 and arr[i] + arr[i+1] != 4:
            return False
    return True
   
def scale_finder():
    scales = []
    scale = [1 for i in range(7)]
    end = [3 for i in range(7)]

    while scale != end:
        scale[0] += 1
        for i in range(len(scale)-1):
            if scale[i] == 4:
                scale[i] = 1
                scale[i+1] += 1
            
        if is_valid(scale):
            temp = [0 for i in range(7)]
            for i in range(6):
                temp[i+1] = temp[i]+scale[i]
            scales.append(temp)
        
    for scale in scales:
        print(f'{scale}')
        
    return scales
        
    
    
def scale_explorer_1(scales):

    #(degree, place, major/minor)
    switcher = {
        (1,0,"m"): "i",
        (1,0,"M"): "I",
        (2,1,"m"): "bii",
        (2,1,"M"): "bII",
        (2,2,"m"): "ii",
        (2,2,"M"): "II",
        (2,3,"m"): "#ii",
        (2,3,"M"): "#II",
        (3,3,"m"): "biii",
        (3,3,"M"): "bIII",
        (3,4,"m"): "iii",
        (3,4,"M"): "III",
        (4,4,"m"): "biv",
        (4,4,"M"): "bIV",
        (4,5,"m"): "iv",
        (4,5,"M"): "IV",
        (4,6,"m"): "#iv",
        (4,6,"M"): "#IV",
        (5,6,"m"): "bv",
        (5,6,"M"): "bV",
        (5,7,"m"): "v",
        (5,7,"M"): "V",
        (5,8,"m"): "#v",
        (5,8,"M"): "#V",
        (6,8,"m"): "bvi",
        (6,8,"M"): "bVI",
        (6,9,"m"): "vi",
        (6,9,"M"): "VI",
        (7,9,"m"): "bbvii",
        (7,9,"M"): "bbVII",
        (7,10,"m"): "bvii",
        (7,10,"M"): "bVII",
        (7,11,"m"): "vii",
        (7,11,"M"): "VII"
    }
    
    chords = []
    for scale in scales:
        temp = []
        for i1 in range(7):
            chord = ""
            i2 = (i1+2)%7
            i3 = (i1+4)%7
                
            if (scale[i2]-scale[i1])%12 == 4:
                
                chord = switcher.get((i1+1,scale[i1],"M"))
                if (scale[i3]-scale[i2])%12 == 4:
                    chord += "+"
            else:
                
                chord = switcher.get((i1+1,scale[i1],"m"))
                if (scale[i3]-scale[i2])%12 == 3:
                    chord += "o"
            
            temp.append(chord)
        chords.append(temp)
    return chords
                
        
scales = scale_finder()        
chords = scale_explorer_1(scales)

# adding 10/31/26


chord_frequency = {}
scale_degrees = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
accidentals = ['bb', 'b', '', '#']

for scale_degree, accidental in itertools.product(scale_degrees, accidentals):
    
    if scale_degree == 'i' and accidental != '':
        continue
    if scale_degree == 'ii' and accidental == 'bb':
        continue
    if scale_degree == 'vii' and accidental == '#':
        continue
    major = accidental + scale_degree.upper()
    augmented = major + '+'
    minor = accidental + scale_degree
    diminished = minor + 'o'
    chord_frequency[major] = 0
    chord_frequency[augmented] = 0
    chord_frequency[minor] = 0
    chord_frequency[diminished] = 0


for scale in chords:
    print(scale)
    for chord in scale:
        chord_frequency[chord] = chord_frequency.get(chord, 0) + 1


            
for chord in chord_frequency:
    print(f'{chord} : {chord_frequency.get(chord)}')

print()
print()
sorted_dict = {}
for key in sorted(chord_frequency, key=chord_frequency.get, reverse=True):
    sorted_dict[key] = chord_frequency[key]

for chord in sorted_dict:
    print(f'{chord} : {chord_frequency.get(chord)}')