// History and science tables: civilisations, leaders, key texts, instruments, animal facts, operas.
module.exports = [
  {
    pack: 'his-civilisations', cat: 'his', cols: ['what', 'who', 'd'],
    rows: `
built Machu Picchu high in the Andes|The Incas|1
built the temple complex of Angkor Wat|The Khmer|3
built the step pyramid of Chichen Itza|The Maya|2
built the city of Tenochtitlan on a lake|The Aztecs|2
built the stone city of Great Zimbabwe|The Shona|4
carved the city of Petra out of rock|The Nabataeans|4
made the giant stone moai heads of Easter Island|The Rapa Nui|3
invented cuneiform, one of the first writing systems|The Sumerians|3
built the palace of Knossos on Crete|The Minoans|3
built the cities of Mohenjo-daro and Harappa|The Indus Valley Civilisation|3
carved giant stone heads in ancient Mexico|The Olmecs|4
drew the giant Nazca Lines in the Peruvian desert|The Nazca|3
founded Carthage and spread the alphabet by sea|The Phoenicians|3
built the ceremonial city of Persepolis|The Persians|3
built the Hanging Gardens, one of the Seven Wonders|The Babylonians|2
built the Colosseum and Hadrian's Wall|The Romans|1
built the Parthenon|The ancient Greeks|1
built Hagia Sophia as a church|The Byzantines|3
built the Taj Mahal|The Mughals|2
built the Alhambra palace in Granada|The Moors|3
raided Europe in longships|The Vikings|1
built the Topkapı Palace in Istanbul|The Ottomans|3
made bronze "Benin Bronzes" sculptures|The Kingdom of Benin|4
built the cliff dwellings at Mesa Verde|The Ancestral Puebloans|5
built the "Lion Gate" at Mycenae|The Mycenaeans|4
built the city of Teotihuacan with its Pyramid of the Sun|The Teotihuacanos|5
used knotted strings called quipu to keep records|The Incas|3
used a 260-day sacred calendar and a "Long Count"|The Maya|3
mummified their dead and built the pyramids of Giza|The ancient Egyptians|1
built Stonehenge|Neolithic Britons|3`,
    qs: [{ q: 'Which people {what}?', a: 'who' }]
  },
  {
    pack: 'his-leaders-country', cat: 'his', cols: ['who', 'country', 'reg', 'd'],
    rows: `
Mustafa Kemal Atatürk|Turkey|me|2
Gamal Abdel Nasser|Egypt|me|3
Jawaharlal Nehru|India|as|2
Indira Gandhi|India|as|2
Mao Zedong|China|as|1
Deng Xiaoping|China|as|3
Ho Chi Minh|Vietnam|as|2
Sukarno|Indonesia|as|3
Lee Kuan Yew|Singapore|as|3
Pol Pot|Cambodia|as|3
Kim Il-sung|North Korea|as|2
Ferdinand Marcos|the Philippines|as|3
Benazir Bhutto|Pakistan|as|3
Golda Meir|Israel|me|3
David Ben-Gurion|Israel|me|3
Muammar Gaddafi|Libya|me|2
Saddam Hussein|Iraq|me|1
Ayatollah Khomeini|Iran|me|2
Haile Selassie|Ethiopia|af|3
Kwame Nkrumah|Ghana|af|3
Jomo Kenyatta|Kenya|af|3
Julius Nyerere|Tanzania|af|4
Idi Amin|Uganda|af|2
Robert Mugabe|Zimbabwe|af|2
Ellen Johnson Sirleaf, Africa's first elected woman president|Liberia|af|4
Fidel Castro|Cuba|am|1
Juan Perón|Argentina|am|3
Salvador Allende|Chile|am|3
Augusto Pinochet|Chile|am|3
Hugo Chávez|Venezuela|am|2
Pierre Trudeau|Canada|am|3
Josip Broz Tito|Yugoslavia|eu|3
Francisco Franco|Spain|eu|2
Charles de Gaulle|France|eu|2
Otto von Bismarck|Germany|eu|2
Giuseppe Garibaldi, the unifier|Italy|eu|3
Benito Mussolini|Italy|eu|1
Winston Churchill|the United Kingdom|eu|1
Margaret Thatcher|the United Kingdom|eu|1
Peter the Great|Russia|eu|2
Catherine the Great|Russia|eu|2
Lech Wałęsa|Poland|eu|3
Václav Havel|Czechoslovakia|eu|4
Éamon de Valera|Ireland|eu|4
Angela Merkel|Germany|eu|1
Jacinda Ardern|New Zealand|oc|2
Julia Gillard, the first female prime minister|Australia|oc|3
Emperor Hirohito|Japan|as|2
Emperor Meiji|Japan|as|3
Nelson Mandela|South Africa|af|1`,
    qs: [{ q: 'Which country did {who} lead?', a: 'country', group: 'reg' }]
  },
  {
    pack: 'his-rulers-empires', cat: 'his', cols: ['who', 'empire', 'd'],
    rows: `
Cleopatra VII|Ptolemaic Egypt|2
Ramesses II|Ancient Egypt|2
Tutankhamun|Ancient Egypt|1
Hammurabi, famous for his law code|Babylon|3
Nebuchadnezzar II|Babylon|3
Cyrus the Great|The Persian Empire|2
Darius I|The Persian Empire|3
Alexander the Great|Macedon|2
Ashoka|The Maurya Empire|4
Akbar|The Mughal Empire|3
Shah Jahan, builder of the Taj Mahal|The Mughal Empire|2
Suleiman the Magnificent|The Ottoman Empire|2
Mehmed II, conqueror of Constantinople|The Ottoman Empire|3
Justinian I|The Byzantine Empire|3
Charlemagne|The Frankish Empire (Carolingian)|3
Mansa Musa, perhaps the richest man in history|The Mali Empire|3
Shaka|The Zulu Kingdom|3
Moctezuma II|The Aztec Empire|3
Atahualpa|The Inca Empire|3
Pachacuti|The Inca Empire|4
Kublai Khan|The Mongol Empire (Yuan China)|3
Qin Shi Huang, first emperor of China|The Qin dynasty|3
Augustus|The Roman Empire|2
Hadrian|The Roman Empire|2
Saladin|The Ayyubid Sultanate|4
Tamerlane (Timur)|The Timurid Empire|4`,
    qs: [{ q: 'Which empire or kingdom did {who} rule?', a: 'empire' }]
  },
  {
    pack: 'his-key-texts', cat: 'his', cols: ['work', 'who', 'd'],
    rows: `
the "I Have a Dream" speech|Martin Luther King Jr.|1
the Gettysburg Address|Abraham Lincoln|1
the "We shall fight on the beaches" speech|Winston Churchill|1
the "Ich bin ein Berliner" speech|John F. Kennedy|2
the "Tear down this wall!" speech|Ronald Reagan|2
the autobiography Long Walk to Freedom|Nelson Mandela|2
The Communist Manifesto (with Friedrich Engels)|Karl Marx|2
Das Kapital|Karl Marx|2
The Prince|Niccolò Machiavelli|2
The Art of War|Sun Tzu|1
On the Origin of Species|Charles Darwin|1
Principia Mathematica (1687)|Isaac Newton|3
The Wealth of Nations|Adam Smith|3
Leviathan|Thomas Hobbes|4
The Republic|Plato|3
The Social Contract|Jean-Jacques Rousseau|4
Meditations|Marcus Aurelius|3
the Ninety-five Theses|Martin Luther|2
The Interpretation of Dreams|Sigmund Freud|3
A Brief History of Time|Stephen Hawking|1
Silent Spring|Rachel Carson|3
The Second Sex|Simone de Beauvoir|4
Two Treatises of Government|John Locke|4
A Vindication of the Rights of Woman|Mary Wollstonecraft|4
the Analects|Confucius|3
the Diary of a Young Girl|Anne Frank|1
I Know Why the Caged Bird Sings|Maya Angelou|3
Thus Spoke Zarathustra|Friedrich Nietzsche|4
Common Sense (1776)|Thomas Paine|4
the Declaration of Independence (main author)|Thomas Jefferson|2`,
    qs: [{ q: 'Who wrote or delivered {work}?', a: 'who' }]
  },
  {
    pack: 'sci-instruments', cat: 'sci', cols: ['tool', 'meas', 'd'],
    rows: `
barometer|Air pressure|2
thermometer|Temperature|1
seismograph|Earthquakes|2
anemometer|Wind speed|2
hygrometer|Humidity|3
odometer|Distance travelled|2
speedometer|Speed|1
altimeter|Altitude|2
ammeter|Electric current|3
voltmeter|Voltage|2
Geiger counter|Radiation|2
sphygmomanometer|Blood pressure|3
rain gauge|Rainfall|1
pedometer|Steps walked|1
tachometer|Engine revolutions (RPM)|3
hydrometer|Density of liquids|4
protractor|Angles|1
sextant|Angle between a star and the horizon|3
light meter|Brightness of light|2
decibel meter|Loudness of sound|2
calorimeter|Heat energy|4
pH meter|Acidity|2
spirometer|Lung capacity|4
manometer|Gas pressure in a tube|4`,
    qs: [
      { q: 'What does a {tool} measure?', a: 'meas' },
      { q: 'Which instrument measures {meas}?', a: 'tool', when: r => r.tool !== 'manometer' && r.tool !== 'calorimeter', dAdd: 1 }
    ]
  },
  {
    pack: 'sci-animal-facts', cat: 'sci', cols: ['fact', 'animal', 'd'],
    rows: `
is the only mammal capable of true flight|Bat|1
is an egg-laying mammal with a duck-like bill|Platypus|1
has three hearts and blue blood|Octopus|2
has black skin under its white-looking fur|Polar bear|2
is the fastest bird in a dive|Peregrine falcon|2
is the largest living bird|Ostrich|1
is the largest fish in the sea|Whale shark|2
is the largest living reptile|Saltwater crocodile|2
can fly backwards|Hummingbird|2
is famous for regrowing its legs, and even parts of its heart and brain|Axolotl|3
produces cube-shaped poo|Wombat|2
has the longest migration of any animal, from Arctic to Antarctic|Arctic tern|3
is the slowest mammal, living upside down in trees|Sloth|1
is a jellyfish that can revert to its younger form, called "immortal"|Turritopsis dohrnii|4
has blue blood used in medical testing and is older than the dinosaurs|Horseshoe crab|3
is the longest-living vertebrate known, living for centuries|Greenland shark|3
is the loudest animal on Earth|Sperm whale|3
has the largest eyes of any animal|Colossal squid|3
gets its pink colour from the shrimp and algae it eats|Flamingo|1
has fingerprints almost identical to humans|Koala|3
sleeps up to 20 hours a day and eats eucalyptus|Koala|2
can change sex from male to female|Clownfish|3
is pound for pound the strongest animal, carrying many times its weight|Dung beetle|3
is the tallest animal|Giraffe|1
has striped skin, not just striped fur|Tiger|3
eats almost nothing but bamboo|Giant panda|1
is the largest animal ever to have lived|Blue whale|1
can survive in space and being frozen, also called the "water bear"|Tardigrade|3
is a mammal with scales that rolls into a ball|Pangolin|2
is the bird famous for mimicking chainsaws and camera shutters|Lyrebird|4
is the scavenger known for its "laughing" call|Hyena|2
is the only big cat that lives in groups called prides|Lion|1
has a horn made of keratin, like fingernails|Rhinoceros|2
has a tongue up to 60 cm long and a long snout for termites|Giant anteater|3
uses echolocation clicks and sleeps with half its brain awake|Dolphin|2
is a bird that cannot fly and lives only in New Zealand, active at night|Kiwi|2
is a marsupial that can hop at over 50 km/h and carries its young in a pouch|Kangaroo|1
is the fish whose males carry and give birth to the babies|Seahorse|2`,
    qs: [{ q: 'Which animal {fact}?', a: 'animal' }]
  },
  {
    pack: 'art-operas', cat: 'art', cols: ['opera', 'composer', 'd'],
    rows: `
Carmen|Georges Bizet|2
La Traviata|Giuseppe Verdi|2
Aida|Giuseppe Verdi|2
Rigoletto|Giuseppe Verdi|3
Nabucco|Giuseppe Verdi|4
Madama Butterfly|Giacomo Puccini|2
La Bohème|Giacomo Puccini|2
Tosca|Giacomo Puccini|3
Turandot (with "Nessun dorma")|Giacomo Puccini|2
The Magic Flute|Wolfgang Amadeus Mozart|2
Don Giovanni|Wolfgang Amadeus Mozart|3
The Marriage of Figaro|Wolfgang Amadeus Mozart|2
The Barber of Seville|Gioachino Rossini|2
William Tell|Gioachino Rossini|3
The Ring Cycle|Richard Wagner|2
Tristan und Isolde|Richard Wagner|3
Fidelio, his only opera|Ludwig van Beethoven|3
L'Orfeo, one of the earliest operas|Claudio Monteverdi|4
Eugene Onegin|Pyotr Ilyich Tchaikovsky|4
Porgy and Bess|George Gershwin|2
Dido and Aeneas|Henry Purcell|4
Peter Grimes|Benjamin Britten|4
Salome|Richard Strauss|4
Cavalleria rusticana|Pietro Mascagni|5
Pagliacci|Ruggero Leoncavallo|5`,
    qs: [{ q: 'Who composed the opera {opera}?', a: 'composer' }]
  }
];
