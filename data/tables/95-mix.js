// Mixed world tables: words, web domains, films, fictional places, sports terms, music, drinks, nature.
module.exports = [
  {
    pack: 'art-hello-thanks', cat: 'art', cols: ['kind', 'word', 'lang', 'd'],
    rows: `
thank you|Merci|French|1
thank you|Danke|German|1
thank you|Gracias|Spanish|1
thank you|Grazie|Italian|1
thank you|Obrigado|Portuguese|2
thank you|Arigatō|Japanese|1
thank you|Xièxiè|Mandarin Chinese|2
thank you|Kamsahamnida|Korean|3
thank you|Spasibo|Russian|2
thank you|Dziękuję|Polish|3
thank you|Tack|Swedish|3
thank you|Takk|Norwegian|4
thank you|Dank je|Dutch|3
thank you|Efcharistó|Greek|3
thank you|Teşekkürler|Turkish|3
thank you|Shukran|Arabic|2
thank you|Toda|Hebrew|3
thank you|Dhanyavaad|Hindi|3
thank you|Asante|Swahili|3
thank you|Kiitos|Finnish|4
thank you|Mahalo|Hawaiian|3
thank you|Khop khun|Thai|4
thank you|Cảm ơn|Vietnamese|4
thank you|Terima kasih|Indonesian (Malay)|4
thank you|Diolch|Welsh|5
thank you|Go raibh maith agat|Irish|4
hello|Bonjour|French|1
hello|Hola|Spanish|1
hello|Ciao|Italian|1
hello|Konnichiwa|Japanese|1
hello|Annyeonghaseyo|Korean|3
hello|Nǐ hǎo|Mandarin Chinese|1
hello|Namaste|Hindi|2
hello|Shalom|Hebrew|2
hello|Jambo|Swahili|3
hello|Aloha|Hawaiian|1
hello|Kia ora|Māori|3
hello|Sawasdee|Thai|4
hello|Xin chào|Vietnamese|4
hello|Merhaba|Turkish|3
hello|Privet|Russian|3
hello|Yassou|Greek|3
hello|Olá|Portuguese|2
hello|Sannu|Hausa|5
hello|Sawubona|Zulu|4
hello|Dia dhuit|Irish|4`,
    qs: [{ q: 'In which language is "{word}" a way to say "{kind}"?', a: 'lang', group: 'kind' }]
  },
  {
    pack: 'geo-web-domains', cat: 'geo', cols: ['tld', 'country', 'd'],
    rows: `
.de|Germany|2
.fr|France|1
.es|Spain|2
.it|Italy|1
.nl|the Netherlands|2
.be|Belgium|3
.ch|Switzerland|3
.at|Austria|3
.se|Sweden|3
.no|Norway|3
.dk|Denmark|3
.fi|Finland|3
.pl|Poland|3
.ie|Ireland|2
.uk|the United Kingdom|1
.pt|Portugal|3
.gr|Greece|3
.ru|Russia|2
.ua|Ukraine|3
.tr|Turkey|3
.jp|Japan|1
.cn|China|1
.kr|South Korea|2
.in|India|1
.pk|Pakistan|3
.th|Thailand|3
.vn|Vietnam|3
.id|Indonesia|4
.ph|the Philippines|3
.au|Australia|1
.nz|New Zealand|2
.ca|Canada|1
.mx|Mexico|2
.br|Brazil|2
.ar|Argentina|3
.cl|Chile|3
.co|Colombia|3
.za|South Africa|3
.ng|Nigeria|3
.ke|Kenya|3
.eg|Egypt|3
.il|Israel|3
.tv|Tuvalu|4
.io|British Indian Ocean Territory|5
.ly|Libya|4
.me|Montenegro|4
.ai|Anguilla|5`,
    qs: [{ q: 'Which country or territory uses the internet domain "{tld}"?', a: 'country' }]
  },
  {
    pack: 'ent-animated-films', cat: 'ent', cols: ['who', 'film', 'studio', 'd'],
    rows: `
Woody and Buzz Lightyear|Toy Story|pixar|1
Lightning McQueen|Cars|pixar|1
Nemo and Dory|Finding Nemo|pixar|1
Mike Wazowski and Sulley|Monsters, Inc.|pixar|1
Remy the rat chef|Ratatouille|pixar|1
WALL-E and EVE|WALL-E|pixar|1
Carl Fredricksen and his balloon house|Up|pixar|1
Joy, Sadness and Anger|Inside Out|pixar|1
Miguel and his great-great-grandfather in the Land of the Dead|Coco|pixar|2
Mr. Incredible and Elastigirl|The Incredibles|pixar|1
Merida the archer|Brave|pixar|2
Flik the ant|A Bug's Life|pixar|2
Joe Gardner, a jazz pianist|Soul|pixar|3
Luca and Alberto, sea monsters on the Italian Riviera|Luca|pixar|3
Mei, who turns into a giant red panda|Turning Red|pixar|3
Ember and Wade|Elemental|pixar|3
Arlo the dinosaur|The Good Dinosaur|pixar|4
Elsa and Anna|Frozen|disney|1
Moana and Maui|Moana|disney|1
Simba and Mufasa|The Lion King|disney|1
Ariel and Sebastian|The Little Mermaid|disney|1
Belle and the Beast|Beauty and the Beast|disney|1
Aladdin and the Genie|Aladdin|disney|1
Rapunzel and Flynn Rider|Tangled|disney|2
Mirabel Madrigal|Encanto|disney|2
Judy Hopps and Nick Wilde|Zootopia (Zootropolis)|disney|2
Baymax|Big Hero 6|disney|2
Ralph and Vanellope|Wreck-It Ralph|disney|2
Hua Mulan and Mushu|Mulan|disney|1
Quasimodo|The Hunchback of Notre Dame|disney|2
Tiana|The Princess and the Frog|disney|2
Stitch|Lilo & Stitch|disney|1
Shrek and Donkey|Shrek|other|1
Po the panda|Kung Fu Panda|other|1
Gru and the Minions|Despicable Me|other|1
Manny the mammoth and Sid the sloth|Ice Age|other|1
Hiccup and Toothless|How to Train Your Dragon|other|1
Miles Morales|Spider-Man: Into the Spider-Verse|other|2
Wallace and his dog Gromit|Wallace & Gromit|other|2
Alex the lion and Marty the zebra|Madagascar|other|2
Roz the robot|The Wild Robot|other|3
Rumi, Mira and Zoey|KPop Demon Hunters|other|3`,
    qs: [{ q: 'Which animated film features {who}?', a: 'film', group: 'studio' }]
  },
  {
    pack: 'ent-fictional-places', cat: 'ent', cols: ['place', 'work', 'kind', 'd'],
    rows: `
Hogwarts|Harry Potter|book|1
Narnia|The Chronicles of Narnia|book|1
Middle-earth|The Lord of the Rings|book|1
Westeros|Game of Thrones|tv|1
Wakanda|Black Panther|film|1
Gotham City|Batman|comic|1
Metropolis|Superman|comic|2
Springfield|The Simpsons|tv|1
Bikini Bottom|SpongeBob SquarePants|tv|1
Neverland|Peter Pan|book|1
the Emerald City|The Wizard of Oz|book|1
the Hundred Acre Wood|Winnie-the-Pooh|book|1
Hill Valley|Back to the Future|film|2
Hawkins, Indiana|Stranger Things|tv|2
Bedrock|The Flintstones|tv|2
Pawnee, Indiana|Parks and Recreation|tv|3
the Scranton branch of Dunder Mifflin|The Office (US)|tv|2
Central Perk|Friends|tv|1
Panem|The Hunger Games|book|2
Gilead|The Handmaid's Tale|book|3
Lilliput|Gulliver's Travels|book|2
Arrakis|Dune|book|2
Tatooine|Star Wars|film|1
Pandora|Avatar|film|2
Isla Nublar|Jurassic Park|film|2
Amity Island|Jaws|film|3
Castle Grayskull|He-Man and the Masters of the Universe|tv|3
Hyrule|The Legend of Zelda|game|2
the Mushroom Kingdom|Super Mario|game|1
Rapture, an undersea city|BioShock|game|4
Los Santos|Grand Theft Auto V|game|3
Pallet Town|Pokémon|game|3
Agrabah|Aladdin|film|2
Arendelle|Frozen|film|1
Sodor|Thomas the Tank Engine|tv|2
Whoville|How the Grinch Stole Christmas!|book|2
Riverdale|Archie Comics|comic|3
Sunnydale|Buffy the Vampire Slayer|tv|3
Wisteria Lane|Desperate Housewives|tv|3
Albert Square|EastEnders|tv|3
Ramsay Street|Neighbours|tv|3
Summer Bay|Home and Away|tv|4
Gondor and Mordor|The Lord of the Rings|book|2`,
    qs: [{ q: 'Which story or series is set in {place}?', a: 'work', group: 'kind', unique: true }]
  },
  {
    pack: 'spo-sport-terms', cat: 'spo', cols: ['term', 'sport', 'd'],
    rows: `
a "love" score and a "deuce"|Tennis|1
a "let" and a "double fault"|Tennis|1
a "birdie", "eagle" or "albatross"|Golf|1
a "bogey" and a "mulligan"|Golf|2
a "googly", "maiden over" and "silly mid-off"|Cricket|2
a "duck" for scoring zero and an "LBW"|Cricket|2
a "scrum", "try" and "line-out"|Rugby|1
a "conversion" kick worth two points after a try|Rugby|2
a "bicycle kick" and a "corner kick"|Football (soccer)|2
a "nutmeg" between the legs|Football (soccer)|2
a "slam dunk" and an "alley-oop"|Basketball|1
a "triple-double"|Basketball|2
a "touchdown" and a "field goal"|American football|1
a "Hail Mary" pass|American football|2
a "home run", "strike" and "bunt"|Baseball|1
a "grand slam" with the bases loaded|Baseball|2
a "power play", "icing" and "Zamboni"|Ice hockey|1
a "turkey" for three strikes in a row|Ten-pin bowling|2
a "spare" and a "gutter ball"|Ten-pin bowling|1
a "bullseye" and "double top"|Darts|1
a "180" maximum score|Darts|2
a "maximum 147" break|Snooker|2
a "snooker" and a "cannon"|Snooker|3
"en garde" and a "riposte"|Fencing|2
"ippon" and "waza-ari"|Judo|3
a "dig", "spike" and "set"|Volleyball|2
a "chukka" on horseback|Polo|3
"stones", "hammer" and "sweeping"|Curling|1
a "jack" being the target ball|Lawn bowls|3
a "clean and jerk" and a "snatch"|Weightlifting|2
a "pit stop" and "pole position"|Formula One|1
a "Fosbury flop"|High jump|3
"checkmate" and "castling"|Chess|1
a "shuttlecock"|Badminton|1
a "half-pipe" and a "kickflip"|Skateboarding|2
a "wipeout" and "hanging ten"|Surfing|2
a "knockout" and "uppercut"|Boxing|1
a "tumble turn"|Swimming|3
a "photo finish" and a "furlong"|Horse racing|2
a "yellow jersey"|Cycling (Tour de France)|2`,
    qs: [{ q: 'In which sport would you hear about {term}?', a: 'sport' }]
  },
  {
    pack: 'art-instrument-family', cat: 'art', cols: ['inst', 'fam', 'd'],
    rows: `
Violin|String|1
Viola|String|2
Cello|String|1
Double bass|String|2
Harp|String|1
Trumpet|Brass|1
Trombone|Brass|1
French horn|Brass|2
Tuba|Brass|1
Flute|Woodwind|1
Clarinet|Woodwind|1
Oboe|Woodwind|2
Bassoon|Woodwind|2
Saxophone (though made of brass)|Woodwind|3
Piccolo|Woodwind|2
Timpani|Percussion|2
Xylophone|Percussion|1
Snare drum|Percussion|1
Triangle|Percussion|1
Glockenspiel|Percussion|2
Cymbals|Percussion|1`,
    qs: [{ q: 'In an orchestra, which family does the {inst} belong to?', a: 'fam' }]
  },
  {
    pack: 'art-instrument-origin', cat: 'art', cols: ['inst', 'place', 'd'],
    rows: `
Sitar|India|2
Tabla|India|3
Didgeridoo|Australia|1
Bagpipes (most famously)|Scotland|1
Ukulele|Hawaii|2
Balalaika|Russia|2
Bouzouki|Greece|3
Steelpan (steel drum)|Trinidad and Tobago|2
Koto|Japan|3
Shamisen|Japan|4
Erhu|China|4
Gamelan orchestra|Indonesia|3
Kora|West Africa|4
Djembe|West Africa|3
Mbira (thumb piano)|Zimbabwe|4
Charango|the Andes|4
Alphorn|Switzerland|2
Banjo (modern form)|the United States|3
Hardanger fiddle|Norway|5`,
    qs: [{ q: 'Where does the {inst} come from?', a: 'place' }]
  },
  {
    pack: 'ent-cocktails', cat: 'ent', cols: ['drink', 'spirit', 'd'],
    rows: `
Mojito|Rum|1
Daiquiri|Rum|2
Piña colada|Rum|1
Mai tai|Rum|3
Margarita|Tequila|1
Paloma|Tequila|3
Tequila sunrise|Tequila|1
Martini (classic)|Gin|2
Negroni|Gin|2
Gin and tonic|Gin|1
Tom Collins|Gin|3
Moscow mule|Vodka|2
Bloody Mary|Vodka|1
Cosmopolitan|Vodka|2
White Russian|Vodka|2
Screwdriver|Vodka|2
Old fashioned|Whiskey|2
Manhattan|Whiskey|2
Irish coffee|Whiskey|1
Caipirinha|Cachaça|3
Pisco sour|Pisco|2
Sidecar|Cognac|4
Bellini|Prosecco and peach|3
Mimosa|Sparkling wine and orange juice|2`,
    qs: [{ q: 'What is the main alcohol in a {drink}?', a: 'spirit' }]
  },
  {
    pack: 'ent-slogans', cat: 'ent', cols: ['slogan', 'brand', 'd'],
    rows: `
Just Do It|Nike|1
Impossible Is Nothing|Adidas|2
I'm Lovin' It|McDonald's|1
Finger Lickin' Good|KFC|1
Think Different|Apple|2
Because You're Worth It|L'Oréal|2
The Ultimate Driving Machine|BMW|2
Vorsprung durch Technik|Audi|3
Gives You Wings|Red Bull|1
Every Little Helps|Tesco|3
Taste the Rainbow|Skittles|1
Melts in your mouth, not in your hand|M&M's|2
Snap! Crackle! Pop!|Rice Krispies|2
They're Gr-r-reat!|Frosted Flakes (Frosties)|2
Open Happiness|Coca-Cola|2
The Happiest Place on Earth|Disneyland|2
Broadcast Yourself|YouTube|3
Don't Leave Home Without It|American Express|3
Connecting People|Nokia|3
Eat Fresh|Subway|2
Have It Your Way|Burger King|2
Gotta Catch 'Em All|Pokémon|1
The Best a Man Can Get|Gillette|2
It's the Real Thing|Coca-Cola|3
Probably the best lager in the world|Carlsberg|2
Keeps going and going and going|Energizer|2
Should've gone to Specsavers|Specsavers|3
You're not you when you're hungry|Snickers|2`,
    qs: [{ q: 'Which brand used the slogan "{slogan}"?', a: 'brand' }]
  },
  {
    pack: 'his-invention-country', cat: 'his', cols: ['thing', 'country', 'd'],
    rows: `
paper|China|1
gunpowder|China|1
the magnetic compass|China|2
porcelain|China|2
paper money|China|3
silk|China|1
the printing press with movable metal type in Europe|Germany|2
the automobile (Benz Patent-Motorwagen)|Germany|2
the airplane (Wright brothers)|the United States|1
the World Wide Web (at CERN)|Switzerland|3
Velcro|Switzerland|3
the Rubik's Cube|Hungary|2
dynamite|Sweden|2
the Walkman|Japan|2
instant noodles|Japan|2
karaoke|Japan|2
the QR code|Japan|3
the steam locomotive|England|2
the hot air balloon (Montgolfier brothers)|France|2
the bikini|France|3
photography (first permanent photo)|France|3
the Braille alphabet|France|2
pizza|Italy|1
the electric battery (Volta)|Italy|3
LEGO bricks|Denmark|1
the Bluetooth standard (named after a Danish king)|Sweden|4
the cardiac pacemaker (first implanted)|Sweden|5
insulin treatment|Canada|3
the zero as a number|India|2
chess (earliest form)|India|2
the Bessemer process for steel|England|5
Skype (developed in Tallinn)|Estonia|3
the black box flight recorder|Australia|4
Wi-Fi's key patent|Australia|4
the boomerang|Australia|1`,
    qs: [{ q: 'Which country gave the world {thing}?', a: 'country' }]
  },
  {
    pack: 'geo-nature-country', cat: 'geo', cols: ['what', 'country', 'cont', 'd'],
    rows: `
Angel Falls, the world's tallest waterfall|Venezuela|am|2
Lake Baikal, the deepest lake|Russia|eu|2
Loch Ness|Scotland|eu|1
Lake Como|Italy|eu|2
Lake Bled|Slovenia|eu|4
Plitvice Lakes|Croatia|eu|3
Mount Fuji|Japan|as|1
Mount Etna|Italy|eu|2
Mount Vesuvius|Italy|eu|1
Eyjafjallajökull, the 2010 ash-cloud volcano|Iceland|eu|2
Krakatoa|Indonesia|as|3
Mount Pinatubo|the Philippines|as|4
Mount St. Helens|the United States|am|3
Popocatépetl|Mexico|am|4
Kilimanjaro|Tanzania|af|1
Mount Kenya|Kenya|af|1
Table Mountain|South Africa|af|2
the Serengeti|Tanzania|af|2
the Masai Mara|Kenya|af|3
the Okavango Delta|Botswana|af|4
Uluru (Ayers Rock)|Australia|oc|1
the Great Barrier Reef|Australia|oc|1
Milford Sound|New Zealand|oc|3
Ha Long Bay|Vietnam|as|2
the Cliffs of Moher|Ireland|eu|2
the Giant's Causeway|Northern Ireland (UK)|eu|3
the fjord Geirangerfjord|Norway|eu|3
the Galápagos Islands|Ecuador|am|2
Torres del Paine|Chile|am|3
Patagonia's Perito Moreno Glacier|Argentina|am|3
Banff National Park|Canada|am|2
the Grand Canyon|the United States|am|1
Yellowstone|the United States|am|1
Cappadocia's fairy chimneys|Turkey|as|3
Pamukkale's white terraces|Turkey|as|4
Zhangjiajie's pillar mountains|China|as|4
the Cotswolds|England|eu|3
the Black Forest|Germany|eu|2
the Dolomites|Italy|eu|3
Sossusvlei's red dunes|Namibia|af|4
the Avenue of the Baobabs|Madagascar|af|4
the Blue Lagoon|Iceland|eu|2`,
    qs: [{ q: 'Which country is home to {what}?', a: 'country', group: 'cont' }]
  },
  {
    pack: 'sci-space-missions', cat: 'sci', cols: ['what', 'answer', 'd'],
    rows: `
the first artificial satellite, launched in 1957|Sputnik 1|2
the first mission to land humans on the Moon|Apollo 11|1
the Apollo mission whose crew survived an oxygen-tank explosion in 1970|Apollo 13|2
the space telescope launched in 1990 that orbits Earth|Hubble|1
the infrared space telescope launched in 2021|James Webb|2
the probe that flew past Pluto in 2015|New Horizons|3
the probe that orbited Saturn and ended by diving into it in 2017|Cassini|3
the NASA rover that landed on Mars in 2021 with a small helicopter|Perseverance|2
the small helicopter that flew on Mars|Ingenuity|3
the NASA rover that landed on Mars in 2012|Curiosity|3
the first rover to drive on Mars, in 1997|Sojourner|4
the space station launched by the Soviet Union in 1986|Mir|3
the US space shuttle that broke up after launch in 1986|Challenger|3
the US space shuttle lost on re-entry in 2003|Columbia|4
the European probe that landed on a comet in 2014|Philae (Rosetta mission)|4
the Indian mission that landed near the Moon's south pole in 2023|Chandrayaan-3|3
the Chinese mission that brought back samples from the Moon's far side in 2024|Chang'e 6|4
the 2026 mission that flew four astronauts around the Moon|Artemis II|2
the first spacecraft to leave the solar system's heliosphere|Voyager 1|2
the SpaceX capsule that carries astronauts to the ISS|Crew Dragon|3
SpaceX's giant reusable rocket being tested in Texas|Starship|2
the dog launched into orbit in 1957|Laika|2`,
    qs: [{ q: 'What was or is {what}?', a: 'answer' }]
  }
];
