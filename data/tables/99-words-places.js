// Loanwords, island oceans, sports venues, novel settings.
module.exports = [
  {
    pack: 'art-loanwords', cat: 'art', cols: ['word', 'lang', 'fam', 'd'],
    rows: `
kindergarten|German|eu|2
wanderlust|German|eu|2
poltergeist|German|eu|3
hamster|German|eu|4
rucksack|German|eu|3
déjà vu|French|eu|1
ballet|French|eu|1
café|French|eu|1
entrepreneur|French|eu|3
piano|Italian|eu|2
graffiti|Italian|eu|2
umbrella|Italian|eu|3
volcano|Italian|eu|3
mosquito|Spanish|eu|2
tornado|Spanish|eu|3
canyon|Spanish|eu|2
patio|Spanish|eu|3
guerrilla|Spanish|eu|3
yacht|Dutch|eu|3
cookie|Dutch|eu|3
boss|Dutch|eu|4
cruise|Dutch|eu|4
ski|Norwegian|eu|2
slalom|Norwegian|eu|3
fjord|Norwegian|eu|1
ombudsman|Swedish|eu|3
smorgasbord|Swedish|eu|2
sauna|Finnish|eu|1
robot|Czech|eu|3
pistol|Czech|eu|5
tsunami|Japanese|as|1
karaoke|Japanese|as|1
emoji|Japanese|as|1
origami|Japanese|as|1
kowtow|Chinese|as|3
shampoo|Hindi|as|3
bungalow|Hindi|as|3
algebra|Arabic|me|2
alcohol|Arabic|me|3
bazaar|Persian|me|3
yogurt|Turkish|me|3
chocolate|Nahuatl (Aztec)|am|3
tomato|Nahuatl (Aztec)|am|3
avocado|Nahuatl (Aztec)|am|3
coyote|Nahuatl (Aztec)|am|3
kayak|Inuit|am|2
igloo|Inuit|am|1
anorak|Inuit|am|3
hammock|Taíno (Caribbean)|am|4
hurricane|Taíno (Caribbean)|am|4
barbecue|Taíno (Caribbean)|am|4
kangaroo|Guugu Yimithirr (Aboriginal Australian)|oc|4
taboo|Tongan|oc|4
tattoo|Tahitian|oc|4
ukulele|Hawaiian|oc|2
wiki|Hawaiian|oc|3
llama|Quechua|am|3
puma|Quechua|am|4
condor|Quechua|am|4
raccoon|Algonquian|am|4
moose|Algonquian|am|4
skunk|Algonquian|am|4`,
    qs: [{ q: 'Which language gave English the word "{word}"?', a: 'lang', group: 'fam' }]
  },
  {
    pack: 'geo-island-oceans', cat: 'geo', cols: ['island', 'ocean', 'd'],
    rows: `
Madagascar|Indian Ocean|1
the Maldives|Indian Ocean|1
the Seychelles|Indian Ocean|2
Mauritius|Indian Ocean|2
Zanzibar|Indian Ocean|3
Réunion|Indian Ocean|3
Sri Lanka|Indian Ocean|1
Christmas Island (Australia)|Indian Ocean|4
the Comoros|Indian Ocean|4
Socotra|Indian Ocean|5
Iceland|Atlantic Ocean|1
Bermuda|Atlantic Ocean|2
the Azores|Atlantic Ocean|2
the Canary Islands|Atlantic Ocean|2
the Falkland Islands|Atlantic Ocean|2
Cape Verde|Atlantic Ocean|3
Saint Helena, where Napoleon died|Atlantic Ocean|3
Tristan da Cunha|Atlantic Ocean|4
the Faroe Islands|Atlantic Ocean|3
the Bahamas|Atlantic Ocean|2
Madeira|Atlantic Ocean|3
Fiji|Pacific Ocean|1
Hawaii|Pacific Ocean|1
the Galápagos Islands|Pacific Ocean|1
Tahiti|Pacific Ocean|2
Easter Island|Pacific Ocean|2
Samoa|Pacific Ocean|2
Guam|Pacific Ocean|2
Tonga|Pacific Ocean|2
the Marshall Islands|Pacific Ocean|3
Pitcairn Island|Pacific Ocean|4
New Caledonia|Pacific Ocean|3
Svalbard|Arctic Ocean|3
Franz Josef Land|Arctic Ocean|4
Ellesmere Island|Arctic Ocean|4
Wrangel Island|Arctic Ocean|5
the Antarctic island South Georgia|Southern Ocean|4`,
    qs: [{ q: 'In which ocean is {island}?', a: 'ocean' }]
  },
  {
    pack: 'spo-event-venues', cat: 'spo', cols: ['event', 'place', 'kind', 'd'],
    rows: `
the Wimbledon Championships|London|tennis|1
the French Open (Roland-Garros)|Paris|tennis|1
the Australian Open|Melbourne|tennis|1
the US Open tennis championships|New York|tennis|2
the Masters golf tournament|Augusta, Georgia|golf|2
the Monaco Grand Prix|Monte Carlo|motor|1
the Indianapolis 500|Indianapolis|motor|1
the 24 Hours of Le Mans|Le Mans|motor|2
the Daytona 500|Daytona Beach|motor|2
the Bathurst 1000|Mount Panorama, Bathurst|motor|4
the British Grand Prix|Silverstone|motor|2
the Italian Grand Prix|Monza|motor|3
the Belgian Grand Prix|Spa-Francorchamps|motor|3
the Japanese Grand Prix|Suzuka|motor|3
the Brazilian (São Paulo) Grand Prix|Interlagos|motor|4
the Isle of Man TT motorcycle races|the Isle of Man|motor|3
the Kentucky Derby|Louisville|horse|3
the Melbourne Cup|Melbourne (Flemington)|horse|3
the Grand National|Aintree, Liverpool|horse|3
Royal Ascot|Ascot|horse|2
the Palio horse race around a medieval square|Siena|horse|4
the Boston Marathon|Boston|run|1
the Comrades Marathon|South Africa|run|4
the Henley Royal Regatta (rowing)|Henley-on-Thames|water|3
the Calgary Stampede rodeo|Calgary|other|2
the Tour de France's traditional final stage|Paris (Champs-Élysées)|other|2
the Hong Kong Sevens rugby tournament|Hong Kong|other|3
the Running of the Bulls|Pamplona|other|2
the Ryder Cup (golf) 2025 edition|Bethpage Black, New York|golf|5
the Australian Football League Grand Final|Melbourne Cricket Ground|other|3
the FA Cup Final|Wembley Stadium|other|2
Super Bowl LX (2026)|Santa Clara, California|other|4
the 2026 FIFA World Cup final|New Jersey (MetLife Stadium)|other|3`,
    qs: [{ q: 'Where is {event} held?', a: 'place', group: 'kind', when: r => !/20\d\d/.test(r.event) },
         { q: 'Where was {event} held?', a: 'place', group: 'kind', when: r => /20\d\d/.test(r.event) }]
  },
  {
    pack: 'art-novel-settings', cat: 'art', cols: ['book', 'setting', 'd'],
    rows: `
Les Misérables|Paris|2
The Hunchback of Notre-Dame|Paris|1
A Tale of Two Cities|London and Paris|2
Oliver Twist|London|1
Anna Karenina|Russia|2
War and Peace|Russia|1
The Great Gatsby|Long Island (West Egg)|2
To Kill a Mockingbird|Alabama|2
Gone with the Wind|Georgia (US)|2
Ulysses (James Joyce)|Dublin|2
Death in Venice|Venice|1
The Name of the Rose|an Italian monastery|3
One Hundred Years of Solitude|Macondo|3
Things Fall Apart|Nigeria (Igboland)|2
The Kite Runner|Afghanistan|1
Memoirs of a Geisha|Japan (Kyoto)|1
Life of Pi (most of it)|a lifeboat in the Pacific|2
Robinson Crusoe|a desert island|1
The Old Man and the Sea|Cuba|2
Heidi|the Swiss Alps|1
Anne of Green Gables|Prince Edward Island|2
Out of Africa|Kenya|3
The Girl with the Dragon Tattoo|Sweden|2
Doctor Zhivago|Russia|2
Captain Corelli's Mandolin|Cephalonia, Greece|3`,
    qs: [{ q: 'Where is {book} set?', a: 'setting' }]
  }
];
