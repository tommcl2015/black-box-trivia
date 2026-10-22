// Sports & leisure fact tables.
module.exports = [
  {
    pack: 'spo-athletes', cat: 'spo', cols: ['who', 'sport', 'd'],
    rows: `
Roger Federer|Tennis|1
Rafael Nadal|Tennis|1
Novak Djokovic|Tennis|1
Naomi Osaka|Tennis|2
Martina Navratilova|Tennis|2
Steffi Graf|Tennis|2
Björn Borg|Tennis|2
Lionel Messi|Soccer|1
Cristiano Ronaldo|Soccer|1
Diego Maradona|Soccer|1
Zinedine Zidane|Soccer|2
Kylian Mbappé|Soccer|2
Erling Haaland|Soccer|2
David Beckham|Soccer|1
Megan Rapinoe|Soccer|2
Rory McIlroy|Golf|2
Annika Sörenstam|Golf|3
Arnold Palmer|Golf|2
Seve Ballesteros|Golf|3
Simone Biles|Gymnastics|1
Nadia Comăneci|Gymnastics|2
Katie Ledecky|Swimming|2
Mark Spitz|Swimming|3
Ian Thorpe|Swimming|3
Sachin Tendulkar|Cricket|2
Virat Kohli|Cricket|2
Don Bradman|Cricket|3
Shane Warne|Cricket|3
Jonah Lomu|Rugby|3
Richie McCaw|Rugby|3
Jonny Wilkinson|Rugby|3
Valentino Rossi|Motorcycle racing|2
Marc Márquez|Motorcycle racing|3
Tony Hawk|Skateboarding|1
Shaun White|Snowboarding|2
Lindsey Vonn|Alpine skiing|2
Mikaela Shiffrin|Alpine skiing|2
Ingemar Stenmark|Alpine skiing|4
Eddie "the Eagle" Edwards|Ski jumping|3
Mike Tyson|Boxing|1
Floyd Mayweather Jr.|Boxing|2
Conor McGregor|Mixed martial arts|2
Ronda Rousey|Mixed martial arts|3
Garry Kasparov|Chess|2
Magnus Carlsen|Chess|2
Bobby Fischer|Chess|2
Babe Ruth|Baseball|2
Derek Jeter|Baseball|2
Ichiro Suzuki|Baseball|3
Eddy Merckx|Cycling|3
Tadej Pogačar|Cycling|3
Chris Hoy|Track cycling|4
Phil Taylor|Darts|3
Luke Littler|Darts|3
Ronnie O'Sullivan|Snooker|3
Mo Farah|Distance running|2
Paula Radcliffe|Marathon running|3
Sergey Bubka|Pole vault|3
Carl Lewis|Sprinting and long jump|3
Jesse Owens|Sprinting and long jump|2
Jayne Torvill and Christopher Dean|Ice dancing|3
Yuzuru Hanyu|Figure skating|3
Kim Yuna|Figure skating|3
Kelly Slater|Surfing|2
Shaquille O'Neal|Basketball|1
Yao Ming|Basketball|2
Dirk Nowitzki|Basketball|3
Giannis Antetokounmpo|Basketball|3
Caitlin Clark|Basketball|2
Hulk Hogan|Professional wrestling|1
Lewis Hamilton|Formula 1|1
Ayrton Senna|Formula 1|2`,
    qs: [{ q: 'Which sport is {who} famous for?', a: 'sport' }]
  },
  {
    pack: 'spo-f1-champions', cat: 'spo', cols: ['year', 'who', 'd'],
    rows: `
1950|Giuseppe Farina|5
1951|Juan Manuel Fangio|4
1952|Alberto Ascari|5
1954|Juan Manuel Fangio|4
1958|Mike Hawthorn|5
1959|Jack Brabham|5
1961|Phil Hill|5
1962|Graham Hill|4
1963|Jim Clark|4
1964|John Surtees|5
1967|Denny Hulme|5
1969|Jackie Stewart|4
1970|Jochen Rindt|5
1972|Emerson Fittipaldi|4
1975|Niki Lauda|4
1976|James Hunt|3
1978|Mario Andretti|4
1979|Jody Scheckter|5
1980|Alan Jones|5
1981|Nelson Piquet|4
1982|Keke Rosberg|5
1985|Alain Prost|4
1988|Ayrton Senna|3
1992|Nigel Mansell|3
1994|Michael Schumacher|3
1996|Damon Hill|3
1997|Jacques Villeneuve|3
1998|Mika Häkkinen|3
2000|Michael Schumacher|3
2005|Fernando Alonso|3
2007|Kimi Räikkönen|3
2008|Lewis Hamilton|2
2009|Jenson Button|3
2010|Sebastian Vettel|2
2016|Nico Rosberg|3
2017|Lewis Hamilton|2
2021|Max Verstappen|2
2025|Lando Norris|2`,
    qs: [{ q: 'Who won the Formula One World Championship in {year}?', a: 'who', near: 'year' }]
  },
  {
    pack: 'spo-ballon-dor', cat: 'spo', cols: ['year', 'who', 'd'],
    rows: `
1995|George Weah|4
1996|Matthias Sammer|5
1997|Ronaldo Nazário|4
1998|Zinedine Zidane|3
1999|Rivaldo|4
2000|Luís Figo|4
2001|Michael Owen|4
2003|Pavel Nedvěd|5
2004|Andriy Shevchenko|4
2005|Ronaldinho|3
2006|Fabio Cannavaro|4
2007|Kaká|3
2008|Cristiano Ronaldo|2
2009|Lionel Messi|2
2013|Cristiano Ronaldo|2
2015|Lionel Messi|2
2018|Luka Modrić|3
2022|Karim Benzema|3
2023|Lionel Messi|2
2024|Rodri|3
2025|Ousmane Dembélé|3`,
    qs: [{ q: "Who won the men's Ballon d'Or in {year}?", a: 'who', near: 'year' }]
  },
  {
    pack: 'spo-champions-league', cat: 'spo', cols: ['year', 'club', 'd'],
    rows: `
1991|Red Star Belgrade|5
1993|Marseille|4
1995|Ajax|4
1997|Borussia Dortmund|4
1999|Manchester United|3
2001|Bayern Munich|4
2003|AC Milan|4
2004|Porto|3
2005|Liverpool|3
2006|Barcelona|3
2008|Manchester United|3
2010|Inter Milan|3
2012|Chelsea|3
2013|Bayern Munich|3
2015|Barcelona|3
2018|Real Madrid|3
2019|Liverpool|3
2020|Bayern Munich|3
2021|Chelsea|3
2023|Manchester City|2
2024|Real Madrid|2
2025|Paris Saint-Germain|2
2026|Paris Saint-Germain|2`,
    qs: [{ q: 'Which club won the UEFA Champions League in {year}?', a: 'club', near: 'year' }]
  },
  {
    pack: 'spo-wimbledon', cat: 'spo', cols: ['year', 'who', 'g', 'd'],
    rows: `
1980|Björn Borg|m|3
1981|John McEnroe|m|3
1982|Jimmy Connors|m|4
1985|Boris Becker|m|3
1987|Pat Cash|m|4
1988|Stefan Edberg|m|4
1991|Michael Stich|m|5
1992|Andre Agassi|m|3
1993|Pete Sampras|m|3
1996|Richard Krajicek|m|5
2001|Goran Ivanišević|m|4
2002|Lleyton Hewitt|m|3
2003|Roger Federer|m|2
2008|Rafael Nadal|m|2
2011|Novak Djokovic|m|2
2013|Andy Murray|m|2
2023|Carlos Alcaraz|m|2
2025|Jannik Sinner|m|2
2026|Jannik Sinner|m|2
1990|Martina Navratilova|f|3
1991|Steffi Graf|f|3
1994|Conchita Martínez|f|5
1997|Martina Hingis|f|4
1998|Jana Novotná|f|4
1999|Lindsay Davenport|f|4
2000|Venus Williams|f|3
2002|Serena Williams|f|2
2004|Maria Sharapova|f|3
2006|Amélie Mauresmo|f|4
2011|Petra Kvitová|f|4
2013|Marion Bartoli|f|4
2017|Garbiñe Muguruza|f|4
2018|Angelique Kerber|f|4
2019|Simona Halep|f|4
2021|Ashleigh Barty|f|3
2022|Elena Rybakina|f|4
2023|Markéta Vondroušová|f|4
2024|Barbora Krejčíková|f|4
2025|Iga Świątek|f|3
2026|Linda Nosková|f|4`,
    qs: [
      { q: "Who won the Wimbledon men's singles title in {year}?", a: 'who', group: 'g', near: 'year', when: r => r.g === 'm' },
      { q: "Who won the Wimbledon women's singles title in {year}?", a: 'who', group: 'g', near: 'year', when: r => r.g === 'f' }
    ]
  },
  {
    pack: 'spo-team-sizes', cat: 'spo', cols: ['sport', 'n', 'd'],
    rows: `
soccer|11|1
rugby union|15|3
rugby league|13|4
basketball|5|1
volleyball|6|2
ice hockey|6|2
baseball|9|2
cricket|11|2
netball|7|3
water polo|7|4
handball|7|4
field hockey|11|3
Australian rules football|18|4
Gaelic football|15|5
polo|4|4
beach volleyball|2|2
curling|4|3`,
    qs: [{ q: 'How many players does one {sport} team have in play at a time?', a: 'n' }]
  },
  {
    pack: 'spo-sport-origins', cat: 'spo', cols: ['sport', 'where', 'd'],
    rows: `
judo|Japan|2
sumo wrestling|Japan|1
taekwondo|South Korea|2
cricket|England|2
rugby|England|2
golf|Scotland|2
curling|Scotland|3
ice hockey|Canada|2
volleyball|United States|3
baseball|United States|2
table tennis|England|4
lawn tennis|England|3
polo|Persia|4
kabaddi|India|4
capoeira|Brazil|3
hurling|Ireland|3
pétanque|France|3
bobsleigh|Switzerland|5`,
    qs: [{ q: 'In which country did {sport} originate?', a: 'where' }]
  },
  {
    pack: 'spo-brands', cat: 'spo', cols: ['brand', 'country', 'cont', 'd'],
    rows: `
Nokia|Finland|Europe|2
Samsung|South Korea|Asia|1
LG|South Korea|Asia|2
Hyundai|South Korea|Asia|2
Kia|South Korea|Asia|2
Sony|Japan|Asia|1
Panasonic|Japan|Asia|2
Canon|Japan|Asia|2
Uniqlo|Japan|Asia|2
Lenovo|China|Asia|3
Huawei|China|Asia|2
Xiaomi|China|Asia|3
Alibaba|China|Asia|2
Tata|India|Asia|3
Volvo|Sweden|Europe|2
H&M|Sweden|Europe|2
Spotify|Sweden|Europe|3
Ericsson|Sweden|Europe|3
Carlsberg|Denmark|Europe|3
Pandora jewellery|Denmark|Europe|4
Philips|Netherlands|Europe|3
Adidas|Germany|Europe|1
Puma|Germany|Europe|2
BMW|Germany|Europe|1
Siemens|Germany|Europe|2
Bosch|Germany|Europe|3
Haribo|Germany|Europe|3
Nivea|Germany|Europe|3
Nestlé|Switzerland|Europe|3
Rolex|Switzerland|Europe|2
Swatch|Switzerland|Europe|2
Lindt|Switzerland|Europe|3
Toblerone|Switzerland|Europe|2
Fiat|Italy|Europe|2
Gucci|Italy|Europe|2
Prada|Italy|Europe|2
Ferrero, maker of Nutella|Italy|Europe|3
Vespa scooters|Italy|Europe|2
Peugeot|France|Europe|2
Renault|France|Europe|2
Chanel|France|Europe|2
L'Oréal|France|Europe|2
Michelin|France|Europe|3
Zara|Spain|Europe|2
SEAT|Spain|Europe|3
Rolls-Royce|United Kingdom|Europe|2
Burberry|United Kingdom|Europe|2
Cadbury|United Kingdom|Europe|2
Dyson|United Kingdom|Europe|3
Lululemon|Canada|Americas|3
Canada Goose|Canada|Americas|2
Shopify|Canada|Americas|3
Red Bull|Austria|Europe|3
Swarovski|Austria|Europe|3
Škoda|Czech Republic|Europe|3
Havaianas|Brazil|Americas|3
Embraer|Brazil|Americas|4
Qantas|Australia|Oceania|2
Vegemite|Australia|Oceania|2
Emirates airline|United Arab Emirates|Asia|2`,
    qs: [{ q: 'In which country was the brand {brand} founded?', a: 'country', group: 'cont' }]
  },
  {
    pack: 'spo-founders', cat: 'spo', cols: ['co', 'who', 'd', 'alt'],
    rows: `
Google|Larry Page and Sergey Brin|2|Page and Brin
Netflix|Reed Hastings and Marc Randolph|3|Reed Hastings
Alibaba|Jack Ma|2|Ma
Nike|Phil Knight and Bill Bowerman|3|Phil Knight
Adidas|Adolf "Adi" Dassler|3|Adi Dassler;Dassler
Puma|Rudolf Dassler|4|Dassler
Honda|Soichiro Honda|2|Honda
Ferrari|Enzo Ferrari|1|Ferrari
Lamborghini, which began by making tractors|Ferruccio Lamborghini|3|Lamborghini
Porsche|Ferdinand Porsche|2|Porsche
Walmart|Sam Walton|3|Walton
KFC|Colonel Harland Sanders|1|Colonel Sanders;Harland Sanders;Sanders
Disney|Walt and Roy Disney|1|Walt Disney
Harley-Davidson|William Harley and Arthur Davidson|2|Harley and Davidson
Hewlett-Packard|Bill Hewlett and Dave Packard|2|Hewlett and Packard
Dell|Michael Dell|1|Dell
Oracle|Larry Ellison|3|Ellison
Rolex|Hans Wilsdorf|5|Wilsdorf
Chanel|Coco Chanel|1|Chanel
Kellogg's|Will Keith Kellogg|2|W. K. Kellogg;Kellogg
Heinz|Henry J. Heinz|2|Heinz
Cadbury|John Cadbury|2|Cadbury
Nestlé|Henri Nestlé|2|Nestle;Nestlé
Hershey's|Milton Hershey|2|Hershey
Boeing|William Boeing|2|Boeing
Sony|Masaru Ibuka and Akio Morita|4|Morita;Akio Morita
Uber|Travis Kalanick and Garrett Camp|4|Kalanick
Airbnb|Brian Chesky, Joe Gebbia and Nathan Blecharczyk|4|Chesky
YouTube|Chad Hurley, Steve Chen and Jawed Karim|4|Hurley, Chen and Karim
Instagram|Kevin Systrom and Mike Krieger|4|Systrom
WhatsApp|Jan Koum and Brian Acton|4|Koum
Wikipedia|Jimmy Wales and Larry Sanger|3|Jimmy Wales;Wales
Intel|Robert Noyce and Gordon Moore|4|Noyce and Moore
eBay|Pierre Omidyar|4|Omidyar
Zoom|Eric Yuan|4|Yuan`,
    qs: [{ q: 'Who founded {co}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'spo-food-origins', cat: 'spo', cols: ['item', 'country', 'kind', 'd'],
    rows: `
Parmesan (Parmigiano-Reggiano) cheese|Italy|cheese|1
Gorgonzola cheese|Italy|cheese|2
Pecorino cheese|Italy|cheese|3
Mascarpone cheese|Italy|cheese|2
Burrata cheese|Italy|cheese|3
Brie cheese|France|cheese|2
Camembert cheese|France|cheese|2
Roquefort cheese|France|cheese|3
Comté cheese|France|cheese|4
Gouda cheese|Netherlands|cheese|2
Edam cheese|Netherlands|cheese|2
Gruyère cheese|Switzerland|cheese|3
Raclette cheese|Switzerland|cheese|3
Cheddar cheese|England|cheese|1
Stilton cheese|England|cheese|3
Halloumi cheese|Cyprus|cheese|3
Manchego cheese|Spain|cheese|3
Paneer cheese|India|cheese|2
Havarti cheese|Denmark|cheese|4
Jarlsberg cheese|Norway|cheese|4
Cotija cheese|Mexico|cheese|4
Monterey Jack cheese|United States|cheese|3
soju|South Korea|drink|3
ouzo|Greece|drink|2
retsina wine|Greece|drink|4
grappa|Italy|drink|3
limoncello|Italy|drink|2
sangria|Spain|drink|1
sherry|Spain|drink|3
port wine|Portugal|drink|2
cognac|France|drink|2
calvados apple brandy|France|drink|4
mezcal|Mexico|drink|3
cachaça|Brazil|drink|3
the mojito cocktail|Cuba|drink|3
the piña colada|Puerto Rico|drink|4
Jägermeister|Germany|drink|3
bourbon whiskey|United States|drink|3
baijiu|China|drink|4
Tokaji wine|Hungary|drink|4
Baileys Irish Cream|Ireland|drink|2
Pimm's|England|drink|3`,
    qs: [{ q: 'Which country does {item} come from?', a: 'country', group: 'kind' }]
  }
];
