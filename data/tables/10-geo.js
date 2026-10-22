// World geography fact tables. Only well-established facts; contested or recently changed ones are left out.
module.exports = [
  {
    pack: 'geo-currency', cat: 'geo', cols: ['country', 'currency', 'cont', 'd', 'alt'],
    rows: `
Japan|Yen|Asia|1
China|Yuan|Asia|2|Renminbi
United Kingdom|Pound sterling|Europe|1|Pound
Russia|Ruble|Europe|2|Rouble
India|Rupee|Asia|2|Indian rupee
South Africa|Rand|Africa|2
Brazil|Real|Americas|3
Mexico|Peso|Americas|2
Switzerland|Franc|Europe|2|Swiss franc
South Korea|Won|Asia|3
Thailand|Baht|Asia|3
Vietnam|Dong|Asia|3
Indonesia|Rupiah|Asia|4
Malaysia|Ringgit|Asia|4
Philippines|Peso|Asia|4
Israel|Shekel|Asia|3|New shekel
Turkey|Lira|Europe|3|Turkish lira
Poland|Złoty|Europe|3|Zloty
Czech Republic|Koruna|Europe|4|Czech crown;Crown
Hungary|Forint|Europe|4
Sweden|Krona|Europe|3|Swedish krona
Norway|Krone|Europe|3|Norwegian krone
Denmark|Krone|Europe|3|Danish krone
Iceland|Króna|Europe|4|Krona
Saudi Arabia|Riyal|Asia|3
United Arab Emirates|Dirham|Asia|3
Morocco|Dirham|Africa|4
Egypt|Pound|Africa|3|Egyptian pound
Nigeria|Naira|Africa|3
Kenya|Shilling|Africa|4|Kenyan shilling
Ghana|Cedi|Africa|4
Ethiopia|Birr|Africa|4
Argentina|Peso|Americas|2
Chile|Peso|Americas|3
Peru|Sol|Americas|4
Venezuela|Bolívar|Americas|4|Bolivar
Costa Rica|Colón|Americas|4|Colon
Guatemala|Quetzal|Americas|4
Paraguay|Guaraní|Americas|5|Guarani
Haiti|Gourde|Americas|5
Bangladesh|Taka|Asia|4
Pakistan|Rupee|Asia|3|Pakistani rupee
Iran|Rial|Asia|4
Ukraine|Hryvnia|Europe|4
Romania|Leu|Europe|4
Georgia|Lari|Asia|5
Armenia|Dram|Asia|5
Mongolia|Tögrög|Asia|5|Tugrik
Cambodia|Riel|Asia|5
Myanmar|Kyat|Asia|5
Bhutan|Ngultrum|Asia|5
Botswana|Pula|Africa|5
Zambia|Kwacha|Africa|5
Angola|Kwanza|Africa|5
Albania|Lek|Europe|5
Serbia|Dinar|Europe|4
Jordan|Dinar|Asia|4
Kuwait|Dinar|Asia|4
Qatar|Riyal|Asia|4
Germany|Euro|Europe|1
Italy|Euro|Europe|1
Croatia|Euro|Europe|3
Australia|Dollar|Oceania|1|Australian dollar
New Zealand|Dollar|Oceania|2|New Zealand dollar`,
    qs: [
      { q: 'What is the currency of {country}?', a: 'currency', group: 'cont', alt: 'alt' },
      { q: 'The {currency} is the currency of which country?', a: 'country', group: 'cont', unique: true, dAdd: 1 }
    ]
  },
  {
    pack: 'geo-language', cat: 'geo', cols: ['country', 'lang', 'cont', 'd', 'alt'],
    rows: `
Brazil|Portuguese|Americas|1
Mexico|Spanish|Americas|1
Argentina|Spanish|Americas|1
Uruguay|Spanish|Americas|2
Colombia|Spanish|Americas|1
Chile|Spanish|Americas|1
Jamaica|English|Americas|2
Guyana|English|Americas|3
Belize|English|Americas|4
Egypt|Arabic|Africa|2
Saudi Arabia|Arabic|Asia|1
Tunisia|Arabic|Africa|3
Lebanon|Arabic|Asia|3
Jordan|Arabic|Asia|2
Iran|Persian|Asia|3|Farsi
Israel|Hebrew|Asia|2
Bangladesh|Bengali|Asia|3|Bangla
Netherlands|Dutch|Europe|1
Austria|German|Europe|1
Liechtenstein|German|Europe|3
Monaco|French|Europe|2
Andorra|Catalan|Europe|4
Greece|Greek|Europe|1
Turkey|Turkish|Europe|1
Poland|Polish|Europe|1
Portugal|Portuguese|Europe|1
Angola|Portuguese|Africa|3
Mozambique|Portuguese|Africa|3
Cape Verde|Portuguese|Africa|4
Senegal|French|Africa|3
Ivory Coast|French|Africa|3
Democratic Republic of the Congo|French|Africa|3
Indonesia|Indonesian|Asia|3|Bahasa Indonesia
Vietnam|Vietnamese|Asia|1
Thailand|Thai|Asia|1
Japan|Japanese|Asia|1
South Korea|Korean|Asia|1
Laos|Lao|Asia|4|Laotian
Cambodia|Khmer|Asia|4
Myanmar|Burmese|Asia|4|Myanmar
Nepal|Nepali|Asia|3
Mongolia|Mongolian|Asia|3
Uzbekistan|Uzbek|Asia|4
Armenia|Armenian|Asia|3
Georgia|Georgian|Asia|3
Iceland|Icelandic|Europe|2
Norway|Norwegian|Europe|1
Sweden|Swedish|Europe|1
Denmark|Danish|Europe|1
Estonia|Estonian|Europe|3
Latvia|Latvian|Europe|3
Lithuania|Lithuanian|Europe|3
Hungary|Hungarian|Europe|2|Magyar
Romania|Romanian|Europe|2
Bulgaria|Bulgarian|Europe|2
Serbia|Serbian|Europe|2
Croatia|Croatian|Europe|2
Czech Republic|Czech|Europe|2
Slovakia|Slovak|Europe|3
Ukraine|Ukrainian|Europe|2
Russia|Russian|Europe|1
Greenland|Greenlandic|Americas|4|Kalaallisut`,
    qs: [{ q: 'What is the official language of {country}?', a: 'lang', group: 'cont', alt: 'alt' }]
  },
  {
    pack: 'geo-rivers', cat: 'geo', cols: ['city', 'river', 'cont', 'd', 'alt'],
    rows: `
London|Thames|Europe|1|River Thames
Paris|Seine|Europe|1
Rome|Tiber|Europe|2
Vienna|Danube|Europe|2
Budapest|Danube|Europe|2
Bratislava|Danube|Europe|4
Prague|Vltava|Europe|4
Berlin|Spree|Europe|4
Hamburg|Elbe|Europe|3
Dresden|Elbe|Europe|4
Cologne|Rhine|Europe|3
Basel|Rhine|Europe|4
Düsseldorf|Rhine|Europe|4
Florence|Arno|Europe|4
Lisbon|Tagus|Europe|4|Tejo
Seville|Guadalquivir|Europe|5
Warsaw|Vistula|Europe|4
Kraków|Vistula|Europe|4
Kyiv|Dnieper|Europe|4
Moscow|Moskva|Europe|3
Saint Petersburg|Neva|Europe|4
Cairo|Nile|Africa|1
Baghdad|Tigris|Asia|3
Varanasi|Ganges|Asia|3|Ganga
Delhi|Yamuna|Asia|4
Wuhan|Yangtze|Asia|4
Bangkok|Chao Phraya|Asia|4
Phnom Penh|Mekong|Asia|4
Seoul|Han|Asia|4|Han River
Montreal|St. Lawrence|Americas|2|Saint Lawrence
Quebec City|St. Lawrence|Americas|3|Saint Lawrence
New York City|Hudson|Americas|3
Washington, D.C.|Potomac|Americas|3
New Orleans|Mississippi|Americas|2
St. Louis|Mississippi|Americas|3
Calgary|Bow|Americas|4|Bow River
Edmonton|North Saskatchewan|Americas|4
Winnipeg|Red|Americas|4|Red River
Dublin|Liffey|Europe|3|River Liffey
Belfast|Lagan|Europe|5
Newcastle upon Tyne|Tyne|Europe|2
Liverpool|Mersey|Europe|3
Amsterdam|Amstel|Europe|3
Bordeaux|Garonne|Europe|4
Nantes|Loire|Europe|4
Turin|Po|Europe|4
Geneva|Rhône|Europe|4|Rhone
Bern|Aare|Europe|5
Salzburg|Salzach|Europe|5
Munich|Isar|Europe|4
Frankfurt|Main|Europe|4
Riga|Daugava|Europe|5
Kinshasa|Congo|Africa|3
Bamako|Niger|Africa|4
Brisbane|Brisbane River|Oceania|3|Brisbane
Perth|Swan|Oceania|4|Swan River`,
    qs: [
      { q: 'Which river flows through {city}?', a: 'river', group: 'cont', alt: 'alt' },
      { q: 'Which of these cities stands on the {river}?', a: 'city', group: 'cont', unique: true }
    ]
  },
  {
    pack: 'geo-mountains', cat: 'geo', cols: ['country', 'peak', 'cont', 'd', 'alt'],
    rows: `
Japan|Mount Fuji|Asia|1|Fuji;Fujisan
Canada|Mount Logan|Americas|3|Logan
United States|Denali|Americas|3|Mount McKinley
Mexico|Pico de Orizaba|Americas|4|Citlaltépetl;Orizaba
Argentina|Aconcagua|Americas|3
Chile|Ojos del Salado|Americas|5
Peru|Huascarán|Americas|5|Huascaran
Ecuador|Chimborazo|Americas|4
Venezuela|Pico Bolívar|Americas|5|Pico Bolivar
Tanzania|Mount Kilimanjaro|Africa|2|Kilimanjaro
Kenya|Mount Kenya|Africa|3
Morocco|Toubkal|Africa|5|Jebel Toubkal
Russia|Mount Elbrus|Europe|3|Elbrus
France|Mont Blanc|Europe|2
Switzerland|Dufourspitze|Europe|5|Monte Rosa
Austria|Grossglockner|Europe|4|Großglockner
Germany|Zugspitze|Europe|4
Spain|Teide|Europe|5|Mount Teide
Greece|Mount Olympus|Europe|2|Olympus
Turkey|Mount Ararat|Asia|3|Ararat
Iran|Mount Damavand|Asia|5|Damavand
Scotland|Ben Nevis|Europe|2
Wales|Snowdon|Europe|3|Yr Wyddfa
England|Scafell Pike|Europe|4
Ireland|Carrauntoohil|Europe|5
Norway|Galdhøpiggen|Europe|5|Galdhopiggen
Sweden|Kebnekaise|Europe|5
Poland|Rysy|Europe|5
Slovenia|Triglav|Europe|5
Australia|Mount Kosciuszko|Oceania|3|Kosciuszko;Kosciusko
New Zealand|Aoraki / Mount Cook|Oceania|3|Mount Cook;Aoraki
Pakistan|K2|Asia|3
Malaysia|Mount Kinabalu|Asia|4|Kinabalu
Indonesia|Puncak Jaya|Asia|5
Philippines|Mount Apo|Asia|4|Apo
Taiwan|Yushan|Asia|5|Jade Mountain
Vietnam|Fansipan|Asia|5
Bolivia|Sajama|Americas|5|Nevado Sajama
Brazil|Pico da Neblina|Americas|5
Cameroon|Mount Cameroon|Africa|5`,
    qs: [
      { q: 'What is the highest mountain in {country}?', a: 'peak', group: 'cont', alt: 'alt' },
      { q: '{peak} is the highest mountain in which country?', a: 'country', group: 'cont', unique: true, dAdd: -1 }
    ]
  },
  {
    pack: 'geo-islands', cat: 'geo', cols: ['island', 'country', 'cont', 'd'],
    rows: `
Sicily|Italy|Europe|1
Sardinia|Italy|Europe|2
Capri|Italy|Europe|2
Corsica|France|Europe|2
Crete|Greece|Europe|2
Rhodes|Greece|Europe|2
Santorini|Greece|Europe|2
Lesbos|Greece|Europe|3
Mallorca|Spain|Europe|2
Ibiza|Spain|Europe|2
Tenerife|Spain|Europe|2
the Canary Islands|Spain|Europe|2
Madeira|Portugal|Europe|3
the Azores|Portugal|Europe|3
Gotland|Sweden|Europe|4
Bornholm|Denmark|Europe|4
the Faroe Islands|Denmark|Europe|3
Svalbard|Norway|Europe|3
the Isle of Skye|United Kingdom|Europe|2
the Falkland Islands|United Kingdom|Americas|3
Bermuda|United Kingdom|Americas|3
Bali|Indonesia|Asia|1
Java|Indonesia|Asia|2
Sumatra|Indonesia|Asia|3
Hokkaido|Japan|Asia|2
Okinawa|Japan|Asia|2
Honshu|Japan|Asia|3
Jeju|South Korea|Asia|3
Hainan|China|Asia|3
Phuket|Thailand|Asia|2
Luzon|Philippines|Asia|3
Mindanao|Philippines|Asia|3
Sakhalin|Russia|Asia|4
Socotra|Yemen|Asia|5
Zanzibar|Tanzania|Africa|3
Djerba|Tunisia|Africa|4
Réunion|France|Africa|4
Tasmania|Australia|Oceania|1
Tahiti|France|Oceania|3
New Caledonia|France|Oceania|4
the Galápagos Islands|Ecuador|Americas|3
Hawaii|United States|Americas|1
Puerto Rico|United States|Americas|2
Guam|United States|Oceania|3
Vancouver Island|Canada|Americas|2
Newfoundland|Canada|Americas|2
Martinique|France|Americas|4
Aruba|Netherlands|Americas|4
Curaçao|Netherlands|Americas|4`,
    qs: [{ q: 'Which country does {island} belong to?', a: 'country', group: 'cont' }]
  },
  {
    pack: 'geo-regional-capitals', cat: 'geo', cols: ['place', 'capital', 'country', 'd'],
    rows: `
New South Wales|Sydney|Australia|2
Victoria|Melbourne|Australia|2
Queensland|Brisbane|Australia|2
Western Australia|Perth|Australia|2
South Australia|Adelaide|Australia|3
Tasmania|Hobart|Australia|3
the Northern Territory|Darwin|Australia|3
British Columbia|Victoria|Canada|2
Alberta|Edmonton|Canada|2
Saskatchewan|Regina|Canada|3
Manitoba|Winnipeg|Canada|2
Ontario|Toronto|Canada|1
Quebec|Quebec City|Canada|1
New Brunswick|Fredericton|Canada|3
Nova Scotia|Halifax|Canada|2
Prince Edward Island|Charlottetown|Canada|3
Newfoundland and Labrador|St. John's|Canada|3
Yukon|Whitehorse|Canada|3
the Northwest Territories|Yellowknife|Canada|3
Nunavut|Iqaluit|Canada|4
Bavaria|Munich|Germany|2
Baden-Württemberg|Stuttgart|Germany|4
Hesse|Wiesbaden|Germany|5
North Rhine-Westphalia|Düsseldorf|Germany|4
Lower Saxony|Hanover|Germany|4
Saxony|Dresden|Germany|4
Schleswig-Holstein|Kiel|Germany|5
Rhineland-Palatinate|Mainz|Germany|5
Brandenburg|Potsdam|Germany|5
Scotland|Edinburgh|United Kingdom|1
Wales|Cardiff|United Kingdom|1
Northern Ireland|Belfast|United Kingdom|2
Catalonia|Barcelona|Spain|2
Andalusia|Seville|Spain|3
Tuscany|Florence|Italy|2
Sicily|Palermo|Italy|3
Lombardy|Milan|Italy|3
Tyrol|Innsbruck|Austria|4`,
    qs: [
      { q: 'What is the capital of {place} in {country}?', a: 'capital', group: 'country' },
      { q: '{capital} is the capital of which region of {country}?', a: 'place', group: 'country', unique: true }
    ]
  },
  {
    pack: 'geo-largest-city', cat: 'geo', cols: ['country', 'city', 'capital', 'd', 'w', 'wc'],
    rows: `
Australia|Sydney|Canberra|2|Melbourne;Brisbane;Canberra;Perth|Sydney;Melbourne;Perth;Brisbane
Canada|Toronto|Ottawa|1|Montreal;Vancouver;Ottawa;Calgary|Toronto;Montreal;Vancouver
the United States|New York City|Washington, D.C.|1|Los Angeles;Chicago;Washington, D.C.;Houston|New York City;Philadelphia;Boston
Brazil|São Paulo|Brasília|2|Rio de Janeiro;Brasília;Salvador|São Paulo;Rio de Janeiro;Salvador
Turkey|Istanbul|Ankara|2|Ankara;Izmir;Antalya|Istanbul;Izmir;Bursa
Nigeria|Lagos|Abuja|3|Abuja;Kano;Ibadan|Lagos;Kano;Ibadan
Switzerland|Zürich|Bern|3|Geneva;Bern;Basel|Zürich;Geneva;Basel
New Zealand|Auckland|Wellington|2|Wellington;Christchurch;Hamilton|Auckland;Christchurch;Dunedin
Morocco|Casablanca|Rabat|3|Rabat;Marrakesh;Fez|Casablanca;Marrakesh;Fez
Vietnam|Ho Chi Minh City|Hanoi|3|Hanoi;Da Nang;Haiphong|Ho Chi Minh City;Da Nang;Hue
Pakistan|Karachi|Islamabad|3|Lahore;Islamabad;Faisalabad|Karachi;Lahore;Rawalpindi
Ecuador|Guayaquil|Quito|4|Quito;Cuenca;Manta|Guayaquil;Cuenca;Loja
Kazakhstan|Almaty|Astana|4|Astana;Shymkent;Karaganda|Almaty;Shymkent;Aktobe
Tanzania|Dar es Salaam|Dodoma|4|Dodoma;Arusha;Mwanza|Dar es Salaam;Arusha;Zanzibar City
Ivory Coast|Abidjan|Yamoussoukro|4|Yamoussoukro;Bouaké;San-Pédro|Abidjan;Bouaké;San-Pédro
Cameroon|Douala|Yaoundé|5|Yaoundé;Garoua;Bamenda|Douala;Garoua;Bamenda
Myanmar|Yangon|Naypyidaw|4|Mandalay;Naypyidaw;Bago|Yangon;Mandalay;Bago
the United Arab Emirates|Dubai|Abu Dhabi|2|Abu Dhabi;Sharjah;Al Ain|Dubai;Sharjah;Al Ain
Scotland|Glasgow|Edinburgh|3|Edinburgh;Aberdeen;Dundee|Glasgow;Aberdeen;Dundee
Belize|Belize City|Belmopan|5|Belmopan;San Ignacio;Orange Walk|Belize City;San Ignacio;Orange Walk
the Philippines|Quezon City|Manila|5|Manila;Davao City;Cebu City|Quezon City;Davao City;Cebu City
India|Mumbai|New Delhi|3|Kolkata;Bangalore;Chennai|Mumbai;Kolkata;Bangalore`,
    qs: [
      { q: 'What is the largest city in {country}?', a: 'city', wrong: 'w', when: r => r.country !== 'India' },
      { q: 'What is the capital of {country}? (Careful: it is not {city}.)', a: 'capital', wrong: 'wc', dAdd: -1 }
    ]
  },
  {
    pack: 'geo-landmark-city', cat: 'geo', cols: ['landmark', 'city', 'cont', 'd'],
    rows: `
the Colosseum|Rome|Europe|1
the Trevi Fountain|Rome|Europe|2
the Sagrada Família|Barcelona|Europe|2
Las Ramblas|Barcelona|Europe|3
the Acropolis|Athens|Europe|1
Big Ben|London|Europe|1
Tower Bridge|London|Europe|1
Buckingham Palace|London|Europe|1
the Louvre|Paris|Europe|1
the Arc de Triomphe|Paris|Europe|1
the Sacré-Cœur basilica|Paris|Europe|2
the Reichstag building|Berlin|Europe|3
Checkpoint Charlie|Berlin|Europe|3
the Charles Bridge|Prague|Europe|3
Schönbrunn Palace|Vienna|Europe|3
the Alhambra|Granada|Europe|3
the Prado Museum|Madrid|Europe|3
the Rijksmuseum|Amsterdam|Europe|3
the Anne Frank House|Amsterdam|Europe|2
the Atomium|Brussels|Europe|3
the Manneken Pis statue|Brussels|Europe|3
the Little Mermaid statue|Copenhagen|Europe|3
Edinburgh Castle|Edinburgh|Europe|1
Red Square|Moscow|Europe|1
St. Basil's Cathedral|Moscow|Europe|2
the Hermitage Museum|Saint Petersburg|Europe|3
the Hagia Sophia|Istanbul|Europe|2
Topkapı Palace|Istanbul|Europe|3
the Rialto Bridge|Venice|Europe|3
the Western Wall|Jerusalem|Asia|2
the Forbidden City|Beijing|Asia|1
the Bund waterfront|Shanghai|Asia|3
Victoria Peak|Hong Kong|Asia|3
the Terracotta Army|Xi'an|Asia|3
the Potala Palace|Lhasa|Asia|4
the Taj Mahal|Agra|Asia|2
the Gateway of India|Mumbai|Asia|3
the Golden Temple|Amritsar|Asia|4
the Hawa Mahal ("Palace of the Winds")|Jaipur|Asia|4
the Grand Palace|Bangkok|Asia|3
the Shwedagon Pagoda|Yangon|Asia|4
the Petronas Towers|Kuala Lumpur|Asia|2
the Merlion statue|Singapore|Asia|2
Gardens by the Bay|Singapore|Asia|3
the Tokyo Skytree|Tokyo|Asia|2
the Fushimi Inari shrine|Kyoto|Asia|3
the Burj Al Arab hotel|Dubai|Asia|2
the Sheikh Zayed Grand Mosque|Abu Dhabi|Asia|3
Table Mountain|Cape Town|Africa|2
Robben Island|Cape Town|Africa|3
the Hassan II Mosque|Casablanca|Africa|4
the Jemaa el-Fna square|Marrakesh|Africa|4
the Valley of the Kings|Luxor|Africa|4
the Statue of Liberty|New York City|Americas|1
Times Square|New York City|Americas|1
the Golden Gate Bridge|San Francisco|Americas|1
the Space Needle|Seattle|Americas|2
the Gateway Arch|St. Louis|Americas|3
the Hollywood Sign|Los Angeles|Americas|1
the Alamo|San Antonio|Americas|3
the Liberty Bell|Philadelphia|Americas|3
the Lincoln Memorial|Washington, D.C.|Americas|2
the Zócalo square|Mexico City|Americas|4
Christ the Redeemer|Rio de Janeiro|Americas|1
Copacabana Beach|Rio de Janeiro|Americas|2
the Sydney Opera House|Sydney|Oceania|1
Bondi Beach|Sydney|Oceania|2`,
    qs: [{ q: 'In which city would you find {landmark}?', a: 'city', group: 'cont' }]
  }
];
