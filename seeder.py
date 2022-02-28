import random
import hashlib

class MnemonicHasher:

    def generate():
        wordlist = open("wordlist.txt", "r")
        words = wordlist.readlines()
        seed_list = []
        cons = 0
        while cons <= 11:
            randomnum = random.randint(0, 2465)
            seed = words[randomnum].strip("\n")
            seed_list.append(seed)
            cons = cons + 1
        seeds = ''.join(seed_list)
        wordlist.close()
        key = hashlib.sha256(seeds.encode('utf-8')).hexdigest()
        print ("-"*200)
        print ("That's the seeds generated: ", seed_list)
        print ("-"*200)
        print ("That's your private key: ", key)
        print ("-"*200)
        print ("It is advisable to keep safe, preferably in a offline device or written out in a paper.")
        print ("Keep in mind that the sequence of this seed matters to retrieve the key.")
        print ("-"*200)
    
    def recover():
        seed_list = []
        cons = 0
        seed_pos = cons + 1
        while cons <= 11:
            seed = input(f'Seed in the position {seed_pos}: ')
            seed_list.append(seed)
            print (seed_list)
            seed_pos = seed_pos + 1
            cons = cons + 1

        seeds = ''.join(seed_list)
        key = hashlib.sha256(seeds.encode('utf-8')).hexdigest()
        print ("-"*200)
        print ("That's your private key: ", key)

