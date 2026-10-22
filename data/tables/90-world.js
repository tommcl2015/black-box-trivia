// World culture tables: people, food, sport events, brands, festivals, animals.
module.exports = [
  {
    pack: 'his-people-country', cat: 'his', cols: ['who', 'what', 'country', 'reg', 'd'],
    rows: `
Wolfgang Amadeus Mozart|the composer|Austria|eu|2
Ludwig van Beethoven|the composer|Germany|eu|2
Frédéric Chopin|the composer|Poland|eu|3
Pyotr Ilyich Tchaikovsky|the composer|Russia|eu|2
Antonio Vivaldi|the composer|Italy|eu|3
Jean Sibelius|the composer|Finland|eu|4
Edvard Grieg|the composer|Norway|eu|4
Antonín Dvořák|the composer|Czechia|eu|4
Giuseppe Verdi|the opera composer|Italy|eu|3
Vincent van Gogh|the painter|the Netherlands|eu|2
Rembrandt|the painter|the Netherlands|eu|3
Pablo Picasso|the painter|Spain|eu|2
Salvador Dalí|the painter|Spain|eu|2
Frida Kahlo|the painter|Mexico|am|2
Edvard Munch|the painter of The Scream|Norway|eu|3
Gustav Klimt|the painter of The Kiss|Austria|eu|3
René Magritte|the surrealist painter|Belgium|eu|4
Katsushika Hokusai|the artist of The Great Wave|Japan|as|3
Hans Christian Andersen|the fairy-tale writer|Denmark|eu|2
Astrid Lindgren|the author of Pippi Longstocking|Sweden|eu|3
Gabriel García Márquez|the novelist|Colombia|am|3
Miguel de Cervantes|the author of Don Quixote|Spain|eu|2
Leo Tolstoy|the novelist|Russia|eu|2
Rabindranath Tagore|the poet and first non-European Nobel literature winner|India|as|4
Pablo Neruda|the poet|Chile|am|3
Chinua Achebe|the author of Things Fall Apart|Nigeria|af|3
Haruki Murakami|the novelist|Japan|as|3
Paulo Coelho|the author of The Alchemist|Brazil|am|3
Jorge Luis Borges|the writer|Argentina|am|4
Henrik Ibsen|the playwright|Norway|eu|4
Marie Curie|the scientist (by birth)|Poland|eu|3
Alfred Nobel|the inventor of dynamite|Sweden|eu|2
Galileo Galilei|the astronomer|Italy|eu|2
Nicolaus Copernicus|the astronomer|Poland|eu|3
Tycho Brahe|the astronomer|Denmark|eu|4
Louis Pasteur|the scientist|France|eu|3
Carl Linnaeus|the botanist who named species|Sweden|eu|4
Confucius|the philosopher|China|as|2
Che Guevara|the revolutionary (by birth)|Argentina|am|3
Simón Bolívar|the liberator|Venezuela|am|3
Nelson Mandela|the president|South Africa|af|1
Kofi Annan|the UN secretary-general|Ghana|af|4
Wangari Maathai|the environmentalist and Nobel Peace laureate|Kenya|af|4
Malala Yousafzai|the education activist|Pakistan|as|2
Mahatma Gandhi|the independence leader|India|as|1
Genghis Khan|the conqueror|Mongolia|as|2
Roald Amundsen|the polar explorer|Norway|eu|3
Vasco da Gama|the explorer|Portugal|eu|3
Marco Polo|the traveller|Italy|eu|2
Ibn Battuta|the traveller|Morocco|af|4
Edmund Hillary|the mountaineer|New Zealand|oc|3
Yuri Gagarin|the Soviet cosmonaut|Russia|eu|2
Usain Bolt|the sprinter|Jamaica|am|1
Pelé|the footballer|Brazil|am|1
Diego Maradona|the footballer|Argentina|am|1
Johan Cruyff|the footballer|the Netherlands|eu|3
Zinedine Zidane|the footballer|France|eu|2
Mohamed Salah|the footballer|Egypt|af|2
Didier Drogba|the footballer|Ivory Coast|af|3
Sachin Tendulkar|the cricketer|India|as|2
Roger Federer|the tennis player|Switzerland|eu|1
Rafael Nadal|the tennis player|Spain|eu|1
Novak Djokovic|the tennis player|Serbia|eu|2
Naomi Osaka|the tennis player|Japan|as|3
Eliud Kipchoge|the marathon runner|Kenya|af|3
Haile Gebrselassie|the distance runner|Ethiopia|af|4
Yao Ming|the basketball player|China|as|2
Dirk Nowitzki|the basketball player|Germany|eu|3
Nikola Jokić|the basketball player|Serbia|eu|3
Giannis Antetokounmpo|the basketball player|Greece|eu|3
Wayne Gretzky|the hockey player|Canada|am|2
Ayrton Senna|the racing driver|Brazil|am|2
Michael Schumacher|the racing driver|Germany|eu|2
Max Verstappen|the racing driver|the Netherlands|eu|2
Shakira|the singer|Colombia|am|1
Björk|the singer|Iceland|eu|3
Rihanna|the singer|Barbados|am|2
Bob Marley|the reggae singer|Jamaica|am|1
ABBA|the pop group|Sweden|eu|1
U2|the rock band|Ireland|eu|2
AC/DC|the rock band|Australia|oc|2
BTS|the boy band|South Korea|as|1
Celine Dion|the singer|Canada|am|2
Fela Kuti|the Afrobeat pioneer|Nigeria|af|4
Burna Boy|the Afrobeats singer|Nigeria|af|3
Bad Bunny|the rapper and singer|Puerto Rico|am|3
Akira Kurosawa|the film director|Japan|as|3
Hayao Miyazaki|the animator|Japan|as|2
Ingmar Bergman|the film director|Sweden|eu|4
Federico Fellini|the film director|Italy|eu|4
Pedro Almodóvar|the film director|Spain|eu|4
Bong Joon-ho|the director of Parasite|South Korea|as|3
Shah Rukh Khan|the Bollywood star|India|as|2
Penélope Cruz|the actress|Spain|eu|3
Nicole Kidman|the actress|Australia|oc|2
Hugh Jackman|the actor|Australia|oc|2
Ryan Gosling|the actor|Canada|am|2
Liam Neeson|the actor|Northern Ireland (UK)|eu|4
Arnold Schwarzenegger|the actor and bodybuilder|Austria|eu|2
Jean-Claude Van Damme|the action star|Belgium|eu|3
Mr. Bean actor Rowan Atkinson|the comedian|England|eu|2
Ikea founder Ingvar Kamprad|the businessman|Sweden|eu|3
Lego founder Ole Kirk Christiansen|the toymaker|Denmark|eu|3`,
    qs: [{ q: 'Which country is {who}, {what}, from?', a: 'country', group: 'reg', unique: true }]
  },
  {
    pack: 'spo-olympic-hosts', cat: 'spo', cols: ['year', 'season', 'city', 'd'],
    rows: `
1896|Summer|Athens|3
1900|Summer|Paris|4
1908|Summer|London|4
1912|Summer|Stockholm|4
1920|Summer|Antwerp|5
1924|Summer|Paris|4
1928|Summer|Amsterdam|4
1932|Summer|Los Angeles|4
1936|Summer|Berlin|2
1948|Summer|London|3
1952|Summer|Helsinki|4
1956|Summer|Melbourne|4
1960|Summer|Rome|3
1964|Summer|Tokyo|3
1968|Summer|Mexico City|3
1972|Summer|Munich|3
1976|Summer|Montreal|3
1980|Summer|Moscow|3
1984|Summer|Los Angeles|3
1988|Summer|Seoul|3
1992|Summer|Barcelona|2
1996|Summer|Atlanta|2
2000|Summer|Sydney|2
2004|Summer|Athens|2
2008|Summer|Beijing|1
2012|Summer|London|1
2016|Summer|Rio de Janeiro|1
2021 (postponed 2020)|Summer|Tokyo|2
2024|Summer|Paris|1
1924|Winter|Chamonix|5
1928|Winter|St. Moritz|5
1936|Winter|Garmisch-Partenkirchen|5
1952|Winter|Oslo|4
1960|Winter|Squaw Valley|5
1964|Winter|Innsbruck|4
1968|Winter|Grenoble|4
1972|Winter|Sapporo|4
1976|Winter|Innsbruck|4
1980|Winter|Lake Placid|3
1984|Winter|Sarajevo|3
1988|Winter|Calgary|3
1992|Winter|Albertville|4
1994|Winter|Lillehammer|3
1998|Winter|Nagano|3
2002|Winter|Salt Lake City|3
2006|Winter|Turin|3
2010|Winter|Vancouver|2
2014|Winter|Sochi|2
2018|Winter|Pyeongchang|2
2022|Winter|Beijing|2
2026|Winter|Milan and Cortina d'Ampezzo|2`,
    qs: [{ q: 'Which city hosted the {year} {season} Olympics?', a: 'city', group: 'season', near: 'year' }]
  },
  {
    pack: 'spo-world-cups', cat: 'spo', cols: ['year', 'host', 'winner', 'd'],
    rows: `
1930|Uruguay|Uruguay|3
1934|Italy|Italy|4
1938|France|Italy|4
1950|Brazil|Uruguay|3
1954|Switzerland|West Germany|4
1958|Sweden|Brazil|3
1962|Chile|Brazil|4
1966|England|England|2
1970|Mexico|Brazil|3
1974|West Germany|West Germany|3
1978|Argentina|Argentina|3
1982|Spain|Italy|3
1986|Mexico|Argentina|2
1990|Italy|West Germany|3
1994|the United States|Brazil|2
1998|France|France|2
2002|South Korea and Japan|Brazil|2
2006|Germany|Italy|2
2010|South Africa|Spain|2
2014|Brazil|Germany|2
2018|Russia|France|2
2022|Qatar|Argentina|1`,
    qs: [
      { q: 'Which country won the {year} FIFA World Cup?', a: 'winner', near: 'year' },
      { q: 'Which country hosted the {year} FIFA World Cup?', a: 'host', near: 'year', dAdd: 1 }
    ]
  },
  {
    pack: 'spo-other-world-cups', cat: 'spo', cols: ['event', 'year', 'winner', 'kind', 'd'],
    rows: `
Rugby World Cup|1987|New Zealand|rugby|4
Rugby World Cup|1991|Australia|rugby|4
Rugby World Cup|1995|South Africa|rugby|3
Rugby World Cup|1999|Australia|rugby|4
Rugby World Cup|2003|England|rugby|3
Rugby World Cup|2007|South Africa|rugby|4
Rugby World Cup|2011|New Zealand|rugby|3
Rugby World Cup|2015|New Zealand|rugby|3
Rugby World Cup|2019|South Africa|rugby|3
Rugby World Cup|2023|South Africa|rugby|2
Cricket World Cup|1975|West Indies|cricket|4
Cricket World Cup|1983|India|cricket|3
Cricket World Cup|1992|Pakistan|cricket|3
Cricket World Cup|1996|Sri Lanka|cricket|3
Cricket World Cup|2011|India|cricket|3
Cricket World Cup|2019|England|cricket|3
Cricket World Cup|2023|Australia|cricket|3
FIFA Women's World Cup|1991|the United States|wfoot|4
FIFA Women's World Cup|2003|Germany|wfoot|4
FIFA Women's World Cup|2011|Japan|wfoot|3
FIFA Women's World Cup|2015|the United States|wfoot|3
FIFA Women's World Cup|2019|the United States|wfoot|3
FIFA Women's World Cup|2023|Spain|wfoot|2
UEFA European Championship (Euro)|1992|Denmark|euro|4
UEFA European Championship (Euro)|2004|Greece|euro|3
UEFA European Championship (Euro)|2016|Portugal|euro|3
UEFA European Championship (Euro 2020)|2021|Italy|euro|3
UEFA European Championship (Euro)|2024|Spain|euro|2
Copa América|2021|Argentina|copa|3
Copa America|2024|Argentina|copa|3
Africa Cup of Nations|2019|Algeria|afcon|4
Africa Cup of Nations|2023 (played 2024)|Ivory Coast|afcon|4`,
    qs: [{ q: 'Who won the {year} {event}?', a: 'winner', group: 'kind' }]
  },
  {
    pack: 'spo-football-clubs', cat: 'spo', cols: ['club', 'city', 'country', 'd'],
    rows: `
Real Madrid|Madrid|Spain|1
FC Barcelona|Barcelona|Spain|1
Atlético Madrid|Madrid|Spain|2
Sevilla|Seville|Spain|3
Bayern Munich|Munich|Germany|1
Borussia Dortmund|Dortmund|Germany|2
Juventus|Turin|Italy|2
AC Milan|Milan|Italy|1
Inter Milan|Milan|Italy|2
AS Roma|Rome|Italy|2
Napoli|Naples|Italy|2
Paris Saint-Germain|Paris|France|1
Olympique de Marseille|Marseille|France|3
Olympique Lyonnais|Lyon|France|3
Ajax|Amsterdam|the Netherlands|2
PSV|Eindhoven|the Netherlands|3
Feyenoord|Rotterdam|the Netherlands|3
Benfica|Lisbon|Portugal|3
FC Porto|Porto|Portugal|2
Sporting CP|Lisbon|Portugal|3
Celtic|Glasgow|Scotland|2
Rangers|Glasgow|Scotland|3
Galatasaray|Istanbul|Turkey|3
Fenerbahçe|Istanbul|Turkey|3
Boca Juniors|Buenos Aires|Argentina|2
River Plate|Buenos Aires|Argentina|3
Flamengo|Rio de Janeiro|Brazil|3
Santos|Santos|Brazil|4
Al Ahly|Cairo|Egypt|4
Liverpool|Liverpool|England|1
Everton|Liverpool|England|3
Manchester United|Manchester|England|1
Manchester City|Manchester|England|1
Arsenal|London|England|1
Chelsea|London|England|1
Tottenham Hotspur|London|England|2
Aston Villa|Birmingham|England|3
Newcastle United|Newcastle|England|2
Anderlecht|Brussels|Belgium|4
Red Bull Salzburg|Salzburg|Austria|4
Dinamo Zagreb|Zagreb|Croatia|4
Olympiacos|Piraeus|Greece|4
Inter Miami|Miami|the United States|2
LA Galaxy|Los Angeles|the United States|3
Al Nassr|Riyadh|Saudi Arabia|3`,
    qs: [
      { q: 'Which city is the football club {club} based in?', a: 'city', group: 'country' },
      { q: 'Which country does the football club {club} play in?', a: 'country', dAdd: -1 }
    ]
  },
  {
    pack: 'ent-car-brands', cat: 'ent', cols: ['brand', 'country', 'd'],
    rows: `
Toyota|Japan|1
Honda|Japan|1
Nissan|Japan|1
Mazda|Japan|2
Subaru|Japan|2
Mitsubishi|Japan|2
Suzuki|Japan|2
Lexus|Japan|2
Hyundai|South Korea|1
Kia|South Korea|2
Volkswagen|Germany|1
BMW|Germany|1
Mercedes-Benz|Germany|1
Audi|Germany|1
Porsche|Germany|1
Opel|Germany|3
Ferrari|Italy|1
Lamborghini|Italy|1
Fiat|Italy|1
Maserati|Italy|2
Alfa Romeo|Italy|2
Bugatti|France|3
Peugeot|France|2
Renault|France|2
Citroën|France|2
Volvo|Sweden|2
Saab|Sweden|2
Koenigsegg|Sweden|4
Škoda|Czechia|3
SEAT|Spain|3
Rolls-Royce|the United Kingdom|2
Bentley|the United Kingdom|2
Aston Martin|the United Kingdom|2
Jaguar|the United Kingdom|2
Land Rover|the United Kingdom|2
Mini|the United Kingdom|2
McLaren|the United Kingdom|2
Lotus|the United Kingdom|3
Ford|the United States|1
Chevrolet|the United States|1
Tesla|the United States|1
Cadillac|the United States|2
Jeep|the United States|2
Dodge|the United States|2
BYD|China|3
Geely|China|4
Tata Motors|India|3
Lada|Russia|3
Dacia|Romania|4
Holden|Australia|4`,
    qs: [{ q: 'Which country does the car brand {brand} come from?', a: 'country', dAdd: 0 }]
  },
  {
    pack: 'geo-national-dishes', cat: 'geo', cols: ['dish', 'country', 'cont', 'd'],
    rows: `
Paella|Spain|eu|1
Gazpacho|Spain|eu|2
Moussaka|Greece|eu|2
Goulash|Hungary|eu|2
Pierogi|Poland|eu|2
Borscht|Ukraine|eu|3
Haggis|Scotland|eu|1
Fondue|Switzerland|eu|2
Rösti|Switzerland|eu|3
Smørrebrød|Denmark|eu|4
Wiener Schnitzel|Austria|eu|2
Bratwurst|Germany|eu|2
Croissant|France|eu|1
Ratatouille|France|eu|1
Risotto|Italy|eu|1
Pastel de nata|Portugal|eu|2
Stroopwafel|the Netherlands|eu|2
Irish stew|Ireland|eu|1
Sushi|Japan|as|1
Ramen|Japan|as|1
Kimchi|South Korea|as|1
Bibimbap|South Korea|as|2
Pad thai|Thailand|as|1
Tom yum|Thailand|as|2
Pho|Vietnam|as|1
Banh mi|Vietnam|as|2
Peking duck|China|as|1
Dim sum|China|as|2
Biryani|India|as|2
Butter chicken|India|as|1
Nasi goreng|Indonesia|as|2
Rendang|Indonesia|as|3
Adobo|the Philippines|as|3
Laksa|Malaysia|as|3
Kebab (döner)|Turkey|as|2
Baklava|Turkey|as|2
Falafel|Egypt|af|3
Tagine|Morocco|af|2
Couscous|Morocco|af|2
Jollof rice|Nigeria|af|3
Bobotie|South Africa|af|4
Injera|Ethiopia|af|3
Tacos|Mexico|am|1
Mole|Mexico|am|3
Ceviche|Peru|am|2
Feijoada|Brazil|am|3
Empanadas and asado|Argentina|am|3
Arepas|Venezuela|am|3
Poutine|Canada|am|1
Jerk chicken|Jamaica|am|2
Meat pie and Vegemite toast|Australia|oc|2`,
    qs: [{ q: 'Which country is the dish "{dish}" most associated with?', a: 'country', group: 'cont' }]
  },
  {
    pack: 'geo-cheese-drink', cat: 'geo', cols: ['thing', 'kind', 'country', 'd'],
    rows: `
Parmesan|cheese|Italy|1
Mozzarella|cheese|Italy|1
Gorgonzola|cheese|Italy|2
Brie|cheese|France|1
Camembert|cheese|France|2
Roquefort|cheese|France|3
Gouda|cheese|the Netherlands|1
Edam|cheese|the Netherlands|2
Emmental|cheese|Switzerland|2
Gruyère|cheese|Switzerland|3
Feta|cheese|Greece|1
Halloumi|cheese|Cyprus|3
Manchego|cheese|Spain|3
Cheddar|cheese|England|1
Stilton|cheese|England|3
Paneer|cheese|India|3
Tequila|drink|Mexico|1
Sake|drink|Japan|1
Soju|drink|South Korea|2
Ouzo|drink|Greece|2
Grappa|drink|Italy|3
Limoncello|drink|Italy|2
Sangria|drink|Spain|1
Port|drink|Portugal|2
Champagne|drink|France|1
Cognac|drink|France|2
Vodka (most famously)|drink|Russia|2
Cachaça|drink|Brazil|3
Guinness|drink|Ireland|1
Pilsner|drink|Czechia|3
Mate|drink|Argentina|3
Rooibos tea|drink|South Africa|3
Masala chai|drink|India|2`,
    qs: [{ q: 'Which country does {thing} ({kind}) come from?', a: 'country', group: 'kind' }]
  },
  {
    pack: 'sci-dog-breeds', cat: 'sci', cols: ['breed', 'country', 'd'],
    rows: `
Chihuahua|Mexico|1
Dalmatian|Croatia|3
Great Dane|Germany|3
German Shepherd|Germany|1
Dachshund|Germany|2
Rottweiler|Germany|2
Dobermann|Germany|3
Shih Tzu|China|3
Pekingese|China|2
Chow Chow|China|3
Akita|Japan|2
Shiba Inu|Japan|2
Siberian Husky|Russia|2
Samoyed|Russia|3
Afghan Hound|Afghanistan|2
Saint Bernard|Switzerland|2
Bernese Mountain Dog|Switzerland|3
Labrador Retriever|Canada|3
Newfoundland|Canada|2
Golden Retriever|the United Kingdom|3
Border Collie|the United Kingdom|3
Yorkshire Terrier|the United Kingdom|2
Bulldog|the United Kingdom|2
Beagle|the United Kingdom|3
Jack Russell Terrier|the United Kingdom|3
Irish Wolfhound|Ireland|1
Pomeranian|Germany|4
French Bulldog|France|2
Basenji|the Congo region|4
Rhodesian Ridgeback|Zimbabwe|4
Australian Cattle Dog|Australia|2
Pug|China|4
Maltese|Malta|2
Weimaraner|Germany|4
Great Pyrenees|France|3`,
    qs: [{ q: 'Which country does the {breed} dog breed come from?', a: 'country' }]
  },
  {
    pack: 'geo-festivals', cat: 'geo', cols: ['what', 'country', 'cont', 'd'],
    rows: `
the tomato-throwing festival La Tomatina|Spain|eu|2
the running of the bulls in Pamplona|Spain|eu|1
Oktoberfest|Germany|eu|1
King's Day, when everyone wears orange|the Netherlands|eu|2
the Venice Carnival with its masks|Italy|eu|1
Bastille Day on July 14|France|eu|2
Midsummer (Midsommar) maypole dancing|Sweden|eu|3
Hogmanay New Year celebrations|Scotland|eu|2
St Patrick's Day|Ireland|eu|1
the Day of the Dead (Día de Muertos)|Mexico|am|1
the Rio Carnival|Brazil|am|1
Holi, the festival of colours|India|as|1
Diwali, the festival of lights|India|as|1
cherry blossom viewing (hanami)|Japan|as|1
Songkran, the water-fight New Year|Thailand|as|2
Chuseok harvest festival|South Korea|as|3
the Harbin Ice and Snow Festival|China|as|3
Anzac Day|Australia|oc|3
Waitangi Day|New Zealand|oc|3
Thanksgiving in November|the United States|am|1
Canada Day on July 1|Canada|am|1
Inti Raymi, the Inca Festival of the Sun|Peru|am|4
Junkanoo street parade|the Bahamas|am|4
the Up Helly Aa Viking fire festival|Scotland|eu|5
Timkat (Epiphany) festival|Ethiopia|af|5
the Fes Festival of World Sacred Music|Morocco|af|5`,
    qs: [{ q: 'Which country is famous for {what}?', a: 'country', group: 'cont' }]
  },
  {
    pack: 'ent-airlines', cat: 'ent', cols: ['airline', 'country', 'd'],
    rows: `
Qantas|Australia|1
Air New Zealand|New Zealand|1
Lufthansa|Germany|1
KLM|the Netherlands|2
Iberia|Spain|2
Alitalia (now ITA Airways)|Italy|2
Aer Lingus|Ireland|2
Ryanair|Ireland|2
easyJet|the United Kingdom|2
Virgin Atlantic|the United Kingdom|2
British Airways|the United Kingdom|1
Air France|France|1
Swiss|Switzerland|2
Finnair|Finland|2
Icelandair|Iceland|2
Aeroflot|Russia|2
Turkish Airlines|Turkey|1
Emirates|the United Arab Emirates|1
Etihad|the United Arab Emirates|2
Qatar Airways|Qatar|1
El Al|Israel|2
Singapore Airlines|Singapore|1
Cathay Pacific|Hong Kong|2
Japan Airlines|Japan|1
ANA (All Nippon Airways)|Japan|2
Korean Air|South Korea|1
Thai Airways|Thailand|1
Garuda Indonesia|Indonesia|3
Air India|India|1
Ethiopian Airlines|Ethiopia|2
LATAM|Chile|3
Avianca|Colombia|3
Aeroméxico|Mexico|2
Delta|the United States|1
WestJet|Canada|2`,
    qs: [{ q: 'Which country is the airline {airline} based in?', a: 'country' }]
  },
  {
    pack: 'sci-national-animals', cat: 'sci', cols: ['country', 'animal', 'd', 'alt'],
    rows: `
Australia|Kangaroo|1
New Zealand|Kiwi|1|Kiwi bird
China|Giant panda|1|Panda
India|Bengal tiger|2|Tiger
Scotland|Unicorn|2
Wales|Red dragon|1|Dragon
England|Lion|2
the United States|Bald eagle|1|Eagle
Canada|Beaver|1
Mexico|Golden eagle|3|Eagle
Russia|Brown bear|2|Bear
France|Gallic rooster|2|Rooster;Cockerel
South Africa|Springbok|2
Peru|Vicuña|4|Vicuna
Bolivia|Llama|3
Thailand|Elephant|2
Indonesia|Komodo dragon|3
Madagascar|Ring-tailed lemur|2|Lemur
Bhutan|Takin|5
Belgium|Lion|4
Malaysia|Malayan tiger|3|Tiger
Pakistan|Markhor|5`,
    qs: [{ q: 'What is the national animal of {country}?', a: 'animal', alt: 'alt', unique: true }]
  },
  {
    pack: 'ent-eurovision', cat: 'ent', cols: ['year', 'country', 'song', 'd'],
    rows: `
1974|Sweden|Waterloo (ABBA)|2
1988|Switzerland|Ne partez pas sans moi (Celine Dion)|4
1994|Ireland|Rock 'n' Roll Kids|4
1997|the United Kingdom|Love Shine a Light (Katrina and the Waves)|4
2006|Finland|Hard Rock Hallelujah (Lordi)|3
2012|Sweden|Euphoria (Loreen)|3
2014|Austria|Rise Like a Phoenix (Conchita Wurst)|3
2016|Ukraine|1944 (Jamala)|4
2018|Israel|Toy (Netta)|4
2019|the Netherlands|Arcade (Duncan Laurence)|4
2021|Italy|Zitti e buoni (Måneskin)|3
2022|Ukraine|Stefania (Kalush Orchestra)|3
2023|Sweden|Tattoo (Loreen)|3
2024|Switzerland|The Code (Nemo)|3
2025|Austria|Wasted Love (JJ)|3
2026|Bulgaria|Bangaranga (Dara)|3`,
    qs: [{ q: 'Which country won Eurovision in {year} with "{song}"?', a: 'country' }]
  },
  {
    pack: 'ent-video-game-makers', cat: 'ent', cols: ['game', 'maker', 'd'],
    rows: `
Super Mario Bros.|Nintendo|1
The Legend of Zelda|Nintendo|1
Animal Crossing|Nintendo|2
Sonic the Hedgehog|Sega|1
Halo|Microsoft|2
Minecraft|Mojang|2
Fortnite|Epic Games|1
Grand Theft Auto|Rockstar Games|1
Red Dead Redemption|Rockstar Games|2
Pac-Man|Namco|2
Space Invaders|Taito|3
Street Fighter|Capcom|2
Resident Evil|Capcom|2
Final Fantasy|Square Enix|2
Metal Gear Solid|Konami|3
Call of Duty|Activision|2
World of Warcraft|Blizzard|2
The Sims|Maxis|2
FIFA / EA Sports FC|EA Sports|1
Angry Birds|Rovio|2
Candy Crush Saga|King|3
Clash of Clans|Supercell|3
The Witcher 3|CD Projekt Red|3
Elden Ring|FromSoftware|3
Uncharted|Naughty Dog|3
The Last of Us|Naughty Dog|3
God of War|Santa Monica Studio|4
Roblox|Roblox Corporation|2
Among Us|Innersloth|4
League of Legends|Riot Games|3
Valorant|Riot Games|3
Half-Life|Valve|3
Portal|Valve|3
Crash Bandicoot (original)|Naughty Dog|4
Donkey Kong (original)|Nintendo|2
Kirby|Nintendo|2
Genshin Impact|miHoYo (HoYoverse)|4
Assassin's Creed|Ubisoft|2
Rayman|Ubisoft|3`,
    qs: [{ q: 'Which company made the video game {game}?', a: 'maker' }]
  },
  {
    pack: 'art-shakespeare-settings', cat: 'art', cols: ['play', 'setting', 'd'],
    rows: `
Romeo and Juliet|Verona|1
Hamlet|Denmark|1
Macbeth|Scotland|1
Othello|Venice and Cyprus|3
The Merchant of Venice|Venice|1
Julius Caesar|Rome|1
Antony and Cleopatra|Egypt and Rome|2
Much Ado About Nothing|Messina, Sicily|4
A Midsummer Night's Dream|Athens|3
The Two Gentlemen of Verona|Verona and Milan|2
Timon of Athens|Athens|2
King Lear|Britain|3
The Winter's Tale|Sicily and Bohemia|4
Twelfth Night|Illyria|4
Pericles|Tyre|5`,
    qs: [{ q: 'Where is Shakespeare\'s {play} mainly set?', a: 'setting' }]
  },
  {
    pack: 'sci-moons', cat: 'sci', cols: ['moon', 'planet', 'd'],
    rows: `
Phobos|Mars|3
Deimos|Mars|3
Io|Jupiter|3
Europa|Jupiter|3
Ganymede|Jupiter|3
Callisto|Jupiter|4
Titan|Saturn|2
Enceladus|Saturn|4
Mimas|Saturn|4
Rhea|Saturn|5
Titania|Uranus|4
Miranda|Uranus|4
Oberon|Uranus|4
Triton|Neptune|3
Charon|Pluto|3`,
    qs: [{ q: '{moon} is a moon of which world?', a: 'planet' }]
  },
  {
    pack: 'ent-anime', cat: 'ent', cols: ['what', 'title', 'd'],
    rows: `
features Goku and the hunt for seven magical orbs|Dragon Ball|2
follows a boy made of rubber who wants to be King of the Pirates|One Piece|2
follows a young ninja named Naruto Uzumaki|Naruto|1
features humanity behind giant walls fighting Titans|Attack on Titan|2
has a student who finds a notebook that kills anyone whose name is written in it|Death Note|2
features Tanjiro, who fights demons after his sister becomes one|Demon Slayer|2
features magical girl Usagi Tsukino|Sailor Moon|2
is a Studio Ghibli film about a girl who works in a spirit bathhouse|Spirited Away|2
is a Studio Ghibli film with a big grey forest spirit and a Catbus|My Neighbor Totoro|2
is a Studio Ghibli film about a young witch who runs a delivery service|Kiki's Delivery Service|3
is a Studio Ghibli film about a castle that walks on legs|Howl's Moving Castle|2
is a Studio Ghibli film about a forest war between humans and animal gods|Princess Mononoke|3
features a pocket-sized cat robot from the future|Doraemon|3
features students who train to be heroes with superpowers called "quirks"|My Hero Academia|3
features two brothers who use alchemy to try to restore their bodies|Fullmetal Alchemist|3
is a 1988 cyberpunk film set in Neo-Tokyo|Akira|3
is a 2016 film about two teenagers who swap bodies|Your Name|3
features a boy named Yuji who swallows a cursed finger|Jujutsu Kaisen|3
features a chainsaw-powered devil hunter named Denji|Chainsaw Man|4
features a spy, an assassin and a mind-reading girl who form a fake family|Spy × Family|3`,
    qs: [{ q: 'Which anime {what}?', a: 'title' }]
  },
  {
    pack: 'ent-kpop-bollywood', cat: 'ent', cols: ['qw', 'what', 'answer', 't', 'd'],
    rows: `
Who|had the 2012 viral hit "Gangnam Style"|PSY|p|1
Which group|had a hit with "Dynamite" in 2020|BTS|g|2
Which group|features Jennie, Lisa, Jisoo and Rosé|Blackpink|g|1
Who|had a 2024 global hit "APT." with Bruno Mars|Rosé|p|2
Which K-pop group|had the hits "Fancy" and "TT"|Twice|g|4
Which K-pop group|had the hit "God's Menu"|Stray Kids|g|4
Which K-pop group|is known for "Super Shy" and "Hype Boy"|NewJeans|g|4
Which film|is the 2025 animated hit about a K-pop girl group who fight demons|KPop Demon Hunters|f|2
Which fictional girl group|stars in KPop Demon Hunters|Huntr/x|g|3
Which film|is the 2022 Indian blockbuster whose song "Naatu Naatu" won an Oscar|RRR|f|3
Which film|is the 2008 Oscar winner about a Mumbai teenager on a quiz show|Slumdog Millionaire|f|2
Which film|is the 2009 Bollywood comedy about three engineering students|3 Idiots|f|4
Which film|is the 2001 Bollywood epic about cricket under British rule|Lagaan|f|4
Who|is the Bollywood star known as "King Khan"|Shah Rukh Khan|p|2
Who|is the Bollywood legend known as "Big B"|Amitabh Bachchan|p|3
Who|is the former Miss World who starred in Devdas|Aishwarya Rai|p|3
Who|is the Indian actress who starred in the US series Quantico|Priyanka Chopra|p|3`,
    qs: [{ q: '{qw} {what}?', a: 'answer', group: 't' }]
  }
];
