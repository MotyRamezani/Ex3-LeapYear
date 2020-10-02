import random

words = ['Pizza','Bread','Hamburger','Kebab','Fish','Egg','Chicken','Salad','Rice','Shrimp','Soup','Banana','Lemon','Pineapple',
     'Apple','Grape','Orange','Cherry','Watermelon','Apricot','Pomegranate','Kiwi','Mango','Camel','Horse','Cow','Goat','Donkey',
     'Deer','Cat','Gorilla','Tiger','Fox','Lion','Dog','Elephant','Wolf','Cheetah','Giraffe','Zebra','Piano','Guitar','Trumpet',
     'Drums','Violin','Saxophone','Flute','Harp','Accordion','Pop','Hip hop','Jazz','Rap','Techno','Folk','Country','Folk',
     'Metal','Rock','River','Mountain','Forrest','Stone','Cave','Leaf','Beach','Sea','Dam','Grass','Hill','Island','Lighthouse',
     'Mine','Ocean','Spring','Volcano','Waterfall','Wave','Georgia','Bolivia','Armenia','Morocco','Ukraine','Philippines','Iraq',
     'Ukraine','Chile','Switzerland','Norway','Kazakhstan','Spain','Italy','England','Sudan','Japan','Germany','Oman','Lebanon',
     'Sofa','Carpet','Armchair','Bed','Floor Lamp','Table','Air Conditioner','Bookshelf','Clock','Bedside Table','Dressing Table',
     'Television','Telephone','Curtain','Hat Stand','Desk','Dresser','Fireplace','Coffee Table','Stereo System','Vase','Cushion',
     'Turquoise','Ivory','Denim','Navy','Lime','Mustard','Coral','Aqua','Magenta','Orchid','Crimson','Olive','Wheat']

not_used = words

def Hangman():

    while len(not_used) > 0:
        Foods = ['Pizza','Bread','Hamburger','Kebab','Fish','Egg','Chicken','Salad','Rice','Shrimp','Soup']
        Fruits = ['Banana','Lemon','Pineapple','Apple','Grape','Orange','Cherry','Watermelon','Apricot','Pomegranate','Kiwi','Mango']
        Animals = ['Camel','Horse','Cow','Goat','Donkey','Deer','Cat','Gorilla','Tiger','Fox','Lion','Dog','Elephant','Wolf',
                   'Cheetah','Giraffe','Zebra']
        Music = ['Piano','Guitar','Trumpet','Drums','Violin','Saxophone','Flute','Harp','Accordion','Pop','Hip hop','Jazz','Rap',
                 'Techno','Folk','Country','Folk','Metal','Rock']
        Nature = ['River','Mountain','Forrest','Stone','Cave','Leaf','Beach','Sea','Dam','Grass','Hill','Island','Lighthouse',
                  'Mine','Ocean','Spring','Volcano','Waterfall','Wave']
        Countries = ['Georgia','Bolivia','Armenia','Morocco','Ukraine','Philippines','Iraq','Ukraine','Chile','Switzerland',
                     'Norway','Kazakhstan','Spain','Italy','England','Sudan','Japan','Germany','Oman','Lebanon']
        Furniture = ['Sofa','Carpet','Armchair','Bed','Floor Lamp','Table','Air Conditioner','Bookshelf','Clock','Bedside Table',
                     'Dressing Table','Television','Telephone','Curtain','Hat Stand','Desk','Dresser','Fireplace','Coffee Table',
                     'Stereo System','Vase','Cushion']
        Colors = ['Turquoise','Ivory','Denim','Navy','Lime','Mustard','Coral','Aqua','Magenta','Orchid','Crimson','Olive','Wheat']
        
        print('\n')
        
        rand_word = random.choice(not_used)
        not_used.remove(rand_word)
        
        if rand_word in Foods:
            print("Hint: Food")
        elif rand_word in Fruits:
            print("Hint: Fruit")
        elif rand_word in Animals:
            print("Hint: Animal")
        elif rand_word in Music:
            print("Hint: Music")
        elif rand_word in Nature:
            print("Hint: Nature")
        elif rand_word in Countries:
            print("Hint: Country")
        elif rand_word in Furniture:
            print("Hint: Furniture")
        elif rand_word in Colors: 
            print("Hint: Color")
            
        print('\n')
      
        alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                     "p","q","r","s","t","u","v","w","x","y","z"]
        l2 = []
        l_00 = []
        rand_word_low = rand_word.lower()
        for char in rand_word_low:
            if char in alphabet_list:
                l2.append("_ ")
            else:
                l2.append("  ")
        l_00 = "".join(l2)
        print('\n',l_00)
        print('\n') 
        
        
        l1 = []
        for i in rand_word_low:
            l1.append(i)
    
    
        life = 8
        rep_check= []
        not_allowed_letters = ["`","1","2","3","4","5","6","7","8","9","0","-","=","/","?",".",">","<",",","_","+",")"
                              ,"(","*","&","^","%","$","#","@","!","~","|","}","{","[","]",":",";"," ",""]
        
        while life > 0 and "_ " in l2:
            print('\n')
            letter = input('Please enter a letter: ').lower()
            if letter in not_allowed_letters:
                print("\n","This letter is not allowed!","\n")
            elif letter in l1 and letter not in l2:
                while letter in l1:
                    lettr_idx = l1.index(letter) 
                    l2[lettr_idx] = letter
                    l1[lettr_idx] = '_' 
                    l3 = ''.join(l2)
                print('\n',l3)
                
            elif letter in l2:
                print("\n","You can't use repetitive letter!","\n")
            elif letter not in l1:
                if letter not in rep_check:
                    life -=1
                    if life > 0:
                        print("\n","Oh no! You've lost a life. Your remaining life= ",life)
                        rep_check.append(letter)
                    else:
                        print("\n","You've Lost! (╥_╥)","\n")
                        print("\n","The correct answer was: ",rand_word,"\n")
                        ans = input('Do you want to play again? Yes or No? : ').lower()
                        if ans == "yes":
                            return Hangman()
                        else:
                            print("\n","Thanks for playind this game. Bye ღゝ◡╹)ノ♡  ")
                            raise SystemExit
                            
                        
                else:
                    print("\n","You can't use repetitive letter!","\n")
        if life > 0:            
            print("\n","Congrats! You've WON! ヽ(๑>ᴗ<๑)ノ")
            print('\n')
            ans = input('Do you want to play again? Yes or No? : ').lower()
            if ans == "yes":
                return Hangman()
            else:
                print("\n","Thanks for playing this game ღゝ◡╹)ノ♡ ")
                raise SystemExit
                
    print("\n","WoOoW, You've finished the game and Now you're a Free Man (ノ^o^)ノ ")
    raise SystemExit  
          
Hangman()