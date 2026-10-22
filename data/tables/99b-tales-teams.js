// Fairy tales, national team nicknames, neighbours, brand mascots.
module.exports = [
  {
    pack: 'art-fairy-tales', cat: 'art', cols: ['what', 'tale', 'd'],
    rows: `
a glass slipper left on the palace stairs|Cinderella|1
a poisoned apple and seven dwarfs|Snow White|1
a princess pricking her finger on a spindle and sleeping for 100 years|Sleeping Beauty|1
a girl who lets down her very long hair from a tower|Rapunzel|1
a trail of breadcrumbs and a gingerbread house|Hansel and Gretel|1
a pea hidden under twenty mattresses|The Princess and the Pea|1
a magic beanstalk and a giant in the clouds|Jack and the Beanstalk|1
three bowls of porridge, three chairs and three beds|Goldilocks and the Three Bears|1
a wolf dressed as a grandmother|Little Red Riding Hood|1
a cygnet teased for being ugly that grows into a swan|The Ugly Duckling|1
a vain ruler parading in invisible clothes|The Emperor's New Clothes|1
a mermaid who gives up her voice for legs|The Little Mermaid|1
a man who leads a town's rats, then its children, away with his music|The Pied Piper of Hamelin|2
a little man who spins straw into gold and whose name must be guessed|Rumpelstiltskin|2
a princess who kisses a frog|The Frog Prince|1
a clever cat in boots who wins his master a fortune|Puss in Boots|2
a wolf who huffs and puffs at houses of straw, sticks and bricks|The Three Little Pigs|1
a slow tortoise beating a boastful hare|The Tortoise and the Hare|1
a shepherd boy who raised false alarms until nobody believed him|The Boy Who Cried Wolf|1
"Open sesame!" and forty thieves|Ali Baba and the Forty Thieves|2
a girl no bigger than a thumb, born from a flower|Thumbelina|2
a queen whose splinter of mirror freezes a boy's heart|The Snow Queen|3
a donkey, dog, cat and rooster who set off to become musicians|The Town Musicians of Bremen|3
"Run, run, as fast as you can! You can't catch me!"|The Gingerbread Man|1
elves who secretly finish a poor shoemaker's work at night|The Elves and the Shoemaker|2
princesses whose shoes are worn out every morning|The Twelve Dancing Princesses|3
a fox who decides the grapes he can't reach must be sour|The Fox and the Grapes|2
a goose that lays golden eggs, killed by a greedy owner|The Goose That Laid the Golden Eggs|2
a wooden puppet whose nose grows when he lies|Pinocchio|1
a girl who falls down a rabbit hole|Alice's Adventures in Wonderland|1
a beautiful girl who lives in a castle with a cursed beast|Beauty and the Beast|1
a sailor with seven voyages in the Arabian Nights|Sinbad the Sailor|2
a storyteller who tells a king a tale every night to save her life|One Thousand and One Nights|3`,
    qs: [{ q: 'Which story features {what}?', a: 'tale' }]
  },
  {
    pack: 'spo-team-nicknames', cat: 'spo', cols: ['nick', 'team', 'sport', 'd'],
    rows: `
the All Blacks|New Zealand|rugby|1
the Wallabies|Australia|rugby|2
the Springboks|South Africa|rugby|2
the Pumas|Argentina|rugby|3
the Brave Blossoms|Japan|rugby|4
the Flying Fijians|Fiji|rugby|3
the Black Ferns|New Zealand (women)|rugby|3
the Socceroos|Australia|football|2
the Matildas|Australia (women)|football|2
the Lionesses|England (women)|football|2
the Three Lions|England|football|1
Les Bleus|France|football|2
the Azzurri|Italy|football|2
Oranje|the Netherlands|football|2
La Roja|Spain|football|3
the Seleção|Brazil|football|2
La Albiceleste|Argentina|football|3
El Tri|Mexico|football|3
the Red Devils|Belgium|football|3
the Vatreni (Blazers)|Croatia|football|4
the Samurai Blue|Japan|football|3
the Taeguk Warriors|South Korea|football|4
the Super Eagles|Nigeria|football|2
the Black Stars|Ghana|football|3
the Indomitable Lions|Cameroon|football|3
the Pharaohs|Egypt|football|3
Bafana Bafana|South Africa|football|3
the Atlas Lions|Morocco|football|3
the Desert Foxes|Algeria|football|4
the Elephants|Ivory Coast|football|4
the Kiwis|New Zealand|rugby league|4
the Black Caps|New Zealand|cricket|3
the Proteas|South Africa|cricket|3
the Windies|West Indies|cricket|3
the Boomers|Australia|basketball|4`,
    qs: [{ q: 'Which national team is nicknamed {nick}?', a: 'team', group: 'sport' }]
  },
  {
    pack: 'geo-neighbours', cat: 'geo', cols: ['country', 'n', 'w', 'd'],
    rows: `
France|Belgium|Austria;Denmark;Czechia|2
Germany|Poland|Hungary;Slovakia;Sweden|2
Spain|Portugal|Italy;Belgium;Switzerland|1
Italy|Slovenia|Croatia;Hungary;Germany|3
Austria|Liechtenstein|Poland;Croatia;Belgium|4
Switzerland|Liechtenstein|Belgium;Slovenia;the Netherlands|3
Poland|Lithuania|Latvia;Hungary;Romania|3
Hungary|Romania|Poland;Bulgaria;Czechia|3
Greece|Albania|Serbia;Romania;Croatia|3
Norway|Finland|Denmark;Estonia;Poland|3
Russia|North Korea|South Korea;Japan;Vietnam|3
China|Afghanistan|Iran;Turkmenistan;Uzbekistan|4
India|Nepal|Iran;Thailand;Sri Lanka|2
Thailand|Cambodia|Vietnam;Indonesia;the Philippines|3
Vietnam|Laos|Thailand;Myanmar;Malaysia|3
Iran|Iraq|Saudi Arabia;Syria;Jordan|2
Turkey|Georgia|Russia;Ukraine;Jordan|3
Egypt|Sudan|Ethiopia;Chad;Tunisia|2
Israel|Jordan|Iraq;Saudi Arabia;Turkey|2
Saudi Arabia|Yemen|Iran;Syria;Egypt|2
Nigeria|Benin|Ghana;Togo;Mali|3
Kenya|Ethiopia|Rwanda;Zambia;Sudan|3
South Africa|Namibia|Zambia;Angola;Malawi|2
Zimbabwe|Zambia|Angola;Malawi;Tanzania|3
Morocco|Algeria|Libya;Tunisia;Mali|2
Brazil|every South American country except Chile and Ecuador|every South American country except Peru and Bolivia;every South American country except Uruguay and Paraguay;only five countries|4
Argentina|Chile|Peru;Ecuador;Colombia|1
Peru|Ecuador|Venezuela;Uruguay;Paraguay|3
Colombia|Panama|Costa Rica;Guyana;Bolivia|2
Mexico|Guatemala|Honduras;Nicaragua;Cuba|2
Portugal|only Spain|Spain and France;Spain and Andorra;Spain and Morocco|1
the Dominican Republic|Haiti|Cuba;Jamaica;Puerto Rico|2
Papua New Guinea|Indonesia|Australia;Malaysia;the Philippines|3
Malaysia|Brunei|Myanmar;Vietnam;the Philippines|4
Mongolia|only China and Russia|China and Kazakhstan;Russia and Kazakhstan;China, Russia and Kazakhstan|3`,
    qs: [{ q: 'Which country shares a land border with {country}?', a: 'n', wrong: 'w', when: r => !/^(every|only)/.test(r.n) && !/\?/.test(r.w) },
         { q: 'Which countries does {country} share a land border with?', a: 'n', wrong: 'w', when: r => /^(every|only)/.test(r.n) }]
  },
  {
    pack: 'ent-mascots', cat: 'ent', cols: ['mascot', 'brand', 'd'],
    rows: `
Ronald McDonald|McDonald's|1
Colonel Sanders|KFC|1
Tony the Tiger|Frosted Flakes (Frosties)|2
Bibendum, the Michelin Man|Michelin|2
Mr. Peanut|Planters|3
the Pillsbury Doughboy|Pillsbury|2
the Kool-Aid Man|Kool-Aid|2
the Gecko|GEICO|3
the Jolly Green Giant|Green Giant|3
Chester Cheetah|Cheetos|2
Toucan Sam|Froot Loops|2
Cornelius the rooster|Kellogg's Corn Flakes|3
the Quaker Oats man|Quaker Oats|3
Hello Kitty|Sanrio|3
Bertie Bassett|Liquorice Allsorts (Bassett's)|5
the Duracell Bunny|Duracell|2
the Energizer Bunny|Energizer|2
Smokey Bear|the US Forest Service|3
the Android robot ("Bugdroid")|Android|2
Clippy, the paperclip assistant|Microsoft Office|2
Duolingo's green owl|Duolingo|1
the Twitter bird, Larry|Twitter|3
the Aflac Duck|Aflac|4
Wenlock and Mandeville|the London 2012 Olympics|3
Bing Dwen Dwen, a panda in an ice suit|the Beijing 2022 Winter Olympics|3
the Phryges, red bonnet mascots|the Paris 2024 Olympics|3`,
    qs: [{ q: 'Which brand or event has the mascot {mascot}?', a: 'brand' }]
  }
];
