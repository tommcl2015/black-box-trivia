// Former names, continents, sidekicks, film songs and quotes, board games.
module.exports = [
  {
    pack: 'geo-former-names', cat: 'geo', cols: ['old', 'now', 'kind', 'd'],
    rows: `
Ceylon|Sri Lanka|country|2
Siam|Thailand|country|2
Persia|Iran|country|2
Burma|Myanmar|country|2
Zaire|the Democratic Republic of the Congo|country|3
Rhodesia|Zimbabwe|country|3
the Gold Coast|Ghana|country|3
Abyssinia|Ethiopia|country|3
Dahomey|Benin|country|4
Upper Volta|Burkina Faso|country|4
Bechuanaland|Botswana|country|4
Nyasaland|Malawi|country|4
East Pakistan|Bangladesh|country|3
Swaziland|Eswatini|country|3
Kampuchea|Cambodia|country|4
Formosa|Taiwan|country|3
New Holland|Australia|country|4
Gaul|France|country|3
Hibernia|Ireland|country|4
Caledonia|Scotland|country|4
Bombay|Mumbai|city|1
Madras|Chennai|city|3
Calcutta|Kolkata|city|2
Peking|Beijing|city|1
Canton|Guangzhou|city|3
Saigon|Ho Chi Minh City|city|2
Edo|Tokyo|city|2
Constantinople|Istanbul|city|1
Leningrad|Saint Petersburg|city|2
Stalingrad|Volgograd|city|3
Danzig|Gdańsk|city|3
Königsberg|Kaliningrad|city|4
Pressburg|Bratislava|city|5
Christiania|Oslo|city|4
Batavia|Jakarta|city|4
Rangoon|Yangon|city|3
Salisbury|Harare|city|4
Léopoldville|Kinshasa|city|4
New Amsterdam|New York City|city|2
Lutetia|Paris|city|4
Londinium|London|city|2
Eboracum|York|city|4
Pile o' Bones|Regina|city|5
Bytown|Ottawa|city|4
Yerba Buena|San Francisco|city|4`,
    qs: [
      { q: 'What is the modern name of the place once called {old}?', a: 'now', group: 'kind', when: r => r.kind !== 'skip' },
      { q: 'What was {now} once called?', a: 'old', group: 'kind', unique: true, dAdd: 1, when: r => r.kind !== 'skip' }
    ]
  },
  {
    pack: 'geo-continents', cat: 'geo', cols: ['country', 'cont', 'd'],
    rows: `
Mongolia|Asia|2
Uzbekistan|Asia|3
Laos|Asia|3
Bhutan|Asia|2
Yemen|Asia|3
Oman|Asia|3
Sri Lanka|Asia|1
Nepal|Asia|1
Mali|Africa|2
Niger|Africa|3
Chad|Africa|3
Malawi|Africa|3
Gabon|Africa|3
Djibouti|Africa|3
Eritrea|Africa|3
Botswana|Africa|2
Namibia|Africa|2
Madagascar|Africa|1
Mauritius|Africa|3
Cape Verde|Africa|4
Guyana|South America|3
Suriname|South America|3
Paraguay|South America|2
Uruguay|South America|2
Ecuador|South America|2
Bolivia|South America|2
Belize|North America|3
Honduras|North America|3
Nicaragua|North America|3
Costa Rica|North America|3
Panama|North America|3
Haiti|North America|3
Dominican Republic|North America|3
Moldova|Europe|3
Belarus|Europe|3
Estonia|Europe|2
Slovenia|Europe|2
Montenegro|Europe|3
Albania|Europe|2
Andorra|Europe|2
Liechtenstein|Europe|2
Luxembourg|Europe|1
Malta|Europe|2
Iceland|Europe|1
Fiji|Oceania|2
Samoa|Oceania|2
Tonga|Oceania|2
Vanuatu|Oceania|3
Papua New Guinea|Oceania|2
Kiribati|Oceania|4
Tuvalu|Oceania|4
Solomon Islands|Oceania|3`,
    qs: [{ q: 'On which continent is {country}?', a: 'cont' }]
  },
  {
    pack: 'art-sidekicks', cat: 'art', cols: ['hero', 'side', 'kind', 'd'],
    rows: `
Sherlock Holmes|Dr John Watson|lit|1
Don Quixote|Sancho Panza|lit|2
Batman|Robin|comic|1
Tintin|Snowy|comic|2
Asterix|Obelix|comic|1
Obelix|Dogmatix (Idéfix)|comic|3
Han Solo|Chewbacca|film|1
Luke Skywalker|R2-D2|film|2
Frodo Baggins|Samwise Gamgee|lit|1
Harry Potter's owl|Hedwig|lit|1
Shrek|Donkey|film|1
Mario|Luigi|game|1
Sonic the Hedgehog|Tails|game|2
Scooby-Doo|Shaggy|tv|1
Captain Kirk|Mr. Spock|tv|2
The Doctor's robot dog|K-9|tv|4
Hercule Poirot|Captain Hastings|lit|3
The Lone Ranger|Tonto|film|3
Wallace|Gromit|film|1
Phineas|Ferb|tv|2
SpongeBob|Patrick Star|tv|1
Mulan|Mushu|film|1
Aladdin|Abu the monkey|film|2
Pinocchio|Jiminy Cricket|film|2
Ash Ketchum|Pikachu|game|1
Link|Navi the fairy|game|4
Simba|Timon and Pumbaa|film|1
Peter Pan|Tinker Bell|lit|1
Winnie-the-Pooh|Piglet|lit|1
Fred Flintstone|Barney Rubble|tv|2
Captain America|Bucky Barnes|comic|3
Iron Man's AI butler|J.A.R.V.I.S.|film|3
Rick Sanchez|Morty|tv|2
Bart Simpson|Milhouse|tv|2
Moana|Heihei the rooster|film|3
Rapunzel|Pascal the chameleon|film|3
Ash's rival|Gary Oak|game|4
Pac-Man's wife|Ms. Pac-Man|game|3
Robinson Crusoe|Friday|lit|3
Phileas Fogg|Passepartout|lit|3`,
    qs: [{ q: 'Who is the famous companion of {hero}?', a: 'side', group: 'kind', when: r => !/'s (owl|robot|AI|rival|wife)/.test(r.hero) },
         { q: 'Who or what is {hero}?', a: 'side', group: 'kind', when: r => /'s (owl|robot|AI|rival|wife)/.test(r.hero) }]
  },
  {
    pack: 'ent-film-songs', cat: 'ent', cols: ['song', 'film', 'd'],
    rows: `
Let It Go|Frozen|1
How Far I'll Go|Moana|1
You're Welcome|Moana|2
We Don't Talk About Bruno|Encanto|1
Circle of Life|The Lion King|1
Hakuna Matata|The Lion King|1
Under the Sea|The Little Mermaid|1
Part of Your World|The Little Mermaid|2
A Whole New World|Aladdin|1
Friend Like Me|Aladdin|2
Be Our Guest|Beauty and the Beast|1
Colors of the Wind|Pocahontas|2
I'll Make a Man Out of You|Mulan|2
Reflection|Mulan|3
You've Got a Friend in Me|Toy Story|1
Remember Me|Coco|2
When You Wish Upon a Star|Pinocchio|2
Bare Necessities|The Jungle Book|1
Supercalifragilisticexpialidocious|Mary Poppins|1
Chim Chim Cher-ee|Mary Poppins|2
Do-Re-Mi|The Sound of Music|1
Over the Rainbow|The Wizard of Oz|1
My Heart Will Go On|Titanic|1
I Will Always Love You (Whitney Houston)|The Bodyguard|2
Eye of the Tiger|Rocky III|2
Take My Breath Away|Top Gun|2
(I've Had) The Time of My Life|Dirty Dancing|2
Stayin' Alive|Saturday Night Fever|2
Skyfall|Skyfall|1
Shallow|A Star Is Born|2
Happy (Pharrell Williams)|Despicable Me 2|2
Let's Go Fly a Kite|Mary Poppins|3
Ghostbusters theme|Ghostbusters|1
Don't You (Forget About Me)|The Breakfast Club|3
Lose Yourself|8 Mile|2
This Is Me|The Greatest Showman|2
Naatu Naatu|RRR|3
What Was I Made For?|Barbie|2
Golden|KPop Demon Hunters|2
Footloose|Footloose|1
Mrs. Robinson|The Graduate|3`,
    qs: [{ q: 'Which film features the song "{song}"?', a: 'film', when: r => r.film !== 'x' }]
  },
  {
    pack: 'ent-film-quotes', cat: 'ent', cols: ['quote', 'film', 'd'],
    rows: `
Here's looking at you, kid.|Casablanca|3
There's no place like home.|The Wizard of Oz|1
You're gonna need a bigger boat.|Jaws|2
E.T. phone home.|E.T. the Extra-Terrestrial|1
Houston, we have a problem.|Apollo 13|2
Life is like a box of chocolates.|Forrest Gump|1
I see dead people.|The Sixth Sense|2
You can't handle the truth!|A Few Good Men|3
Why so serious?|The Dark Knight|2
To infinity and beyond!|Toy Story|1
Just keep swimming.|Finding Nemo|1
I'm the king of the world!|Titanic|1
Wax on, wax off.|The Karate Kid|2
Hasta la vista, baby.|Terminator 2: Judgment Day|2
I'm going to make him an offer he can't refuse.|The Godfather|2
Show me the money!|Jerry Maguire|3
You shall not pass!|The Lord of the Rings: The Fellowship of the Ring|2
Keep your friends close, but your enemies closer.|The Godfather Part II|4
Here's Johnny!|The Shining|2
Nobody puts Baby in a corner.|Dirty Dancing|2
Hakuna matata — it means no worries.|The Lion King|1
I am Groot.|Guardians of the Galaxy|1
Wakanda forever!|Black Panther|1
I am inevitable.|Avengers: Endgame|2
Avengers, assemble.|Avengers: Endgame|3
Roads? Where we're going, we don't need roads.|Back to the Future|2
Bond. James Bond.|Dr. No|3
Say hello to my little friend!|Scarface|3
After all, tomorrow is another day!|Gone with the Wind|3
Run, Forrest, run!|Forrest Gump|1
I feel the need — the need for speed!|Top Gun|2
Life finds a way.|Jurassic Park|2
Welcome to Jurassic Park.|Jurassic Park|2
They may take our lives, but they'll never take our freedom!|Braveheart|2
Are you not entertained?|Gladiator|2
I'm walking here!|Midnight Cowboy|5
Toto, I've a feeling we're not in Kansas anymore.|The Wizard of Oz|2
Ogres are like onions.|Shrek|1
The first rule of Fight Club is: you do not talk about Fight Club.|Fight Club|2
Help me, Obi-Wan Kenobi. You're my only hope.|Star Wars|2
No, I am your father.|The Empire Strikes Back|2
Do or do not. There is no try.|The Empire Strikes Back|2`,
    qs: [{ q: 'Which film has the line: "{quote}"', a: 'film', unique: true, when: r => r.film !== 'x' && !/never actually|films$/.test(r.film + r.quote) }]
  },
  {
    pack: 'ent-board-games', cat: 'ent', cols: ['what', 'game', 'd'],
    rows: `
has Mayfair, Park Lane or Boardwalk and "Go to Jail"|Monopoly|1
has you build roads and settlements and trade sheep and ore|Catan|2
asks whether it was Colonel Mustard in the library with the candlestick|Cluedo (Clue)|1
has you fill a 15×15 board with letter tiles worth points|Scrabble|1
has you move up ladders and slide back down|Snakes and Ladders|1
has you drop discs to get four in a row|Connect Four|1
has you remove wooden blocks from a tower without toppling it|Jenga|1
has you sink your opponent's fleet on a hidden grid|Battleship|1
has you place your hands and feet on coloured circles on a mat|Twister|1
has you try to conquer the world with armies on a map|Risk|1
has you collect pie wedges for six categories of questions|Trivial Pursuit|1
has you remove body parts with tweezers without touching the sides|Operation|1
has you match a colour or number and shout its name when down to one card|UNO|1
has a spinner, little cars and life's milestones|The Game of Life|2
has you guess your opponent's character by asking yes/no questions about faces|Guess Who?|1
has you give one-word clues to help your team find secret agents|Codenames|2
has players work together to stop four diseases spreading|Pandemic|3
has you build train routes across a map of North America|Ticket to Ride|2
has you draw pictures for your team to guess|Pictionary|1
is an ancient game of black and white stones from China|Go|2
is the Indian game that "Ludo" is based on|Pachisi|4
is the game where you jump diagonally and crown a king|Checkers (Draughts)|1
is a two-player game with "points" and doubling cube|Backgammon|3
is a Chinese tile game for four players with "dragons" and "winds"|Mahjong|2
has you lay tiles to build a medieval landscape of cities and roads|Carcassonne|3
has you yell "Yahtzee!" for five of a kind with dice|Yahtzee|1
has you hunt down "Mr. X" across London|Scotland Yard|4
has you find words in a grid of 16 letter dice shaken in a box|Boggle|2`,
    qs: [{ q: 'Which game {what}?', a: 'game' }]
  }
];
