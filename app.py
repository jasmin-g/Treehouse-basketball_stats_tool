import copy
from constants import TEAMS
from constants import PLAYERS
import random

players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)


def clean_data(players):
    for player in players_copy:
        player['height'] = int(player['height'].replace(' inches', ''))
        player['guardians'] = player['guardians'].split(' and ')
        
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False    
            
            
def balance_teams(teams, players):
    experienced = []
    inexperienced = []
    balanced_teams = {}
    
    for player in players_copy:
            if player['experience'] == True:
                experienced.append(player)
            else:
                inexperienced.append(player)
    
    for team in teams_copy:    
        balanced_teams[team] = random.sample(experienced, int(len(players_copy)/6)) +\
            random.sample(inexperienced, int(len(players_copy)/6))
        
        for player in balanced_teams[team]:
            
            if player in experienced:
                experienced.remove(player)
            elif player in inexperienced:
                inexperienced.remove(player)
    
    return balanced_teams
  
  
def display_stats(team):
    num_players = len(team)
    num_experienced = 0
    num_inexperienced = 0
    guardians_lst = []
    players_lst = []
    avg_height = 0    
    
    
    for player in team:
        players_lst.append(player['name'])
        guardians_lst.append(player['guardians'])
        avg_height  += player['height']
        
        if player['experience'] == True:
            num_experienced += 1
        else:
            num_inexperienced += 1 
            
    avg_height = round(avg_height/num_players,2)  
        
    print(f'Total players: {num_players}')
    print(f'Experienced players: {num_experienced}')
    print(f'Ixperienced players: {num_inexperienced}')
    print(f'Average height: {avg_height}\n')
    print('Players on team:\n', ', '.join(players_lst))
    print('\nGuardians:\n', ', '.join(', '.join(l) for l in guardians_lst))
            
      
      
def menu():
    print('BASKETBALL TEAM STATS TOOL\n')
    print('-' *4, 'MENU', '-' *4,'\n')
    print('Here are your choices:\n')
    print(' 1) Display Team Stats\n')
    print(' 2) Quit\n')
    
    choice = input('Enter an option: ')
    while (choice != '1') & (choice != '2'):
        print('Please enter either 1 or 2')
        choice = input('Enter an option: ')
   
    if choice == '1':
        choice_1 = input('\nChoose a team:\n1) Panthers\n2) Bandits\n3) Warriors\n'
                        )
        while (choice_1 != '1') & (choice_1 != '2') & (choice_1 != '3'):
            print('Please enter either 1, 2 or 3')
            choice_1 = input('\nChoose a team:\n1) Panthers\n2) Bandits\n3) Warriors\n')
            
        if choice_1 == '1':
            print('\nTeam: Panthers Stats\n')
            print('-'*20,'\n')
            display_stats(teams['Panthers'])
        elif choice_1 == '2':
            print('\nTeam: Bandits Stats\n')
            print('-'*20,'\n')
            display_stats(teams['Bandits'])
        elif choice_1 == '3': 
            print('\nTeam: Warriors Stats\n')
            print('-'*20,'\n')
            display_stats(teams['Warriors'])
            
            
    elif choice == '2':
        print('Thank you for using the Basketball Stats Tool. Have a great day!')
        
        
        
if __name__ == "__main__":
    players = clean_data(players_copy)
    teams = balance_teams(teams_copy, players)
    menu()        
      