letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Point Dictionary
# Add lowercase letters to letters lists and double the points list 
letters += [letter.lower() for letter in letters]
points *= 2

letter_to_points = {
  key: value 
  for key, value in zip(letters, points)
} # Combines list above to dictionary



letter_to_points[" "] = 0 # add key " " with value of 0 to dict 

print(letter_to_points) #Prints new dict

# Score a word

def score_word(word): # Create score_word function
  point_total = 0 
  for letter in word:
    point_total += letter_to_points.get(letter, 0) #Get value of each letter and add to point total (add zero of it's not in the list)
  return point_total # return point total


brownie_points = score_word("CHOC")

print(brownie_points)

# Score a Game

#A dictionary of players containing each word 
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"], 
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points 

update_point_totals()
print(player_to_points)

def play_word(player, word):
  if player not in player_to_words:
    player_to_words[player] = []
  player_to_words[player].append(word)
play_word("Dani", "ASTER")
print(player_to_words)