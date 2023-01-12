#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
suits=("Hearts","Spades","Clubs","Diamonds")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}


# In[10]:


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        


# In[11]:


a=Card("Spades","Seven")


# In[12]:


print(a)


# In[13]:


a.value


# In[14]:


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return new_deck.all_cards.pop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


new_deck=Deck()


# In[16]:


print(new_deck)


# In[315]:


new_deck.shuffle()


# In[316]:


mycard=new_deck.deal_one()


# In[317]:


print(mycard)


# In[318]:


len(new_deck.all_cards)


# In[319]:


first_card=new_deck.all_cards[6]


# In[320]:


print(first_card)


# In[321]:


for card_object in new_deck.all_cards:
    print(card_object)


# In[322]:


len(new_deck.all_cards)


# In[323]:


print(first_card) #after shuffling


# In[324]:


new_deck.shuffle()


# In[325]:


print(new_deck.all_cards[1])


# In[326]:


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        #if it's a list of more than one card
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        #if it's a list of one card
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# In[327]:


new_player=Player("Navya")


# In[328]:


print(new_player)


# In[329]:


new_player.add_cards(mycard)


# In[330]:


print(new_player)


# In[331]:


new_player.add_cards([mycard,mycard,mycard])


# In[332]:


print(new_player)


# In[333]:


new_player.remove_one()


# In[334]:


print(new_player)


# In[374]:


#game setup
player_one=Player("One")
player_two=Player("Two")

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[375]:


game_on=True


# In[377]:


round_number=0

while game_on:
    round_number+=1
    print(f'Round Number : {round_number}')
    if len(player_one.all_cards)==0: #these are the cards which player has it with them in their hands holding it in front of their face.
        print(f'Player 1 lost the game!\nPlayer 2 wins with {len(player_two_cards)} cards!')
        game_on=False
        break 
    if len(player_two.all_cards)==0:
        print(f'Player 2 lost the game!\nPlayer 1 wins with {len(player_one_cards)} cards!')
        game_on=False
        break 
    #start a new round
    player_one_cards=[] #these are the cards which player 1 puts on the table
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards=[]  #these are the cards which player 2 puts on the table
    player_two_cards.append(player_two.remove_one())

    at_war=True
    while at_war:
        if player_one_cards[-1].value>player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
    
        elif player_one_cards[-1].value<player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False
            
        else:
            print("YOU ARE AT WAR!!!")
            
            if len(player_one.all_cards)<5:
                print("Player 1 CANNOT DECLARE A WAR\nPLAYER 2 WINS!")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print("Player 2 CANNOT DECLARE A WAR\nPLAYER 1 WINS!")
                game_on=False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                

                
        
                
                
            
        
        
         
   
     
    

        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




