// More fact tables across categories.
module.exports = [
  {
    pack: 'his-nicknames', cat: 'his', cols: ['nick', 'who', 'd', 'alt'],
    rows: `
The Iron Duke|The Duke of Wellington|3|Wellington;Arthur Wellesley
The Iron Chancellor|Otto von Bismarck|3|Bismarck
Lionheart|Richard I of England|2|Richard I;Richard the Lionheart
The Conqueror|William I of England|2|William the Conqueror;William I
The Little Corporal|Napoleon Bonaparte|3|Napoleon
The Maid of Orléans|Joan of Arc|3
The Lady with the Lamp|Florence Nightingale|2|Nightingale
The Desert Fox|Erwin Rommel|3|Rommel
Old Hickory|Andrew Jackson|4|Jackson
Honest Abe|Abraham Lincoln|2|Lincoln
The Gipper|Ronald Reagan|4|Reagan
Il Duce|Benito Mussolini|3|Mussolini
Bonnie Prince Charlie|Charles Edward Stuart|4|Charles Stuart
The Hammer of the Scots|Edward I of England|4|Edward I
The Red Baron|Manfred von Richthofen|3|von Richthofen;Richthofen
Scarface|Al Capone|2|Capone
The Father of History|Herodotus|4
The Father of Medicine|Hippocrates|3
Barbarossa (Red Beard)|Frederick I, Holy Roman Emperor|5|Frederick Barbarossa;Frederick I
The Scourge of God|Attila the Hun|4|Attila
The Impaler|Vlad III of Wallachia|3|Vlad the Impaler;Vlad Dracula
The Great, who burned the cakes|Alfred the Great|4|Alfred
Mahatma ("great soul")|Mohandas Gandhi|2|Gandhi
The Liberator of South America|Simón Bolívar|3|Bolivar;Bolívar
Madiba|Nelson Mandela|3|Mandela
The Swedish Nightingale|Jenny Lind|5|Lind
Tricky Dick|Richard Nixon|3|Nixon
The Virgin Queen|Elizabeth I|2|Elizabeth the First
The Sun King|Louis XIV|2|Louis 14
The Iron Lady|Margaret Thatcher|1|Thatcher`,
    qs: [{ q: 'Who was nicknamed "{nick}"?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'his-ships', cat: 'his', cols: ['what', 'ship', 'd', 'alt'],
    rows: `
carried Charles Darwin on his voyage to the Galápagos|HMS Beagle|2|Beagle
was Captain Cook's ship on his first Pacific voyage|HMS Endeavour|3|Endeavour
was Admiral Nelson's flagship at Trafalgar|HMS Victory|3|Victory
was Francis Drake's ship on his voyage around the world|Golden Hind|4|The Golden Hind
was Henry VIII's warship that sank in 1545 and was raised in 1982|Mary Rose|3|The Mary Rose
was the Swedish warship that sank on its maiden voyage in 1628, now in a Stockholm museum|Vasa|4|The Vasa
was the liner sunk by a German U-boat in 1915, helping bring the US into WWI|Lusitania|3|RMS Lusitania
was the German battleship sunk in 1941 after sinking HMS Hood|Bismarck|3
was Shackleton's ship, crushed by ice in 1915 and found on the seabed in 2022|Endurance|3
was the fastest tea clipper of its day, now preserved in Greenwich|Cutty Sark|3
is the US Navy warship nicknamed "Old Ironsides"|USS Constitution|4|Constitution
was the battleship sunk at Pearl Harbor, now a memorial|USS Arizona|3|Arizona
was the tanker that caused a huge Alaskan oil spill in 1989|Exxon Valdez|3
was the cruise ship that capsized off Italy in 2012|Costa Concordia|3
was the Greenpeace ship bombed by French agents in New Zealand in 1985|Rainbow Warrior|4
was the world's first nuclear-powered submarine|USS Nautilus|4|Nautilus
was the ship that carried the Pilgrims to America in 1620|Mayflower|1|The Mayflower
was Columbus's flagship in 1492|Santa María|2|Santa Maria`,
    qs: [{ q: 'Which famous ship {what}?', a: 'ship', alt: 'alt' }]
  },
  {
    pack: 'his-first-leaders', cat: 'his', cols: ['role', 'country', 'who', 'd', 'alt'],
    rows: `
President|the United States|George Washington|1|Washington
President|post-Soviet Russia|Boris Yeltsin|3|Yeltsin
black President|South Africa|Nelson Mandela|2|Mandela
President|Kenya|Jomo Kenyatta|4|Kenyatta
President|Ghana|Kwame Nkrumah|4|Nkrumah
President|Indonesia|Sukarno|4
Prime Minister|independent India|Jawaharlal Nehru|3|Nehru
Governor-General|Pakistan|Muhammad Ali Jinnah|4|Jinnah
Prime Minister|Israel|David Ben-Gurion|3|Ben-Gurion
President|the Republic of Turkey|Mustafa Kemal Atatürk|3|Atatürk;Ataturk
President|Tanzania|Julius Nyerere|4|Nyerere
President|Zambia|Kenneth Kaunda|4|Kaunda
Prime Minister|Singapore|Lee Kuan Yew|3|Lee Kuan Yew
Prime Minister|Malaysia|Tunku Abdul Rahman|5
President|the Czech Republic|Václav Havel|4|Havel;Vaclav Havel
Chancellor|West Germany|Konrad Adenauer|4|Adenauer
President|Bangladesh|Sheikh Mujibur Rahman|5|Mujibur Rahman
President|Senegal|Léopold Sédar Senghor|5|Senghor
President|Botswana|Seretse Khama|5|Khama
Prime Minister|Canada|John A. Macdonald|2|Macdonald;John Macdonald
Prime Minister|Australia|Edmund Barton|4|Barton
President|the People's Republic of China|Mao Zedong|2|Mao
President|Ukraine|Leonid Kravchuk|5|Kravchuk`,
    qs: [{ q: 'Who was the first {role} of {country}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'his-builders', cat: 'his', cols: ['what', 'who', 'd', 'alt'],
    rows: `
the moai statues of Easter Island|the Rapa Nui people|3|Rapa Nui
Chichén Itzá|the Maya|2|Maya;Mayans
Angkor Wat|the Khmer Empire|2|Khmer
the Parthenon|the ancient Greeks|1|Greeks;Ancient Greeks
the Colosseum|the Romans|1|Romans
Petra|the Nabataeans|4|Nabataeans
Great Zimbabwe|the Shona people|4|Shona
Mohenjo-daro|the Indus Valley Civilization|4|Indus Valley
the Nazca Lines|the Nazca people|3|Nazca
Tenochtitlan|the Aztecs|2|Aztec;Mexica
the Terracotta Army|the Qin dynasty|3|Qin
the Hagia Sophia|the Byzantines|3|Byzantine Empire;Byzantine
the Alhambra|the Nasrid dynasty|5|Nasrids;Moors
the palace of Knossos|the Minoans|4|Minoan
the Lion Gate of Mycenae|the Mycenaeans|4|Mycenaean
Persepolis|the Persians|3|Achaemenid Persians;Persian Empire
the Pyramids of Giza|the ancient Egyptians|1|Egyptians
Machu Picchu|the Incas|1|Inca
Hadrian's Wall|the Romans|1|Romans`,
    qs: [{ q: 'Who built {what}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-paintings2', cat: 'art', cols: ['p', 'who', 'd', 'alt'],
    rows: `
The Garden of Earthly Delights|Hieronymus Bosch|4|Bosch
The Arnolfini Portrait|Jan van Eyck|4|van Eyck
Las Meninas|Diego Velázquez|4|Velazquez;Velázquez
The Third of May 1808|Francisco Goya|4|Goya
Saturn Devouring His Son|Francisco Goya|4|Goya
Liberty Leading the People|Eugène Delacroix|3|Delacroix
The Raft of the Medusa|Théodore Géricault|4|Gericault;Géricault
Impression, Sunrise, which named a movement|Claude Monet|3|Monet
Water Lilies|Claude Monet|2|Monet
Luncheon of the Boating Party|Pierre-Auguste Renoir|4|Renoir
A Sunday Afternoon on the Island of La Grande Jatte|Georges Seurat|4|Seurat
The Card Players|Paul Cézanne|4|Cezanne;Cézanne
The Sleeping Gypsy|Henri Rousseau|5|Rousseau
The Dance|Henri Matisse|4|Matisse
The Son of Man, with an apple in front of the face|René Magritte|3|Magritte
The Treachery of Images ("This is not a pipe")|René Magritte|3|Magritte
Nighthawks|Edward Hopper|3|Hopper
American Gothic|Grant Wood|3|Wood
Whistler's Mother|James McNeill Whistler|3|Whistler
The Hay Wain|John Constable|4|Constable
The Fighting Temeraire|J. M. W. Turner|4|Turner
Ophelia, floating in a stream|John Everett Millais|4|Millais
The Great Wave off Kanagawa|Hokusai|2|Katsushika Hokusai
The Kiss, covered in gold leaf|Gustav Klimt|3|Klimt
Sunflowers|Vincent van Gogh|1|Van Gogh
Café Terrace at Night|Vincent van Gogh|3|Van Gogh
The Swing|Jean-Honoré Fragonard|5|Fragonard
The Creation of Adam|Michelangelo|2
The School of Athens|Raphael|3
Primavera|Sandro Botticelli|4|Botticelli
The Ambassadors, with a hidden skull|Hans Holbein the Younger|4|Holbein
Napoleon Crossing the Alps|Jacques-Louis David|4|David
The Death of Marat|Jacques-Louis David|4|David
Wanderer above the Sea of Fog|Caspar David Friedrich|4|Friedrich
The Gleaners|Jean-François Millet|5|Millet
Olympia|Édouard Manet|4|Manet
Christina's World|Andrew Wyeth|4|Wyeth
Marilyn Diptych|Andy Warhol|3|Warhol
Girl with Balloon|Banksy|2`,
    qs: [{ q: 'Who painted "{p}"?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-museums', cat: 'art', cols: ['m', 'city', 'd'],
    rows: `
the Uffizi Gallery|Florence|3
the Van Gogh Museum|Amsterdam|2
the Museum of Modern Art (MoMA)|New York City|2
the Metropolitan Museum of Art|New York City|2
Tate Modern|London|2
the National Gallery|London|3
the British Museum|London|2
the Musée d'Orsay|Paris|3
the Vatican Museums|Vatican City|2
the Getty Center|Los Angeles|3
the Art Institute of Chicago|Chicago|2
the Smithsonian Institution|Washington, D.C.|2
the Acropolis Museum|Athens|2
the Grand Egyptian Museum, opened in 2025|Giza|3
the Pergamon Museum|Berlin|4
the Kunsthistorisches Museum|Vienna|4
the National Palace Museum|Taipei|4
the Louvre Abu Dhabi|Abu Dhabi|2
the Mauritshuis, home of "Girl with a Pearl Earring"|The Hague|4
the Munch Museum|Oslo|3
the Dalí Theatre-Museum|Figueres|5
Frida Kahlo's Blue House (Casa Azul)|Mexico City|3
the Zeitz Museum of Contemporary Art Africa|Cape Town|4`,
    qs: [{ q: 'In which city is {m}?', a: 'city' }]
  },
  {
    pack: 'geo-flags', cat: 'geo', cols: ['what', 'country', 'd'],
    rows: `
a red circle on a white background|Japan|1
a green cedar tree|Lebanon|2
an outline map of the island|Cyprus|3
a Maasai shield and two spears|Kenya|3
an AK-47 rifle|Mozambique|4
a starry globe with the motto "Ordem e Progresso"|Brazil|2
a blue 24-spoke wheel|India|2
a red-and-blue yin-yang circle and four black trigrams|South Korea|2
a blue Star of David|Israel|1
a white dragon|Bhutan|3
a lion holding a sword|Sri Lanka|3
a grey crowned crane|Uganda|4
an eagle eating a snake on a cactus|Mexico|2
a sun with a face, the "Sun of May"|Argentina|3
a black double-headed eagle on red|Albania|3
the temple of Angkor Wat|Cambodia|3
a frigatebird flying over a rising sun|Kiribati|5
a bird-of-paradise|Papua New Guinea|4
a black trident|Barbados|4
two crossed keys|Vatican City|3
a purple Sisserou parrot|Dominica|5`,
    qs: [{ q: "Which country's flag shows {what}?", a: 'country' }]
  },
  {
    pack: 'geo-seas-straits', cat: 'geo', cols: ['what', 'name', 'kind', 'd'],
    rows: `
lies between Italy and the Balkan Peninsula|Adriatic Sea|sea|2
lies between Africa and the Arabian Peninsula|Red Sea|sea|2
lies between Greece and Turkey|Aegean Sea|sea|2
lies between Ireland and Great Britain|Irish Sea|sea|2
lies between Great Britain and Scandinavia|North Sea|sea|2
lies between Japan and the Korean Peninsula|Sea of Japan|sea|3
lies between China and the Korean Peninsula|Yellow Sea|sea|3
lies between India and the Arabian Peninsula|Arabian Sea|sea|3
lies between Alaska and Russia|Bering Sea|sea|3
lies between Australia and New Zealand|Tasman Sea|sea|2
is enclosed by Turkey, Ukraine, Georgia, Romania and Bulgaria|Black Sea|sea|2
separates Spain from Morocco|Strait of Gibraltar|strait|2
runs through Istanbul, linking the Black Sea to the Sea of Marmara|Bosphorus|strait|3
separates Russia from Alaska|Bering Strait|strait|2
separates Iran from Oman, a key route for oil tankers|Strait of Hormuz|strait|3
separates Malaysia from the Indonesian island of Sumatra|Strait of Malacca|strait|4
separates New Zealand's North and South Islands|Cook Strait|strait|3
separates mainland Australia from Tasmania|Bass Strait|strait|3
runs past the tip of South America, through Chile|Strait of Magellan|strait|3
separates Denmark from Sweden, crossed by a famous bridge|Øresund|strait|4
separates Sicily from mainland Italy|Strait of Messina|strait|4
separates England from France at its narrowest point|Strait of Dover|strait|3`,
    qs: [{ q: 'Which body of water {what}?', a: 'name', group: 'kind' }]
  },
  {
    pack: 'geo-deserts', cat: 'geo', cols: ['desert', 'where', 'd'],
    rows: `
Gobi|Mongolia and China|2
Kalahari|southern Africa|2
Namib|Namibia|3
Mojave|the United States|3
Thar|India and Pakistan|3
Great Victoria|Australia|3
Simpson|Australia|4
Taklamakan|China|4
Karakum|Turkmenistan|5
Patagonian|Argentina|4
Negev|Israel|4
Atacama|Chile|2`,
    qs: [{ q: 'Where is the {desert} Desert?', a: 'where' }]
  },
  {
    pack: 'geo-nicknames', cat: 'geo', cols: ['nick', 'place', 'kind', 'd'],
    rows: `
the Land of the Midnight Sun|Norway|country|3
the Emerald Isle|Ireland|country|1
the Land of Smiles|Thailand|country|3
the Pearl of Africa|Uganda|country|4
the Rainbow Nation|South Africa|country|2
the Land of the Long White Cloud|New Zealand|country|3
the Land Down Under|Australia|country|1
the Hermit Kingdom|North Korea|country|3
the Land of the Thunder Dragon|Bhutan|country|4
the Spice Isle|Grenada|country|4
the Middle Kingdom|China|country|3
the Lion City|Singapore|city|3
the Eternal City|Rome|city|2
the City of Light|Paris|city|2
the City of a Hundred Spires|Prague|city|4
the Pink City|Jaipur|city|4
the City of Angels|Los Angeles|city|1
the Mile High City|Denver|city|3
the Motor City|Detroit|city|2
the Big Easy|New Orleans|city|2
the Emerald City|Seattle|city|4
Auld Reekie|Edinburgh|city|4
La Serenissima|Venice|city|4
the Garden City of India|Bangalore|city|4`,
    qs: [{ q: 'Which {kind} is nicknamed "{nick}"?', a: 'place', group: 'kind' }]
  },
  {
    pack: 'spo-stadiums', cat: 'spo', cols: ['s', 'city', 'd'],
    rows: `
Wembley Stadium|London|1
Camp Nou|Barcelona|2
the Santiago Bernabéu|Madrid|2
Old Trafford|Manchester|2
Anfield|Liverpool|2
the San Siro|Milan|3
the Maracanã|Rio de Janeiro|3
the Allianz Arena|Munich|3
Lord's Cricket Ground|London|3
the Melbourne Cricket Ground|Melbourne|2
Eden Gardens|Kolkata|4
Yankee Stadium|New York City|2
Fenway Park|Boston|2
Wrigley Field|Chicago|3
Lambeau Field|Green Bay|3
Madison Square Garden|New York City|2
the Estadio Azteca|Mexico City|3
Croke Park|Dublin|3
Murrayfield|Edinburgh|3
Twickenham|London|3
the Stade de France|Paris|2
the Bell Centre|Montreal|3
Augusta National Golf Club|Augusta|2
Roland Garros|Paris|2
Flushing Meadows, home of the US Open|New York City|3
Melbourne Park, home of the Australian Open|Melbourne|3`,
    qs: [{ q: 'In which city is {s}?', a: 'city' }]
  },
  {
    pack: 'spo-trophies', cat: 'spo', cols: ['t', 'sport', 'd'],
    rows: `
the Ryder Cup|Golf|2
the Solheim Cup|Golf|4
the Claret Jug|Golf|3
the Green Jacket|Golf|2
the Davis Cup|Tennis|2
the Billie Jean King Cup|Tennis|3
the Venus Rosewater Dish|Tennis|4
the Webb Ellis Cup|Rugby|3
the Calcutta Cup|Rugby|4
the Ashes|Cricket|2
the Larry O'Brien Trophy|Basketball|3
the Commissioner's Trophy|Baseball|4
the Thomas Cup|Badminton|5
the Sam Maguire Cup|Gaelic football|5
the yellow jersey (maillot jaune)|Cycling|2
the Vince Lombardi Trophy|American football|2
the Stanley Cup|Ice hockey|1`,
    qs: [{ q: 'In which sport do teams or players compete for {t}?', a: 'sport' }]
  },
  {
    pack: 'spo-gems-anniversaries', cat: 'spo', cols: ['q', 'a', 'kind', 'd'],
    rows: `
January's birthstone|Garnet|stone|3
February's birthstone|Amethyst|stone|3
March's birthstone|Aquamarine|stone|3
April's birthstone|Diamond|stone|3
May's birthstone|Emerald|stone|3
June's birthstone|Pearl|stone|3
July's birthstone|Ruby|stone|3
August's birthstone|Peridot|stone|4
September's birthstone|Sapphire|stone|3
October's birthstone|Opal|stone|3
November's birthstone|Topaz|stone|4
December's birthstone|Turquoise|stone|4
the traditional gift for a 1st wedding anniversary|Paper|anniv|3
the traditional gift for a 5th wedding anniversary|Wood|anniv|3
the traditional gift for a 10th wedding anniversary|Tin|anniv|4
the traditional gift for a 20th wedding anniversary|China|anniv|4
the traditional gift for a 25th wedding anniversary|Silver|anniv|2
the traditional gift for a 30th wedding anniversary|Pearl|anniv|3
the traditional gift for a 40th wedding anniversary|Ruby|anniv|3
the traditional gift for a 50th wedding anniversary|Gold|anniv|1
the traditional gift for a 60th wedding anniversary|Diamond|anniv|2`,
    qs: [{ q: 'What is {q}?', a: 'a', group: 'kind' }]
  },
  {
    pack: 'sci-rocks', cat: 'sci', cols: ['what', 'a', 'kind', 'd'],
    rows: `
granite|Igneous|type|3
basalt|Igneous|type|3
obsidian, a natural volcanic glass|Igneous|type|3
pumice, a rock that can float|Igneous|type|3
marble|Metamorphic|type|3
slate|Metamorphic|type|3
quartzite|Metamorphic|type|4
gneiss|Metamorphic|type|4
sandstone|Sedimentary|type|3
limestone|Sedimentary|type|3
chalk|Sedimentary|type|3
shale|Sedimentary|type|4
the softest mineral on the Mohs scale, with a hardness of 1|Talc|mohs|3
the hardest natural mineral, with a Mohs hardness of 10|Diamond|mohs|1
the mineral rated 7 on the Mohs scale, common in sand|Quartz|mohs|4
the mineral rated 9 on the Mohs scale, the family of rubies and sapphires|Corundum|mohs|5
the mineral rated 2 on the Mohs scale, used to make plaster|Gypsum|mohs|4
the mineral rated 3 on the Mohs scale, the main part of limestone|Calcite|mohs|4`,
    qs: [
      { q: 'What type of rock is {what}?', a: 'a', group: 'kind', when: r => r.kind === 'type' },
      { q: 'What is {what}?', a: 'a', group: 'kind', when: r => r.kind === 'mohs' }
    ]
  },
  {
    pack: 'sci-vitamins', cat: 'sci', cols: ['q', 'a', 'd'],
    rows: `
Which vitamin deficiency causes scurvy, once common among sailors?|Vitamin C|2
Which vitamin does your skin make in sunlight?|Vitamin D|2
A lack of which vitamin causes rickets, which softens children's bones?|Vitamin D|3
A lack of which vitamin causes night blindness?|Vitamin A|3
Which vitamin helps your blood to clot?|Vitamin K|3
A lack of which vitamin, thiamine, causes beriberi?|Vitamin B1|4
Which vitamin is also called folic acid when made in a lab?|Vitamin B9|5
Which vitamin is mainly found in animal foods, so vegans often take it as a supplement?|Vitamin B12|3`,
    qs: [{ q: '{q}', a: 'a' }]
  },
  {
    pack: 'sci-animal-homes', cat: 'sci', cols: ['animal', 'where', 'd'],
    rows: `
lemurs|Madagascar|2
giant pandas|China|1
kiwi birds|New Zealand|1
quokkas|Australia|3
kakapo parrots|New Zealand|4
okapis|Democratic Republic of the Congo|4
Tasmanian devils|Tasmania|2
axolotls|Mexico|3
orangutans|Borneo and Sumatra|3
Komodo dragons|Indonesia|2
red pandas|the Himalayas|3
llamas|the Andes of South America|2
capybaras|South America|2
platypuses|Australia|2
snow leopards|Central Asia's mountains|3
polar bears|the Arctic|1
emperor penguins|Antarctica|1
proboscis monkeys|Borneo|4
Galápagos giant tortoises|Ecuador|3
aye-ayes|Madagascar|4`,
    qs: [{ q: 'In the wild, where do {animal} live?', a: 'where' }]
  }
];
