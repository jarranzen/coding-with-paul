# Program starts
# import modules
import random

# Question : Do you want to make a random Track?
#print ('Do you want to make a random Track?')
# Answer Y/N
# on yes run script
#on no 
#print((\n"What genre would you like to create?"\n) + (\ngenre\n))
#Define Tempo
tempo = (f"\nTempo: {random.randint(50,200)} \n")
#Define Key
keysig = ['C Maj', 'G Maj', 'D Maj', 'A Maj', 'E Maj', 'B Maj', 'F# Maj', 'C# Maj', 'F Maj', 'Bb Maj', 'Eb Maj', 'Ab Maj', 'Db Maj', 'Gb Maj', 'Cb Maj',\
'a min', 'e min', 'b min', 'f# min', 'c# min', 'g# min', 'd# min', 'a# min', 'd min', 'g min', 'c min', 'fmin', 'bb min', 'eb min', 'ab min' ]
#define Genre
genre = ['Rock', 'Metal', 'Boom Bap', 'Trap', 'Hip Hop', 'Drum & Bass',  ]
#define instruments
instruments = ['Cello', 'Guitar', 'Bass', 'Dbl Bass', ]
#define arrangement
arrangement = ['I-V-PC-C-MI-1/2V-PC-C-MI-B-C-C-O', 'I-C-V-C-V-C-c-O', ]
# print number of tracks | tracks radomly chosen between 3 and 20 tracks
tracknumber = random.randint(4,20)
## or print non repeating instruments fro random array looping for random number of time in range (3 to 20)
#define number of tracks
# Print Instruments in tracks from list Rules : 1 instrument per track | instruments cannot repeat | instruments chosen at random for instrument array | 
#def poprand(lst):
   # '''return a random element of arr and delete it (so arr is now shorter)'''
    #randb = random.randint(0,len(lst)-1) # random index of lst
    #return lst.pop(randb) # returns item in position randb and removes it from lst
#print(random.choices(instruments, cum_weights=(5, 50, 30, 20), k=4))

print(f"\nCompose this -\n" )
# Print Key Signature
print (random.choice(keysig))
# Print Tempo
print (tempo)
# Print track numbers next to instruments
print (f"Arrangement is - " + (random.choice(arrangement)) )
# Print Genre
print (f"Genre is - " + (random.choice(genre)) )


#print Track numbers and instruments

for i in random.sample(range(4,20), 1):
    print ((random.choice(instruments)))
     #cum_weights=(5, 50, 30, 20), k=4)))

# Print arrangement | Rules : One Arrangement must be chosen from arrangement array at random. 

print ('Go create!')
