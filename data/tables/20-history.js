// History fact tables.
module.exports = [
  {
    pack: 'his-uk-pms', cat: 'his', cols: ['pm', 'when', 'year', 'd'],
    rows: `
Arthur Balfour|1902|1902|5
Henry Campbell-Bannerman|1905|1905|5
H. H. Asquith|1908|1908|4
David Lloyd George|1916|1916|3
Bonar Law|1922|1922|5
Ramsay MacDonald|1924|1924|4
Neville Chamberlain|1937|1937|3
Winston Churchill|1940|1940|1
Clement Attlee|1945|1945|3
Anthony Eden|1955|1955|4
Harold Macmillan|1957|1957|4
Alec Douglas-Home|1963|1963|5
Harold Wilson|1964|1964|3
Edward Heath|1970|1970|4
James Callaghan|1976|1976|4
Margaret Thatcher|1979|1979|2
John Major|1990|1990|3
Tony Blair|1997|1997|2
Gordon Brown|2007|2007|3
David Cameron|2010|2010|2
Theresa May|2016|2016|2
Boris Johnson|2019|2019|2
Liz Truss|September 2022|2022|3
Rishi Sunak|October 2022|2022|3
Keir Starmer|2024|2024|2`,
    qs: [
      { q: 'Who became Prime Minister of the United Kingdom in {when}?', a: 'pm', near: 'year' },
      { q: 'In which year did {pm} first become British Prime Minister?', a: 'year', years: true, dAdd: 1, when: r => !['Liz Truss', 'Rishi Sunak'].includes(r.pm) }
    ]
  },
  {
    pack: 'his-explorers', cat: 'his', cols: ['who', 'feat', 'from', 'd', 'alt'],
    rows: `
Christopher Columbus|reached the Caribbean in 1492 while sailing for Spain|Genoa|1|Columbus
Vasco da Gama|was the first to sail from Europe to India around Africa, in 1498|Portugal|3|da Gama
Bartolomeu Dias|first sailed around Africa's Cape of Good Hope, in 1488|Portugal|4|Dias
Vasco Núñez de Balboa|was the first European to see the Pacific from the Americas, in 1513|Spain|4|Balboa
James Cook|charted New Zealand and Australia's east coast on HMS Endeavour|Britain|2|Captain Cook;Cook
Marco Polo|travelled to the court of Kublai Khan in the 1270s|Venice|2|Polo
Ibn Battuta|travelled about 120,000 km across Africa and Asia in the 1300s|Morocco|4|Battuta
Zheng He|commanded huge Chinese treasure fleets across the Indian Ocean in the early 1400s|China|4
Leif Erikson|is said to have reached North America around the year 1000|Iceland|3|Leif Ericson;Erikson
Jacques Cartier|sailed up the St. Lawrence River in the 1530s and claimed land for France|France|3|Cartier
John Cabot|reached Newfoundland in 1497, sailing for England|Venice|3|Cabot;Giovanni Caboto
Henry Hudson|explored a giant bay and a New York river that now carry his name|England|3|Hudson
Abel Tasman|was the first European to reach Tasmania and New Zealand, in 1642|Netherlands|4|Tasman
Francis Drake|was the first Englishman to sail around the world, in 1577–80|England|3|Drake
Robert Falcon Scott|reached the South Pole in 1912 but died on the return journey|Britain|3|Scott
Ernest Shackleton|kept his whole crew alive after the ship Endurance was crushed by Antarctic ice|Ireland|3|Shackleton
David Livingstone|was the first European to see Victoria Falls, in 1855|Scotland|3|Livingstone
Henry Morton Stanley|found a missing explorer in 1871 and supposedly said "Dr. Livingstone, I presume?"|Wales|4|Stanley
Thor Heyerdahl|sailed the balsa raft Kon-Tiki across the Pacific in 1947|Norway|4|Heyerdahl
Jacques Cousteau|co-invented the Aqua-Lung and filmed the undersea world|France|3|Cousteau
Meriwether Lewis and William Clark|led the US Corps of Discovery to the Pacific coast in 1804–06|United States|3|Lewis and Clark
Tenzing Norgay|reached the top of Everest with Edmund Hillary in 1953|Nepal|3|Tenzing
Valentina Tereshkova|became the first woman in space, in 1963|Soviet Union|3|Tereshkova`,
    qs: [
      { q: 'Which explorer {feat}?', a: 'who', alt: 'alt' },
      { q: 'Where was {who} from?', a: 'from', dAdd: 1, when: r => !['Leif Erikson', 'Ernest Shackleton', 'Tenzing Norgay'].includes(r.who) }
    ]
  },
  {
    pack: 'his-war-years', cat: 'his', cols: ['war', 'start', 'end', 'd'],
    rows: `
World War I|1914|1918|1
World War II|1939|1945|1
the American Civil War|1861|1865|2
the American Revolutionary War|1775|1783|3
the Korean War|1950|1953|3
the Vietnam War|1955|1975|3
the Gulf War|1990|1991|3
the Crimean War|1853|1856|4
the Second Boer War|1899|1902|4
the Spanish Civil War|1936|1939|3
the Seven Years' War|1756|1763|4
the Thirty Years' War|1618|1648|4
the Hundred Years' War|1337|1453|5
the Russo-Japanese War|1904|1905|5
the Mexican–American War|1846|1848|5
the Falklands War|1982|1982|3
the Six-Day War|1967|1967|3
the Iraq War|2003|2011|3`,
    qs: [
      { q: 'In which year did {war} begin?', a: 'start', years: true, when: r => r.start !== r.end },
      { q: 'In which year did {war} end?', a: 'end', years: true, dAdd: 1, when: r => r.start !== r.end },
      { q: 'In which year was {war} fought?', a: 'start', years: true, when: r => r.start === r.end }
    ]
  },
  {
    pack: 'his-quotes', cat: 'his', cols: ['quote', 'who', 'kind', 'd'],
    rows: `
I think, therefore I am.|René Descartes|thinker|2
The only thing we have to fear is fear itself.|Franklin D. Roosevelt|leader|3
Ask not what your country can do for you; ask what you can do for your country.|John F. Kennedy|leader|2
We choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard.|John F. Kennedy|leader|3
Mr. Gorbachev, tear down this wall!|Ronald Reagan|leader|2
Never in the field of human conflict was so much owed by so many to so few.|Winston Churchill|leader|3
I have nothing to offer but blood, toil, tears and sweat.|Winston Churchill|leader|3
Give me liberty, or give me death!|Patrick Henry|leader|4
Four score and seven years ago...|Abraham Lincoln|leader|3
A house divided against itself cannot stand.|Abraham Lincoln|leader|4
The lady's not for turning.|Margaret Thatcher|leader|3
The buck stops here.|Harry S. Truman|leader|4
Read my lips: no new taxes.|George H. W. Bush|leader|4
I am not a crook.|Richard Nixon|leader|3
Speak softly and carry a big stick.|Theodore Roosevelt|leader|3
Peace for our time.|Neville Chamberlain|leader|4
Yes we can.|Barack Obama|leader|2
Injustice anywhere is a threat to justice everywhere.|Martin Luther King Jr.|leader|3
The unexamined life is not worth living.|Socrates|thinker|3
God is dead.|Friedrich Nietzsche|thinker|3
Man is born free, and everywhere he is in chains.|Jean-Jacques Rousseau|thinker|4
Religion is the opium of the people.|Karl Marx|thinker|3
Hell is other people.|Jean-Paul Sartre|thinker|4
Knowledge is power.|Francis Bacon|thinker|4
If I have seen further, it is by standing on the shoulders of giants.|Isaac Newton|scientist|3
Eureka!|Archimedes|scientist|2
Give me a place to stand and I will move the Earth.|Archimedes|scientist|4
Genius is one percent inspiration and ninety-nine percent perspiration.|Thomas Edison|scientist|3
Imagination is more important than knowledge.|Albert Einstein|scientist|3
The medium is the message.|Marshall McLuhan|thinker|4
In the future, everyone will be world-famous for 15 minutes.|Andy Warhol|artist|3
I can resist everything except temptation.|Oscar Wilde|writer|3
Not all those who wander are lost.|J.R.R. Tolkien|writer|3
All happy families are alike; each unhappy family is unhappy in its own way.|Leo Tolstoy|writer|4
The die is cast.|Julius Caesar|leader|3
The Eagle has landed.|Neil Armstrong|scientist|3
Float like a butterfly, sting like a bee.|Muhammad Ali|athlete|2`,
    qs: [{ q: 'Who said: "{quote}"', a: 'who', group: 'kind' }]
  },
  {
    pack: 'his-inventions-years', cat: 'his', cols: ['thing', 'who', 'year', 'd', 'alt'],
    rows: `
the telephone|Alexander Graham Bell|1876|2|Bell
the phonograph|Thomas Edison|1877|3|Edison
a practical incandescent light bulb|Thomas Edison|1879|2|Edison
dynamite|Alfred Nobel|1867|3|Nobel
the first working television|John Logie Baird|1926|4|Baird
the World Wide Web|Tim Berners-Lee|1989|3|Berners-Lee
the polio vaccine|Jonas Salk|1955|3|Salk
X-rays|Wilhelm Röntgen|1895|4|Röntgen;Roentgen
the periodic table|Dmitri Mendeleev|1869|3|Mendeleev
riveted blue jeans|Levi Strauss and Jacob Davis|1873|3|Levi Strauss
the modern zipper|Gideon Sundback|1913|5|Sundback
Velcro|George de Mestral|1955|4|de Mestral
the microwave oven|Percy Spencer|1945|4|Spencer
the petrol-powered car|Karl Benz|1886|3|Benz
the diesel engine|Rudolf Diesel|1893|2|Diesel
basketball|James Naismith|1891|3|Naismith
volleyball|William G. Morgan|1895|5|William Morgan;Morgan
the lightning rod|Benjamin Franklin|1752|3|Franklin
the cotton gin|Eli Whitney|1793|4|Whitney
the mercury thermometer|Daniel Gabriel Fahrenheit|1714|4|Fahrenheit
Braille writing|Louis Braille|1824|2|Braille
the daguerreotype photograph|Louis Daguerre|1839|4|Daguerre
the Polaroid instant camera|Edwin Land|1948|4|Land
the laser|Theodore Maiman|1960|5|Maiman
the computer mouse|Douglas Engelbart|1964|4|Engelbart
the ballpoint pen|László Bíró|1938|3|Biro;Bíró;Laszlo Biro
the crossword puzzle|Arthur Wynne|1913|4|Wynne
Kevlar|Stephanie Kwolek|1965|4|Kwolek
the stethoscope|René Laennec|1816|4|Laennec
the revolver|Samuel Colt|1836|3|Colt
the Morse code telegraph|Samuel Morse|1837|3|Morse
pasteurization|Louis Pasteur|1864|2|Pasteur
the barometer|Evangelista Torricelli|1643|4|Torricelli`,
    qs: [
      { q: 'Who invented {thing}?', a: 'who', alt: 'alt' },
      { q: 'Around which year was {thing} invented?', a: 'year', years: true, dAdd: 1 }
    ]
  },
  {
    pack: 'his-empire-capitals', cat: 'his', cols: ['empire', 'capital', 'd', 'alt'],
    rows: `
the Roman Empire|Rome|1
the Byzantine Empire|Constantinople|3|Istanbul
the Ottoman Empire|Constantinople|3|Istanbul
the Aztec Empire|Tenochtitlan|3
the Inca Empire|Cusco|3|Cuzco
the Mongol Empire|Karakorum|5
the Khmer Empire|Angkor|4
the Assyrian Empire|Nineveh|5
the Babylonian Empire|Babylon|3
ancient Carthage|Carthage|3
the Russian Empire|Saint Petersburg|3|St. Petersburg;Petrograd
the Austro-Hungarian Empire|Vienna|3
Egypt's Old Kingdom|Memphis|4`,
    qs: [{ q: 'What was the capital of {empire}?', a: 'capital', alt: 'alt' }]
  },
  {
    pack: 'his-monarchs', cat: 'his', cols: ['king', 'next', 'd', 'i'],
    rows: `
Henry VII|Henry VIII|3|1
Henry VIII|Edward VI|4|2
Mary I|Elizabeth I|3|3
Elizabeth I|James I|3|4
James I|Charles I|4|5
Charles II|James II|5|6
Anne|George I|5|7
George II|George III|5|8
George III|George IV|4|9
William IV|Victoria|3|10
Victoria|Edward VII|3|11
Edward VII|George V|4|12
George V|Edward VIII|4|13
Edward VIII|George VI|3|14
George VI|Elizabeth II|2|15
Elizabeth II|Charles III|1`,
    qs: [{ q: 'Who succeeded {king} on the English (later British) throne?', a: 'next', near: 'i' }]
  },
  {
    pack: 'his-event-years', cat: 'his', cols: ['q', 'year', 'd'],
    rows: `
In which year is the Western Roman Empire traditionally said to have fallen?|476|4
In which year did the Black Death reach Europe?|1347|5
In which year was the Gunpowder Plot to blow up the English Parliament?|1605|4
In which year did England and Scotland unite to form Great Britain?|1707|4
In which year was Napoleon crowned Emperor of the French?|1804|4
In which year did Britain pass the act abolishing slavery in most of its empire?|1833|5
In which year did the Irish Potato Famine begin?|1845|4
In which year did Karl Marx and Friedrich Engels publish "The Communist Manifesto"?|1848|4
In which year was Germany unified as an empire?|1871|4
In which year was the Eiffel Tower completed?|1889|3
In which year did the Russian Revolution take place?|1917|2
In which year was the United Nations founded?|1945|3
In which year was NATO founded?|1949|4
In which year was the State of Israel founded?|1948|3
In which year was the People's Republic of China proclaimed?|1949|3
In which year was Queen Elizabeth II crowned?|1953|3
In which year was Martin Luther King Jr. assassinated?|1968|3
In which year did Saigon fall, ending the Vietnam War?|1975|3
In which year was Nelson Mandela released from prison?|1990|3
In which year did Princess Diana die?|1997|2
In which year did euro coins and notes come into use?|2002|3
In which year did the Indian Ocean tsunami strike, on Boxing Day?|2004|3
In which year was Barack Obama first elected US President?|2008|2
In which year did the UK vote to leave the European Union?|2016|2
In which year did Notre-Dame Cathedral in Paris catch fire?|2019|2
In which year did Queen Elizabeth II die?|2022|1
In which year did the Titanic's sister ship Britannic sink?|1916|5
In which year did the Wright brothers make the first powered flight?|1903|2
In which year did Hillary and Tenzing first climb Everest?|1953|3
In which year did Yuri Gagarin become the first person in space?|1961|2`,
    qs: [{ q: '{q}', a: 'year', years: true }]
  }
];
