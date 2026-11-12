/* Hand-written topic pages for the crawlable trivia library (/trivia/<slug>).
 * Each topic pulls its questions from the pack files in data/new (optionally only some "# --- Section ---" blocks);
 * only questions that are actually in the live game are shown. Intros and facts are written for the page. */
module.exports = [
  // ---------------- History ----------------
  {
    slug: 'world-war-2', cat: 'his', title: 'World War II trivia',
    desc: 'World War II trivia questions with answers: D-Day, the Dambusters, Bletchley Park, the Pacific war and the home front.',
    src: [['033-his-world-wars.txt', ['World War II']], ['037-his-ww2-more.txt'], ['038-his-war-tech.txt', ['WWII: codes and computers', 'WWII: radar, jets and rockets']]],
    intro: [
      'The Second World War ran from 1939 to 1945 and reached almost every corner of the globe. It is also one of the richest seams in trivia: code names, daring raids, secret machines and turning-point battles that people still argue about at the pub.',
      'These questions run from the easy (which beaches did the Allies land on?) to the properly tricky (what was the code name for the dams raid?). Tap "Show answer" to check yourself.'
    ],
    facts: [
      'The D-Day landings on 6 June 1944 used five beaches, code-named Utah, Omaha, Gold, Juno and Sword.',
      'The codebreakers at Bletchley Park built Colossus, one of the first programmable electronic computers, to read German high-command messages.',
      'The Dambusters raid of May 1943 used a "bouncing bomb" designed by Barnes Wallis.'
    ]
  },
  {
    slug: 'world-war-1', cat: 'his', title: 'World War I trivia',
    desc: 'First World War trivia with answers: the trenches, the first tanks, famous battles and how the Great War began and ended.',
    src: [['033-his-world-wars.txt', ['World War I']], ['038-his-war-tech.txt', ['WWI: the tank and more']]],
    intro: [
      'The First World War, once called the Great War, lasted from 1914 to 1918. It brought the world tanks, poison gas, aerial dogfights and the long misery of the trenches.',
      'This set covers how the war started, the big battles, the new machines and the armistice that ended the fighting at the eleventh hour of the eleventh day of the eleventh month.'
    ],
    facts: [
      'The first tanks went into battle at Flers-Courcelette, during the Battle of the Somme, in September 1916.',
      'The British called their new machines "tanks" partly to keep them secret: workers were told they were building water tanks.',
      'The armistice came into force at 11 a.m. on 11 November 1918, which is why Remembrance Day falls on 11 November.'
    ]
  },
  {
    slug: 'atomic-age', cat: 'his', title: 'The atomic age: trivia questions',
    desc: 'Atomic age trivia with answers: the Manhattan Project, the first nuclear tests, the first reactors, Chernobyl and the Cold War.',
    src: [['036-his-atomic-age.txt']],
    intro: [
      'In a little over a decade, splitting the atom went from a laboratory surprise to a bomb, and then to a power source lighting cities. This set follows that story from the Manhattan Project to the nuclear accidents and stand-offs of the Cold War.',
      'Expect questions on the first tests by each nuclear power, the scientists behind them, the first reactors, and the science of how it all works.'
    ],
    facts: [
      'The first nuclear reactor, Chicago Pile-1, went critical under the stands of a squash court at the University of Chicago in December 1942.',
      'The first nuclear test, code-named Trinity, took place in the New Mexico desert on 16 July 1945.',
      'Obninsk, near Moscow, began feeding electricity from a nuclear reactor into the grid in 1954.'
    ]
  },
  {
    slug: 'who-am-i-history', cat: 'his', title: 'Who am I? Famous people from history',
    desc: 'Who am I trivia: guess the famous historical figure from three clues, hardest clue first. Lincoln, JFK, Napoleon, the Tudors and more.',
    src: [['028-who-am-i.txt'], ['048-who-am-i.txt'], ['052-who-am-i-history-tricky.txt']],
    intro: [
      'Who am I? questions give you clues about a famous person, starting with the hardest. The fewer clues you need, the bigger your bragging rights.',
      'This set mixes presidents, emperors, royals, explorers and thinkers, plus some of the people standing just behind them: the assassin, the bodyguard, the spouse who outlived them.'
    ],
    facts: [
      'Abraham Lincoln is the only US president to hold a patent, for a device to lift boats over shoals.',
      'Napoleon was not unusually short: the legend comes partly from the difference between French and English inches.',
      'Henry VIII had six wives; a schoolroom rhyme remembers their fates: divorced, beheaded, died, divorced, beheaded, survived.'
    ]
  },
  {
    slug: 'what-year', cat: 'his', title: 'What year? History trivia',
    desc: 'What year did it happen? Trivia questions with answers on big moments in history, science and pop culture.',
    src: [['046-his-what-year.txt'], ['305-facts-his-dates.txt']],
    intro: [
      'Dates are the backbone of history, and a staple of every pub quiz. Some you will know cold; others you will have to reason your way to from what was happening around them.',
      'A good trick: anchor on a date you are sure of, then ask whether the event came before or after it.'
    ],
    facts: [
      'The Berlin Wall fell in 1989, twenty-eight years after it went up in 1961.',
      'The Wright brothers first flew at Kitty Hawk, North Carolina, in 1903; Neil Armstrong walked on the Moon just 66 years later.',
      'The first email was sent by Ray Tomlinson in 1971, and he picked the @ sign to separate the user from the computer.'
    ]
  },
  {
    slug: 'world-leaders-and-empires', cat: 'his', title: 'World history trivia: royals, empires and leaders',
    desc: 'World history trivia with answers: royals, empires, wars, famous leaders, disasters and mysteries.',
    src: [['024-his-world.txt'], ['304-facts-his-leaders.txt'], ['306-facts-his-ancient.txt']],
    intro: [
      'From the pharaohs to prime ministers, world history is full of characters. This set covers royal families, the rise and fall of empires, famous leaders and the disasters and mysteries that still get people talking.',
      'It is a broad mix, so there should be something here for everyone.'
    ],
    facts: [
      'Queen Elizabeth II reigned for 70 years, the longest of any British monarch.',
      'The Great Pyramid of Giza was the tallest human-made structure in the world for more than 3,800 years.',
      'The Roman Empire in the west fell in 476 AD, but the eastern half carried on as the Byzantine Empire until 1453.'
    ]
  },

  // ---------------- Entertainment ----------------
  {
    slug: 'the-simpsons', cat: 'ent', title: 'The Simpsons trivia',
    desc: 'The Simpsons trivia questions with answers: Springfield, the family, famous episodes, catchphrases and side characters.',
    src: [['031-ent-simpsons.txt']],
    intro: [
      'The Simpsons first appeared as short sketches on The Tracey Ullman Show in 1987 and became a half-hour series in 1989. It is the longest-running American scripted primetime series, which means there is an awful lot of trivia to go round.',
      'These questions cover the family, the town of Springfield, famous episodes and the side characters fans love.'
    ],
    facts: [
      'Matt Groening named Homer, Marge, Lisa and Maggie after members of his own family.',
      'Springfield was chosen because it is one of the most common town names in the United States, so nobody can say exactly which state it is in.',
      'Bart is an anagram of "brat".'
    ]
  },
  {
    slug: 'harry-potter', cat: 'ent', title: 'Harry Potter trivia',
    desc: 'Harry Potter trivia questions with answers: Hogwarts, spells, houses, Quidditch and the people of the wizarding world.',
    src: [['040-ent-fan-hp-sw-lotr.txt', ['Harry Potter']]],
    intro: [
      'Seven books, eight films and a whole wizarding world: Harry Potter is one of the most popular trivia subjects there is. These questions are for fans who know their Hufflepuffs from their horcruxes.',
      'They cover the books and the films, from the Sorting Hat to the final battle.'
    ],
    facts: [
      'The first book was published in the UK in 1997 as Harry Potter and the Philosopher\'s Stone; the US edition was renamed the Sorcerer\'s Stone.',
      'There are four Hogwarts houses: Gryffindor, Hufflepuff, Ravenclaw and Slytherin.',
      'Quidditch is played with three kinds of ball: the Quaffle, two Bludgers and the Golden Snitch.'
    ]
  },
  {
    slug: 'star-wars', cat: 'ent', title: 'Star Wars trivia',
    desc: 'Star Wars trivia questions with answers: the Skywalkers, Jedi and Sith, droids, ships and planets from a galaxy far, far away.',
    src: [['040-ent-fan-hp-sw-lotr.txt', ['Star Wars']]],
    intro: [
      'A long time ago, in 1977, George Lucas released a space adventure that changed the movie business for good. Star Wars trivia is a test of how well you know the saga\'s heroes, villains, droids and ships.',
      'The questions run from the original trilogy through the prequels, the sequels and the TV series.'
    ],
    facts: [
      'The first film was later retitled Star Wars: Episode IV – A New Hope.',
      'The Millennium Falcon made the Kessel Run in less than twelve parsecs, which is a distance, not a time.',
      'Darth Vader was played on set by David Prowse, while James Earl Jones provided his voice.'
    ]
  },
  {
    slug: 'lord-of-the-rings', cat: 'ent', title: 'The Lord of the Rings & The Hobbit trivia',
    desc: 'Lord of the Rings and Hobbit trivia with answers: Middle-earth, the Fellowship, the Ring and the people and places of Tolkien.',
    src: [['040-ent-fan-hp-sw-lotr.txt', ['The Lord of the Rings / The Hobbit']]],
    intro: [
      'J.R.R. Tolkien\'s Middle-earth has been delighting readers since The Hobbit in 1937, and Peter Jackson\'s films brought it to a whole new audience. These questions cover both the books and the films.',
      'One quiz to rule them all, perhaps.'
    ],
    facts: [
      'The Fellowship of the Ring has nine members, to match the nine Black Riders.',
      'Tolkien was a professor of Anglo-Saxon at Oxford and invented several languages for his elves.',
      'The films were shot in New Zealand, and the hobbit village of Hobbiton still stands there as a tourist attraction.'
    ]
  },
  {
    slug: 'friends-office-seinfeld', cat: 'ent', title: 'Friends, The Office and Seinfeld trivia',
    desc: 'Sitcom trivia with answers: Friends, The Office (US) and Seinfeld: characters, catchphrases and famous episodes.',
    src: [['041-ent-fan-sitcoms.txt']],
    intro: [
      'Three of the most rewatched sitcoms ever: six friends in a New York coffee house, a paper company in Scranton, and "a show about nothing". If you have seen every episode more than once, this is your round.',
      'The questions cover characters, catchphrases and the episodes everybody quotes.'
    ],
    facts: [
      'The coffee house in Friends is called Central Perk.',
      'The US version of The Office was adapted from the British series created by Ricky Gervais and Stephen Merchant.',
      'Seinfeld was co-created by Jerry Seinfeld and Larry David, who later made Curb Your Enthusiasm.'
    ]
  },
  {
    slug: 'disney-pixar-marvel', cat: 'ent', title: 'Disney, Pixar and Marvel trivia',
    desc: 'Disney, Pixar and Marvel trivia questions with answers: animated classics, Pixar favourites and the Marvel Cinematic Universe.',
    src: [['042-ent-fan-disney-marvel-tv.txt', ['Disney & Pixar', 'Marvel']]],
    intro: [
      'From Snow White in 1937 to the Avengers, the Disney family of studios has made many of the films people grew up with. This set mixes animated classics, Pixar favourites and the Marvel Cinematic Universe.',
      'A good round for families: the kids will often beat the grown-ups.'
    ],
    facts: [
      'Snow White and the Seven Dwarfs (1937) was the first full-length cel-animated feature film.',
      'Toy Story (1995) was the first feature film made entirely with computer animation.',
      'The Marvel Cinematic Universe began with Iron Man in 2008.'
    ]
  },
  {
    slug: 'tv-dramas-sci-fi', cat: 'ent', title: 'Game of Thrones, Breaking Bad, Star Trek & Doctor Who trivia',
    desc: 'TV trivia with answers: Game of Thrones, Breaking Bad, Star Trek and Doctor Who.',
    src: [['042-ent-fan-disney-marvel-tv.txt', ['Game of Thrones', 'Breaking Bad', 'Star Trek', 'Doctor Who']]],
    intro: [
      'Two of the most talked-about dramas of the 2010s and two science-fiction institutions that have been running, on and off, since the 1960s.',
      'Questions on houses and dragons, a chemistry teacher gone bad, the starship Enterprise and a time-travelling police box.'
    ],
    facts: [
      'Doctor Who first aired in 1963, and the TARDIS is disguised as a 1960s police box.',
      'The original Star Trek series ran for three seasons, from 1966 to 1969.',
      'Game of Thrones is based on George R. R. Martin\'s books, A Song of Ice and Fire.'
    ]
  },
  {
    slug: 'music-by-decade', cat: 'ent', title: 'Music trivia by decade: 1960s to 2010s',
    desc: 'Music trivia questions with answers, decade by decade: the 60s, 70s, 80s, 90s, 2000s and 2010s.',
    src: [['032-ent-music-decades.txt'], ['308-facts-ent-songs.txt']],
    intro: [
      'Every decade has its sound: the British Invasion, disco, synth-pop, grunge, the iPod era and the streaming age. This set takes you through sixty years of hits, bands and big moments.',
      'If you can hum it, you can probably answer it.'
    ],
    facts: [
      'The Beatles hold the record for the most number-one albums on the UK chart.',
      'Michael Jackson\'s Thriller (1982) is widely cited as the best-selling album of all time.',
      'MTV launched in 1981 by playing "Video Killed the Radio Star" by the Buggles.'
    ]
  },
  {
    slug: 'oscars', cat: 'ent', title: 'Oscars trivia',
    desc: 'Academy Awards trivia with answers: Best Picture winners, acting records, firsts and famous Oscar moments.',
    src: [['010-ent-oscars-fun.txt'], ['300-facts-ent-oscars.txt'], ['301-facts-ent-oscars-acting.txt']],
    intro: [
      'The first Academy Awards were handed out in 1929, and the ceremony has been producing records, upsets and famous moments ever since.',
      'This set covers Best Picture winners, acting awards, record-holders and some of the strangest nights in Oscar history.'
    ],
    facts: [
      'Wings won the first award for the year\'s best picture, at the first ceremony in 1929.',
      'Ben-Hur, Titanic and The Lord of the Rings: The Return of the King share the record of 11 Oscars each.',
      'Katharine Hepburn won four Best Actress awards, more than any other performer in an acting category.'
    ]
  },
  {
    slug: 'movie-titles-in-other-words', cat: 'ent', title: 'Movie titles in other words',
    desc: 'Guess the movie from a synonym version of its title: "The Shadowy Cavalier" is The Dark Knight. Movie title trivia with answers.',
    src: [['049-ent-movie-title-synonyms.txt']],
    intro: [
      'Each question takes a famous film title and swaps every word for a synonym. "The Shadowy Cavalier" is The Dark Knight; "Chilled Solid" is Frozen.',
      'It is part vocabulary test, part movie knowledge, and great fun with a group.'
    ],
    facts: [
      'A cavalier is a horseman or knight, which is how "The Shadowy Cavalier" becomes The Dark Knight.',
      'Title puzzles like these are a staple of party games because you can solve them from either end: the words or the films.',
      'Try writing your own: "Arachnid Guy" and "Phantom Smashers" are good places to start.'
    ]
  },
  {
    slug: 'finish-the-title', cat: 'ent', title: 'Finish the title',
    desc: 'Finish the title trivia: complete the name of the famous film, book, song or TV show. Questions with answers.',
    src: [['047-finish-the-title.txt']],
    intro: [
      'You get the start of a famous title; you supply the rest. Films, books, songs and TV shows are all fair game.',
      'It sounds easy until your mind goes blank halfway through.'
    ],
    facts: [
      'Long titles are often shortened by fans: Dr. Strangelove\'s full title is Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb.',
      'Many famous book titles come from older works: Of Mice and Men borrows a line from a Robert Burns poem.',
      'Finishing a title is a good warm-up round for a trivia night: everyone feels they know the answer.'
    ]
  },
  {
    slug: 'who-am-i-fictional', cat: 'ent', title: 'Who am I? Fictional characters',
    desc: 'Who am I trivia for fictional characters: Luke Skywalker, Darth Vader, John McClane, Tony Soprano and more. Three clues each.',
    src: [['051-who-am-i-fictional.txt']],
    intro: [
      'Three clues, one famous character from film, TV or books. The first clue is the hardest; by the third, most people will have it.',
      'Heroes, villains and antiheroes are all here.'
    ],
    facts: [
      'John McClane, the hero of Die Hard, was played by Bruce Willis.',
      'Tony Soprano was played by James Gandolfini over six seasons of The Sopranos.',
      'Sherlock Holmes has been played on screen by more actors than almost any other character.'
    ]
  },
  {
    slug: 'movie-quotes', cat: 'ent', title: 'Famous movie quotes trivia',
    desc: 'Famous movie quotes trivia with answers: which film, which character, and what comes next.',
    src: [['043-pub-classics-1.txt', ['Famous movie quotes']]], match: /(film|movie).*(line|quote|says|said)|(line|quote).*(film|movie)/i,
    intro: [
      'Some lines escape their films and become part of everyday speech. Can you name the movie each famous line comes from?',
      'A classic pub-quiz round that works for every age group.'
    ],
    facts: [
      'Humphrey Bogart never actually says "Play it again, Sam" in Casablanca; the line is "Play it, Sam."',
      '"Here\'s looking at you, kid" is also from Casablanca (1942).',
      'Darth Vader\'s famous reveal is "No, I am your father", not "Luke, I am your father".'
    ]
  },
  {
    slug: 'tv-catchphrases-and-decades', cat: 'ent', title: 'TV catchphrases, theme songs and "name the decade"',
    desc: 'TV trivia with answers: catchphrases, theme songs and name-the-decade questions.',
    src: [['015-ent-themes-decades.txt']],
    intro: [
      'Catchphrases, theme tunes and the fads that pin a moment to its decade. A nostalgic round for anyone who grew up in front of the TV.',
      'For the decade questions, look for clues in the technology, the fashions and the slang.'
    ],
    facts: [
      'The Friends theme, "I\'ll Be There for You", was recorded by The Rembrandts.',
      'Name-the-decade questions are easier if you remember when things were invented: the Walkman arrived in 1979, the iPod in 2001.',
      'Many theme songs were written for the show and later became radio hits.'
    ]
  },

  // ---------------- Arts & Literature ----------------
  {
    slug: 'english-expressions', cat: 'art', title: 'English expressions and idioms',
    desc: 'What does it mean? English idioms and expressions trivia with answers: break a leg, spill the beans, bite the bullet and more.',
    src: [['050-art-english-expressions.txt']],
    intro: [
      'English is full of phrases that make no sense if you take them literally. Nobody is breaking a leg, and there are no beans to spill.',
      'Test how well you know what everyday expressions really mean, and which expression matches each meaning.'
    ],
    facts: [
      '"Mind your Ps and Qs" means "mind your manners"; nobody agrees for certain where it comes from.',
      'A "red herring" is a false clue; strong-smelling smoked fish were said to have been used to throw hounds off a scent.',
      '"Bob\'s your uncle" is British slang for "and there you have it".'
    ]
  },
  {
    slug: 'shakespeare', cat: 'art', title: 'Shakespeare trivia',
    desc: 'Shakespeare trivia questions with answers: the plays, the characters and famous lines.',
    src: [['312-facts-art-shakespeare.txt']],
    intro: [
      'William Shakespeare wrote around 39 plays and 154 sonnets, and his words are still all around us. This round is about the plays: which character is in which, and where the famous lines come from.',
      'You do not need to have read them all, but it helps.'
    ],
    facts: [
      'Shakespeare was born and buried in Stratford-upon-Avon.',
      'Shakespeare\'s plays popularised everyday phrases such as "wild-goose chase" and "break the ice".',
      'The Globe Theatre in London is a modern reconstruction, opened in 1997 near the site of the original.'
    ]
  },
  {
    slug: 'famous-paintings-and-art', cat: 'art', title: 'Art trivia: famous paintings and artists',
    desc: 'Art trivia questions with answers: famous paintings, the artists who made them, art heists and architecture.',
    src: [['310-facts-art-paintings.txt'], ['025-art-books-words.txt', ['Art, heists & architecture']]],
    intro: [
      'From the Mona Lisa to The Starry Night, some paintings are so famous everyone knows them. But who painted them, and where do they hang?',
      'This set also includes famous art heists and some of the world\'s great buildings. For a visual version, try our Famous paintings picture quiz.'
    ],
    facts: [
      'The Mona Lisa was stolen from the Louvre in 1911 and was missing for more than two years.',
      'Vincent van Gogh painted The Starry Night in 1889 while staying at an asylum in Saint-Rémy-de-Provence.',
      'Edvard Munch made several versions of The Scream, in paint and pastel.'
    ]
  },
  {
    slug: 'classical-composers', cat: 'art', title: 'Classical music trivia: composers',
    desc: 'Classical music trivia with answers: famous composers and their best-known works.',
    src: [['311-facts-art-composers.txt']],
    intro: [
      'Bach, Mozart, Beethoven and the rest: you know the names and probably the tunes. But can you match the composer to the piece?',
      'A good round for anyone who learned an instrument as a child.'
    ],
    facts: [
      'Beethoven continued to compose after he lost his hearing, including his Ninth Symphony.',
      'Mozart wrote his first compositions when he was about five years old.',
      'Vivaldi\'s The Four Seasons is a set of four violin concertos.'
    ]
  },
  {
    slug: 'norse-mythology', cat: 'art', title: 'Norse mythology trivia',
    desc: 'Norse mythology trivia with answers: Odin, Thor, Loki, Asgard, Valhalla and Ragnarök.',
    src: [['044-pub-classics-2.txt', ['Norse mythology']]], match: /norse|\bodin\b|\bthor\b|valhalla|asgard|\bloki\b|valkyr|ragnar|yggdrasil|bifr/i, exclude: /marvel|avenger|hemsworth|hiddleston|film|movie/i,
    intro: [
      'The gods of the Vikings have had a second life in comics and films, but the myths are stranger than any movie. Here are questions on the gods, the nine worlds and the end of everything.',
      'You will meet a one-eyed god, an eight-legged horse and a trickster who changes shape.'
    ],
    facts: [
      'Thursday is named after Thor and Wednesday after Odin, also called Woden.',
      'The world tree Yggdrasil connects the nine worlds of Norse myth.',
      'Ragnarök is the battle at the end of the world, in which many of the gods die.'
    ]
  },
  {
    slug: 'authors-and-books', cat: 'art', title: 'Books and authors trivia',
    desc: 'Literature trivia with answers: famous books and their authors, classics, famous lines and bestsellers.',
    src: [['307-facts-art-authors.txt'], ['025-art-books-words.txt', ['Classics & famous lines', 'Bestsellers & book-to-film']]],
    intro: [
      'Who wrote it? A simple question that catches people out all the time. This set covers the classics, famous first lines and modern bestsellers that became films.',
      'Readers of every age should find something they know.'
    ],
    facts: [
      'Mary Shelley began writing Frankenstein when she was 18.',
      'Charles Dickens published most of his novels in monthly or weekly instalments.',
      'Agatha Christie is often cited as the best-selling novelist of all time.'
    ]
  },

  // ---------------- Science & Nature ----------------
  {
    slug: 'space', cat: 'sci', title: 'Space trivia',
    desc: 'Space trivia questions with answers: planets, moons, spacecraft, astronauts and the fastest and farthest things ever launched.',
    src: [['023-sci-space.txt'], ['318-facts-sci-moons.txt']],
    intro: [
      'Planets, moons, rockets and records: space is one of the most popular trivia categories, and one of the most surprising.',
      'Find out how well you know the solar system and the history of exploring it.'
    ],
    facts: [
      'Jupiter is the largest planet in the solar system; more than 1,000 Earths would fit inside it.',
      'Voyager 1, launched in 1977, is the most distant human-made object.',
      'A day on Venus (one full rotation) is longer than its year.'
    ]
  },
  {
    slug: 'weather', cat: 'sci', title: 'Weather trivia',
    desc: 'Weather trivia with answers: record temperatures, hurricanes, tornadoes, lightning and wild winters.',
    src: [['017-sci-weather.txt']],
    intro: [
      'Everybody talks about the weather. This round is about its extremes: the hottest, coldest, windiest and wettest places on Earth, and how storms work.',
      'For something more visual, try the Cloud types picture quiz.'
    ],
    facts: [
      'Lightning is about five times hotter than the surface of the Sun.',
      'Hurricanes, typhoons and cyclones are the same kind of storm with different names in different oceans.',
      'The coldest temperature ever measured at a weather station, −89.2 °C, was recorded at Vostok Station in Antarctica in 1983.'
    ]
  },
  {
    slug: 'myths-and-the-human-body', cat: 'sci', title: 'Myth or fact? Science and the human body',
    desc: 'Myth or fact trivia with answers: busted science myths, the human body and everyday science.',
    src: [['029-sci-myths-body.txt']],
    intro: [
      'Do we only use 10% of our brains? Can you see the Great Wall of China from space? This round busts common myths and tests what you know about the body you live in.',
      'Some answers will surprise you.'
    ],
    facts: [
      'The adult human body has 206 bones; a newborn has around 300, many of which fuse as it grows.',
      'The Great Wall of China is very hard to see with the naked eye from orbit, despite the popular claim.',
      'Brain scans show we use virtually all of our brain, not 10%.'
    ]
  },
  {
    slug: 'deadly-and-weird-nature', cat: 'sci', title: 'Deadly, record-breaking and weird nature',
    desc: 'Nature trivia with answers: the deadliest animals, natural records and weird-but-true facts about the living world.',
    src: [['016-sci-deadly-weird.txt']],
    intro: [
      'The most dangerous animal is smaller than you think, and the natural world is stranger than any fiction. This round covers the deadly, the record-breaking and the just plain odd.',
      'Not one for the squeamish.'
    ],
    facts: [
      'The mosquito, by spreading diseases such as malaria, is often called the deadliest animal to humans.',
      'Blue whales are the largest animals known to have ever lived.',
      'An octopus has three hearts and blue blood.'
    ]
  },
  {
    slug: 'technology-and-science-firsts', cat: 'sci', title: 'Technology and science firsts',
    desc: 'Science and technology trivia with answers: the first transistor, first computers, inventors and famous firsts.',
    src: [['039-sci-tech-firsts.txt'], ['313-facts-sci-inventors.txt']],
    intro: [
      'Who invented it, and when? This set covers the transistor, the first computers, the telephone, radio and the scientists behind the breakthroughs that shape daily life.',
      'Good preparation for the Famous inventions picture round.'
    ],
    facts: [
      'The transistor was invented at Bell Labs in 1947.',
      'Alexander Graham Bell was granted the patent for the telephone in 1876.',
      'Tim Berners-Lee proposed the World Wide Web in 1989 while working at CERN.'
    ]
  },
  {
    slug: 'dinosaurs', cat: 'sci', title: 'Dinosaur trivia',
    desc: 'Dinosaur trivia questions with answers: T. rex, Triceratops, Stegosaurus, the extinction and more.',
    src: [['044-pub-classics-2.txt', ['Dinosaurs']]], match: /dinosaur|tyrannosaur|triceratops|stegosaur|velociraptor|brachiosaur|diplodocus|ankylosaur|pterodactyl|pteranodon|jurassic period|cretaceous/i,
    intro: [
      'Dinosaurs ruled the Earth for more than 160 million years. This round is for every child who could name them all, and every adult who still can.',
      'It covers the famous species, when they lived, and what happened to them.'
    ],
    facts: [
      'The word dinosaur means "terrible lizard".',
      'Birds are living dinosaurs, descended from small feathered theropods.',
      'Tyrannosaurus rex lived closer in time to us than to Stegosaurus.'
    ]
  },
  {
    slug: 'chemical-elements', cat: 'sci', title: 'Chemical elements trivia',
    desc: 'Periodic table trivia with answers: element symbols, atomic numbers and where elements got their names.',
    src: [['319-facts-sci-elements.txt']],
    intro: [
      'The periodic table has 118 elements, and their symbols do not always match their English names: think Fe for iron or Au for gold.',
      'This round tests symbols, names and a few chemistry facts.'
    ],
    facts: [
      'Hydrogen is the most abundant element in the universe.',
      'Gold\'s symbol, Au, comes from the Latin word aurum.',
      'Several elements are named after places, including germanium, francium and americium.'
    ]
  },
  {
    slug: 'riddles-and-maths-puzzles', cat: 'sci', title: 'Riddles and easy maths puzzles',
    desc: 'Riddles and maths puzzles with answers, from As I was going to St Ives to quick mental arithmetic brain teasers.',
    src: [['035-puzzles-riddles.txt']],
    intro: [
      'Not every trivia question is about facts. These riddles and puzzles test how you think: some are classic brain-teasers, some are quick mental arithmetic.',
      'Read carefully. Many of them are designed to trip you up.'
    ],
    facts: [
      'The St Ives riddle has a trick answer: only the narrator is going to St Ives.',
      'Similar counting riddles appear in the Rhind papyrus, an Egyptian maths text more than 3,500 years old.',
      'The best way to solve a riddle is often to question an assumption you did not notice you were making.'
    ]
  },

  // ---------------- Geography ----------------
  {
    slug: 'capital-cities', cat: 'geo', title: 'Capital cities trivia',
    desc: 'Capital cities quiz with answers: name the capital of countries around the world.',
    src: [['314-facts-geo-capitals.txt']],
    intro: [
      'A geography classic. Some capitals are obvious, others catch out nearly everyone: it is Canberra, not Sydney, and Ottawa, not Toronto.',
      'For a picture-based version, try the Flags and Country shapes quizzes.'
    ],
    facts: [
      'Australia\'s capital, Canberra, was purpose-built as a compromise between Sydney and Melbourne.',
      'La Paz in Bolivia is the highest seat of government in the world, at about 3,600 metres.',
      'Some countries have more than one capital: South Africa has three.'
    ]
  },
  {
    slug: 'us-states', cat: 'geo', title: 'US states trivia',
    desc: 'US states trivia with answers: state capitals, nicknames and facts about all 50 states.',
    src: [['315-facts-geo-usstates.txt']],
    intro: [
      'Fifty states, fifty capitals and a lot of nicknames. How well do you know the map of the United States?',
      'For a visual challenge, try the US states picture quiz, where you name each state from its outline.'
    ],
    facts: [
      'Alaska is the largest US state by area, more than twice the size of Texas.',
      'Hawaii is the only US state made up entirely of islands.',
      'Many state capitals are not the largest city in their state: Albany, not New York City, and Sacramento, not Los Angeles.'
    ]
  },
  {
    slug: 'world-records', cat: 'geo', title: 'World records: tallest, longest, oldest',
    desc: 'World records trivia with answers: tallest buildings, longest bridges and railways, oldest things and record-breaking structures.',
    src: [['021-geo-records.txt'], ['022-sci-obscure-records.txt']],
    intro: [
      'Tallest, longest, oldest, fastest, biggest. This round is about records: the buildings, bridges, railways and machines that set them.',
      'Records change, and we update these questions when they do.'
    ],
    facts: [
      'The Burj Khalifa in Dubai, opened in 2010, is the tallest building in the world at 828 metres.',
      'The Trans-Siberian Railway from Moscow to Vladivostok is the longest railway line in the world.',
      'The Great Pyramid of Giza is the only one of the Seven Wonders of the Ancient World still standing.'
    ]
  },
  {
    slug: 'geography-quirks', cat: 'geo', title: 'Fun geography: quirks and who-knew facts',
    desc: 'Fun geography trivia with answers: strange borders, odd place names, landmarks and surprising facts about the world.',
    src: [['011-geo-fun.txt'], ['316-facts-geo-landmarks.txt']],
    intro: [
      'Geography is more than capitals. This round is about the odd corners of the map: strange borders, surprising neighbours, and landmarks with stories behind them.',
      'For pictures, try our Landmarks and Mountains & volcanoes quizzes.'
    ],
    facts: [
      'Russia spans eleven time zones.',
      'Canada has the longest coastline of any country.',
      'Vatican City is the smallest country in the world, at less than half a square kilometre.'
    ]
  },

  // ---------------- Sports & Leisure ----------------
  {
    slug: 'olympics', cat: 'spo', title: 'Olympics trivia',
    desc: 'Olympic Games trivia with answers: host cities, famous athletes and records from the Summer and Winter Games.',
    src: [['302-facts-spo-olympics.txt']],
    intro: [
      'The modern Olympic Games began in Athens in 1896. Since then they have produced legends, records and a long list of host cities.',
      'This round covers both the Summer and Winter Games.'
    ],
    facts: [
      'The five Olympic rings stand for the five inhabited continents taking part in the Games.',
      'Michael Phelps has won more Olympic medals than any other athlete, with 28.',
      'The first Winter Olympics were held in Chamonix, France, in 1924.'
    ]
  },
  {
    slug: 'fifa-world-cup', cat: 'spo', title: 'Football World Cup trivia',
    desc: 'FIFA World Cup trivia with answers: winners, hosts, finals and record-breakers since 1930.',
    src: [['303-facts-spo-worldcup.txt']],
    intro: [
      'The first World Cup was played in Uruguay in 1930, and the hosts won it. Since then the tournament has become the most-watched sporting event on the planet.',
      'Test what you know about winners, hosts and famous finals.'
    ],
    facts: [
      'Brazil has won the men\'s World Cup five times, more than any other country.',
      'The 2026 World Cup is co-hosted by Canada, Mexico and the United States, the first with three host countries.',
      'Miroslav Klose of Germany holds the record for most goals at men\'s World Cups, with 16.'
    ]
  },
  {
    slug: 'hockey-nfl-nba-mlb', cat: 'spo', title: 'Big leagues trivia: hockey, NFL, NBA and MLB',
    desc: 'North American sports trivia with answers: NHL, NFL, NBA, MLB and CFL legends, records and lore.',
    src: [['014-spo-leagues.txt']],
    intro: [
      'Legends, records and trophies from the big North American leagues: hockey, American football, basketball, baseball and the Canadian Football League.',
      'A good round for the sports fans in the group.'
    ],
    facts: [
      'The Stanley Cup, first awarded in 1893, is the oldest professional sports trophy in North America.',
      'Wayne Gretzky holds the NHL record for career points, with 2,857.',
      'The Super Bowl trophy is named after Vince Lombardi.'
    ]
  },
  {
    slug: 'ncaa-team-colours', cat: 'spo', title: 'NCAA teams with a colour in their name',
    desc: 'College sports trivia: NCAA schools and teams with a colour in their name, from the Crimson Tide to the Blue Devils.',
    src: [['045-spo-ncaa-colours.txt']],
    intro: [
      'From the Crimson Tide to the Big Green, a surprising number of US college teams carry a colour in their name. Can you name the school from the clue?',
      'A fun round for college sports fans, and a tough one for everyone else.'
    ],
    facts: [
      'Alabama\'s teams are the Crimson Tide.',
      'Duke\'s teams are the Blue Devils.',
      'Dartmouth\'s teams are known as the Big Green.'
    ]
  },
  {
    slug: 'motor-racing-and-sailing', cat: 'spo', title: 'Formula 1, NASCAR and sailing trivia',
    desc: 'Motor racing and sailing trivia with answers: Formula 1 champions, NASCAR and IndyCar, famous yachts and sailors.',
    src: [['019-spo-racing-sailing.txt']],
    intro: [
      'Fast cars and fast boats. This round covers Formula 1 champions, NASCAR and IndyCar legends, the America\'s Cup and famous sailors, real and fictional.',
      'For a visual challenge, try the Racing circuits picture quiz: name the track from its outline.'
    ],
    facts: [
      'Michael Schumacher and Lewis Hamilton share the record of seven Formula 1 world titles.',
      'The Indianapolis 500 was first run in 1911.',
      'The America\'s Cup, first contested in 1851, is the oldest international sporting trophy still competed for.'
    ]
  },
  {
    slug: 'golf', cat: 'spo', title: 'Golf trivia',
    desc: 'Golf trivia with answers: birdies and eagles, the majors, the Masters green jacket and golf legends.',
    src: [['044-pub-classics-2.txt', ['Golf']]], match: /\bgolf|ryder cup|\bthe masters\b|birdie|bogey|green jacket|augusta/i,
    intro: [
      'Birdies, bogeys and the green jacket. This round covers the language of golf, the four majors and the players who dominated them.',
      'Good for the golfers in the group, and a learning experience for everyone else.'
    ],
    facts: [
      'A birdie is one under par, an eagle two under, and an albatross three under.',
      'St Andrews in Scotland is known as the Home of Golf.',
      'Jack Nicklaus won 18 major championships, the most in men\'s golf.'
    ]
  },
  {
    slug: 'food-and-drink', cat: 'spo', title: 'Food and drink trivia',
    desc: 'Food and drink trivia with answers: national dishes, cocktails, cheeses, beer and famous eats from around the world.',
    src: [['044-pub-classics-2.txt', ['Food & drink']], ['018-spo-food-drink.txt'], ['317-facts-spo-dishes.txt']],
    intro: [
      'National dishes, famous cocktails and what goes into them. A round that tends to make everybody hungry.',
      'It covers food and drink from around the world.'
    ],
    facts: [
      'Paella comes from Valencia in Spain.',
      'Hummus is made mostly from chickpeas.',
      'Parmigiano-Reggiano can only be made in a small area of northern Italy.'
    ]
  },
  {
    slug: 'cars', cat: 'spo', title: 'Car trivia',
    desc: 'Car trivia with answers: car makers, logos, famous models and motoring history.',
    src: [['044-pub-classics-2.txt', ['Cars']], ['026-mixed-world.txt', ['Cars']]],
    intro: [
      'Prancing horses, raging bulls and four interlocking rings. How well do you know the car makers, their logos and their most famous models?',
      'For a historic angle, the Famous inventions picture round includes the Ford Model T.'
    ],
    facts: [
      'Volkswagen means "people\'s car" in German.',
      'Audi\'s four rings stand for the four companies that merged to form Auto Union in 1932.',
      'The Ford Model T went on sale in 1908, and more than 15 million were built.'
    ]
  },
  {
    slug: 'board-games-and-game-shows', cat: 'spo', title: 'Board games, card games and game shows trivia',
    desc: 'Trivia about board games, card games and TV game shows, with answers.',
    src: [['043-pub-classics-1.txt', ['Board & card games', 'Game shows & reality TV']]],
    intro: [
      'From Monopoly to Jeopardy!, games have their own history and their own trivia. This round covers classic board and card games and the TV game shows families have watched for decades.',
      'Fitting, for a trivia game.'
    ],
    facts: [
      'The board for the original US Monopoly uses street names from Atlantic City, New Jersey.',
      'Chess pieces start with the queen on her own colour.',
      'A standard deck of cards has 52 cards, plus jokers.'
    ]
  },
  {
    slug: 'kids-trivia', cat: 'spo', title: 'Trivia for kids',
    desc: 'Easy trivia questions for kids with answers: animals, stories, cartoons, geography and sport. Great for road trips and family nights.',
    src: [['027-kids.txt'], ['034-art-kids-books.txt']],
    intro: [
      'Easy, friendly questions for younger players: animals, fairy tales, cartoons, simple geography and sport. Perfect for car journeys and family nights.',
      'In the game, choose "Easy" difficulty to get questions like these.'
    ],
    facts: [
      'A group of lions is called a pride.',
      'The cheetah is the fastest land animal.',
      'The Very Hungry Caterpillar, by Eric Carle, was first published in 1969.'
    ]
  }
];
