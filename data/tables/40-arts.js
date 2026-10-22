// Arts & literature fact tables.
const roman = n => [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
  .reduce((s, [v, r]) => { while (n >= v) { s += r; n -= v; } return s; }, '');
const nums = [4, 9, 14, 19, 24, 40, 44, 49, 50, 90, 99, 100, 400, 500, 900, 1000, 1066, 1492, 1666, 1776, 1984, 2026];
const romanRows = nums.map(n => {
  const near = [n + 1, n - 1, n + 10, n - 10, n + 5, n + 100].filter(x => x > 0 && x !== n);
  const w = near.slice(0, 3);
  return [roman(n), n, n < 100 ? 2 : n < 1000 ? 3 : 4, w.join(';')].join('|');
}).join('\n');

module.exports = [
  {
    pack: 'art-classical', cat: 'art', cols: ['work', 'who', 'kind', 'd', 'alt'],
    rows: `
Don Giovanni|Wolfgang Amadeus Mozart|opera|3|Mozart
Eine kleine Nachtmusik|Wolfgang Amadeus Mozart|piece|3|Mozart
La Traviata|Giuseppe Verdi|opera|3|Verdi
Rigoletto|Giuseppe Verdi|opera|3|Verdi
Aida|Giuseppe Verdi|opera|3|Verdi
Nabucco|Giuseppe Verdi|opera|4|Verdi
La Bohème|Giacomo Puccini|opera|3|Puccini
Tosca|Giacomo Puccini|opera|3|Puccini
Madama Butterfly|Giacomo Puccini|opera|3|Puccini
Turandot, with the aria "Nessun dorma"|Giacomo Puccini|opera|3|Puccini
Carmen|Georges Bizet|opera|2|Bizet
The Pearl Fishers|Georges Bizet|opera|4|Bizet
William Tell|Gioachino Rossini|opera|3|Rossini
The Flying Dutchman|Richard Wagner|opera|4|Wagner
Ride of the Valkyries|Richard Wagner|piece|3|Wagner
Fidelio|Ludwig van Beethoven|opera|4|Beethoven
Eugene Onegin|Pyotr Ilyich Tchaikovsky|opera|4|Tchaikovsky
Porgy and Bess|George Gershwin|opera|3|Gershwin
Dido and Aeneas|Henry Purcell|opera|5|Purcell
Pagliacci|Ruggero Leoncavallo|opera|5|Leoncavallo
Der Rosenkavalier|Richard Strauss|opera|5
Peter Grimes|Benjamin Britten|opera|5|Britten
Boris Godunov|Modest Mussorgsky|opera|5|Mussorgsky
The Sleeping Beauty ballet|Pyotr Ilyich Tchaikovsky|ballet|3|Tchaikovsky
The Firebird|Igor Stravinsky|ballet|4|Stravinsky
Giselle|Adolphe Adam|ballet|5|Adam
the ballet "Romeo and Juliet"|Sergei Prokofiev|ballet|4|Prokofiev
Peter and the Wolf|Sergei Prokofiev|piece|3|Prokofiev
Boléro|Maurice Ravel|piece|3|Ravel
Coppélia|Léo Delibes|ballet|5|Delibes
Appalachian Spring|Aaron Copland|ballet|4|Copland
Messiah, with the "Hallelujah" chorus|George Frideric Handel|piece|2|Handel
Water Music|George Frideric Handel|piece|3|Handel
Clair de lune|Claude Debussy|piece|3|Debussy
Canon in D|Johann Pachelbel|piece|3|Pachelbel
the "New World" Symphony|Antonín Dvořák|piece|4|Dvorak;Dvořák
In the Hall of the Mountain King|Edvard Grieg|piece|3|Grieg
The Carnival of the Animals|Camille Saint-Saëns|piece|4|Saint-Saens;Saint-Saëns
Pictures at an Exhibition|Modest Mussorgsky|piece|4|Mussorgsky
Flight of the Bumblebee|Nikolai Rimsky-Korsakov|piece|3|Rimsky-Korsakov
Scheherazade|Nikolai Rimsky-Korsakov|piece|4|Rimsky-Korsakov
The Lark Ascending|Ralph Vaughan Williams|piece|4|Vaughan Williams
Gymnopédies|Erik Satie|piece|4|Satie
Pomp and Circumstance|Edward Elgar|piece|3|Elgar
the Enigma Variations|Edward Elgar|piece|4|Elgar
Toccata and Fugue in D minor|Johann Sebastian Bach|piece|3|Bach
Symphony No. 5, famous for its "da-da-da-dum" opening|Ludwig van Beethoven|piece|2|Beethoven
Also sprach Zarathustra, used in "2001: A Space Odyssey"|Richard Strauss|piece|4
Carmina Burana, with "O Fortuna"|Carl Orff|piece|3|Orff
the Radetzky March|Johann Strauss I|piece|5
The Sorcerer's Apprentice|Paul Dukas|piece|4|Dukas
Night on Bald Mountain|Modest Mussorgsky|piece|4|Mussorgsky
the Requiem left unfinished at his death in 1791|Wolfgang Amadeus Mozart|piece|3|Mozart
Hungarian Dances|Johannes Brahms|piece|4|Brahms`,
    qs: [{ q: 'Who composed {work}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-musicals', cat: 'art', cols: ['show', 'who', 'song', 'd'],
    rows: `
Cats|Andrew Lloyd Webber|Memory|2
The Phantom of the Opera|Andrew Lloyd Webber|The Music of the Night|2
Evita|Andrew Lloyd Webber|Don't Cry for Me Argentina|2
Jesus Christ Superstar|Andrew Lloyd Webber|I Don't Know How to Love Him|3
Joseph and the Amazing Technicolor Dreamcoat|Andrew Lloyd Webber|Any Dream Will Do|3
Les Misérables|Claude-Michel Schönberg|I Dreamed a Dream|2
Miss Saigon|Claude-Michel Schönberg|The Movie in My Mind|4
West Side Story|Leonard Bernstein|Maria|2
The Sound of Music|Rodgers and Hammerstein|Do-Re-Mi|1
Oklahoma!|Rodgers and Hammerstein|Oh, What a Beautiful Mornin'|3
The King and I|Rodgers and Hammerstein|Shall We Dance?|3
South Pacific|Rodgers and Hammerstein|Some Enchanted Evening|4
Carousel|Rodgers and Hammerstein|You'll Never Walk Alone|4
My Fair Lady|Lerner and Loewe|I Could Have Danced All Night|3
Cabaret|Kander and Ebb|Willkommen|3
Chicago|Kander and Ebb|All That Jazz|2
Hamilton|Lin-Manuel Miranda|My Shot|2
In the Heights|Lin-Manuel Miranda|96,000|4
Wicked|Stephen Schwartz|Defying Gravity|2
Sweeney Todd|Stephen Sondheim|The Worst Pies in London|3
Into the Woods|Stephen Sondheim|Agony|4
Rent|Jonathan Larson|Seasons of Love|3
Hair|Galt MacDermot|Aquarius|4
Grease|Jim Jacobs and Warren Casey|Summer Nights|2
Fiddler on the Roof|Jerry Bock|If I Were a Rich Man|3
Annie|Charles Strouse|Tomorrow|2
Guys and Dolls|Frank Loesser|Luck Be a Lady|3
Oliver!|Lionel Bart|Consider Yourself|3
Dear Evan Hansen|Pasek and Paul|Waving Through a Window|4
Six|Toby Marlow and Lucy Moss|Ex-Wives|4
Mamma Mia!|Benny Andersson and Björn Ulvaeus|Dancing Queen|2
The Book of Mormon|Trey Parker, Matt Stone and Robert Lopez|Hello!|4`,
    qs: [
      { q: 'Who wrote the music for the musical "{show}"?', a: 'who', dAdd: 1 },
      { q: 'Which musical features the song "{song}"?', a: 'show' }
    ]
  },
  {
    pack: 'art-architects', cat: 'art', cols: ['building', 'who', 'd', 'alt'],
    rows: `
the Sagrada Família in Barcelona|Antoni Gaudí|2|Gaudi;Gaudí
Park Güell in Barcelona|Antoni Gaudí|3|Gaudi;Gaudí
the Walt Disney Concert Hall in Los Angeles|Frank Gehry|4|Gehry
the "Dancing House" in Prague|Frank Gehry|5|Gehry
Fallingwater, a house built over a waterfall|Frank Lloyd Wright|3|Wright
the Sydney Opera House|Jørn Utzon|3|Utzon;Jorn Utzon
the Shard in London|Renzo Piano|4|Piano
the Centre Pompidou in Paris|Renzo Piano and Richard Rogers|4|Piano and Rogers;Rogers and Piano
London's "Gherkin" skyscraper|Norman Foster|4|Foster
the glass dome of Berlin's Reichstag|Norman Foster|4|Foster
St Paul's Cathedral in London|Christopher Wren|3|Wren
the dome of Florence Cathedral|Filippo Brunelleschi|4|Brunelleschi
Villa Savoye near Paris|Le Corbusier|4
the Barcelona Pavilion|Ludwig Mies van der Rohe|5|Mies van der Rohe;Mies
the Bauhaus school building in Dessau|Walter Gropius|4|Gropius
the Heydar Aliyev Center in Baku|Zaha Hadid|4|Hadid
the London Aquatics Centre for the 2012 Olympics|Zaha Hadid|4|Hadid
Beijing's "Bird's Nest" Olympic stadium|Herzog & de Meuron|5|Herzog and de Meuron
Habitat 67 in Montreal|Moshe Safdie|4|Safdie
Marina Bay Sands in Singapore|Moshe Safdie|4|Safdie
the Cathedral of Brasília|Oscar Niemeyer|4|Niemeyer
the Eiffel Tower|Gustave Eiffel|1|Eiffel
the Chrysler Building in New York|William Van Alen|5|Van Alen
the Palace of Westminster (rebuilt after an 1834 fire)|Charles Barry|5|Barry
the Brooklyn Bridge|John A. Roebling|4|Roebling;John Roebling
the Petronas Towers|César Pelli|5|Cesar Pelli;Pelli
the Gateway Arch in St. Louis|Eero Saarinen|4|Saarinen
the Jewish Museum in Berlin|Daniel Libeskind|4|Libeskind
the Hagia Sophia (in 537 AD)|Isidore of Miletus and Anthemius of Tralles|5`,
    qs: [{ q: 'Who designed {building}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-sculptors', cat: 'art', cols: ['work', 'who', 'd', 'alt'],
    rows: `
The Thinker|Auguste Rodin|2|Rodin
The Burghers of Calais|Auguste Rodin|4|Rodin
the marble Pietà in St. Peter's Basilica|Michelangelo|3
The Ecstasy of Saint Teresa|Gian Lorenzo Bernini|4|Bernini
Apollo and Daphne in the Galleria Borghese|Gian Lorenzo Bernini|4|Bernini
the bronze David, the first free-standing nude since antiquity|Donatello|4
Little Dancer Aged Fourteen|Edgar Degas|4|Degas
Balloon Dog|Jeff Koons|3|Koons
the Angel of the North|Antony Gormley|4|Gormley
Chicago's Cloud Gate, "The Bean"|Anish Kapoor|4|Kapoor
Maman, the giant spider|Louise Bourgeois|4|Bourgeois
Fountain, a signed urinal|Marcel Duchamp|3|Duchamp
Walking Man I|Alberto Giacometti|4|Giacometti
Perseus with the Head of Medusa in Florence|Benvenuto Cellini|5|Cellini
Rio's Christ the Redeemer statue|Paul Landowski|5|Landowski
the Statue of Liberty|Frédéric Auguste Bartholdi|3|Bartholdi
Mount Rushmore|Gutzon Borglum|4|Borglum
a shark preserved in a tank of formaldehyde|Damien Hirst|3|Hirst
For the Love of God, a diamond-covered skull|Damien Hirst|4|Hirst
the Infinity Mirror Rooms and polka-dot pumpkins|Yayoi Kusama|3|Kusama
the first hanging "mobile" sculptures|Alexander Calder|4|Calder`,
    qs: [{ q: 'Which artist created {work}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-books', cat: 'art', cols: ['book', 'who', 'from', 'd', 'alt'],
    rows: `
The Count of Monte Cristo|Alexandre Dumas|France|3|Dumas
The Three Musketeers|Alexandre Dumas|France|3|Dumas
The Hunchback of Notre-Dame|Victor Hugo|France|3|Hugo
Madame Bovary|Gustave Flaubert|France|4|Flaubert
In Search of Lost Time|Marcel Proust|France|4|Proust
The Stranger|Albert Camus|France|4|Camus
Candide|Voltaire|France|4
Around the World in Eighty Days|Jules Verne|France|2|Verne
Journey to the Centre of the Earth|Jules Verne|France|3|Verne
The Metamorphosis|Franz Kafka|Austria-Hungary|3|Kafka
The Trial|Franz Kafka|Austria-Hungary|4|Kafka
Siddhartha|Hermann Hesse|Germany|4|Hesse
Steppenwolf|Hermann Hesse|Germany|4|Hesse
All Quiet on the Western Front|Erich Maria Remarque|Germany|3|Remarque
The Neverending Story|Michael Ende|Germany|4|Ende
Perfume: The Story of a Murderer|Patrick Süskind|Germany|4|Suskind;Süskind
The Name of the Rose|Umberto Eco|Italy|4|Eco
The Adventures of Pinocchio|Carlo Collodi|Italy|3|Collodi
The Divine Comedy|Dante Alighieri|Italy|2|Dante
Doctor Zhivago|Boris Pasternak|Russia|4|Pasternak
The Master and Margarita|Mikhail Bulgakov|Russia|4|Bulgakov
Lolita|Vladimir Nabokov|Russia|4|Nabokov
One Day in the Life of Ivan Denisovich|Aleksandr Solzhenitsyn|Russia|4|Solzhenitsyn
Dead Souls|Nikolai Gogol|Russia|5|Gogol
Fathers and Sons|Ivan Turgenev|Russia|5|Turgenev
Love in the Time of Cholera|Gabriel García Márquez|Colombia|4|Garcia Marquez;Márquez
The House of the Spirits|Isabel Allende|Chile|4|Allende
Like Water for Chocolate|Laura Esquivel|Mexico|4|Esquivel
The Shadow of the Wind|Carlos Ruiz Zafón|Spain|4|Zafon;Zafón
Things Fall Apart|Chinua Achebe|Nigeria|3|Achebe
Half of a Yellow Sun|Chimamanda Ngozi Adichie|Nigeria|4|Adichie
The God of Small Things|Arundhati Roy|India|4|Roy
Midnight's Children|Salman Rushdie|India|3|Rushdie
The Kite Runner|Khaled Hosseini|Afghanistan|3|Hosseini
Norwegian Wood|Haruki Murakami|Japan|3|Murakami
Kafka on the Shore|Haruki Murakami|Japan|4|Murakami
The Tale of Genji|Murasaki Shikibu|Japan|4|Murasaki
The Girl with the Dragon Tattoo|Stieg Larsson|Sweden|3|Larsson
Pippi Longstocking|Astrid Lindgren|Sweden|3|Lindgren
Heidi|Johanna Spyri|Switzerland|4|Spyri
The Book Thief|Markus Zusak|Australia|3|Zusak
Life of Pi|Yann Martel|Canada|3|Martel
The Handmaid's Tale|Margaret Atwood|Canada|2|Atwood
Anne of Green Gables|L. M. Montgomery|Canada|2|Lucy Maud Montgomery;Montgomery
The English Patient|Michael Ondaatje|Canada|4|Ondaatje
Wolf Hall|Hilary Mantel|England|4|Mantel
Atonement|Ian McEwan|England|4|McEwan
The Remains of the Day|Kazuo Ishiguro|England|4|Ishiguro
Never Let Me Go|Kazuo Ishiguro|England|4|Ishiguro
Brideshead Revisited|Evelyn Waugh|England|4|Waugh
A Clockwork Orange|Anthony Burgess|England|3|Burgess
Rebecca|Daphne du Maurier|England|4|du Maurier
Wuthering Heights|Emily Brontë|England|2|Emily Bronte
Jane Eyre|Charlotte Brontë|England|2|Charlotte Bronte
Great Expectations|Charles Dickens|England|2|Dickens
Oliver Twist|Charles Dickens|England|1|Dickens
A Christmas Carol|Charles Dickens|England|1|Dickens
David Copperfield|Charles Dickens|England|2|Dickens
Treasure Island|Robert Louis Stevenson|Scotland|2|Stevenson
Kidnapped|Robert Louis Stevenson|Scotland|4|Stevenson
Dracula|Bram Stoker|Ireland|2|Stoker
Gulliver's Travels|Jonathan Swift|Ireland|3|Swift
The War of the Worlds|H. G. Wells|England|2|Wells
The Time Machine|H. G. Wells|England|3|Wells
Robinson Crusoe|Daniel Defoe|England|3|Defoe
Tess of the d'Urbervilles|Thomas Hardy|England|4|Hardy
The Jungle Book|Rudyard Kipling|England|2|Kipling
Peter Pan|J. M. Barrie|Scotland|2|Barrie
Alice's Adventures in Wonderland|Lewis Carroll|England|1|Carroll
The Wind in the Willows|Kenneth Grahame|Scotland|3|Grahame
Winnie-the-Pooh|A. A. Milne|England|2|Milne
Mary Poppins|P. L. Travers|Australia|3|Travers
Watership Down|Richard Adams|England|3|Adams
The Secret Garden|Frances Hodgson Burnett|England|3|Burnett
Little Women|Louisa May Alcott|United States|2|Alcott
Adventures of Huckleberry Finn|Mark Twain|United States|2|Twain
The Scarlet Letter|Nathaniel Hawthorne|United States|3|Hawthorne
The Grapes of Wrath|John Steinbeck|United States|3|Steinbeck
Of Mice and Men|John Steinbeck|United States|2|Steinbeck
The Old Man and the Sea|Ernest Hemingway|United States|2|Hemingway
For Whom the Bell Tolls|Ernest Hemingway|United States|3|Hemingway
Fahrenheit 451|Ray Bradbury|United States|3|Bradbury
Slaughterhouse-Five|Kurt Vonnegut|United States|3|Vonnegut
On the Road|Jack Kerouac|United States|3|Kerouac
Beloved|Toni Morrison|United States|3|Morrison
The Color Purple|Alice Walker|United States|3|Walker
Gone with the Wind|Margaret Mitchell|United States|3|Mitchell
The Road|Cormac McCarthy|United States|4|McCarthy
Charlotte's Web|E. B. White|United States|2|White
Percy Jackson & the Olympians|Rick Riordan|United States|2|Riordan
Diary of a Wimpy Kid|Jeff Kinney|United States|2|Kinney
His Dark Materials|Philip Pullman|England|3|Pullman
Matilda|Roald Dahl|Wales|1|Dahl
The Gruffalo|Julia Donaldson|England|2|Donaldson
Twilight|Stephenie Meyer|United States|2|Meyer
Gone Girl|Gillian Flynn|United States|3|Flynn
Cloud Atlas|David Mitchell|England|4`,
    qs: [{ q: 'Who wrote "{book}"?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-characters', cat: 'art', cols: ['who', 'book', 'd'],
    rows: `
Ebenezer Scrooge|A Christmas Carol|1
Heathcliff|Wuthering Heights|2
Mr. Rochester|Jane Eyre|3
Mr. Darcy|Pride and Prejudice|2
Elizabeth Bennet|Pride and Prejudice|2
Long John Silver|Treasure Island|2
Fagin|Oliver Twist|3
Miss Havisham|Great Expectations|3
Big Brother|Nineteen Eighty-Four|2
Napoleon the pig|Animal Farm|2
Lennie Small and George Milton|Of Mice and Men|3
Tom Joad|The Grapes of Wrath|4
Hester Prynne|The Scarlet Letter|4
Phileas Fogg|Around the World in Eighty Days|3
Quasimodo|The Hunchback of Notre-Dame|2
Edmond Dantès|The Count of Monte Cristo|4
d'Artagnan|The Three Musketeers|3
Gregor Samsa, who wakes up as an insect|The Metamorphosis|3
Bilbo Baggins|The Hobbit|1
Lyra Belacqua|His Dark Materials|4
Bella Swan|Twilight|2
Lisbeth Salander|The Girl with the Dragon Tattoo|3
Becky Sharp|Vanity Fair|4
Emma Woodhouse|Emma|4
Mowgli|The Jungle Book|1
Mr. Toad of Toad Hall|The Wind in the Willows|2
Hazel and Fiver the rabbits|Watership Down|3
Willy Wonka|Charlie and the Chocolate Factory|1
Lemuel Gulliver|Gulliver's Travels|3
Man Friday|Robinson Crusoe|3
Count Olaf|A Series of Unfortunate Events|3
Jo March|Little Women|2
Scarlett O'Hara|Gone with the Wind|2
Holly Golightly|Breakfast at Tiffany's|3
Yossarian|Catch-22|4
Billy Pilgrim|Slaughterhouse-Five|4
Meursault|The Stranger|5
Liesel Meminger|The Book Thief|4
Bastian Balthazar Bux|The Neverending Story|4
Dorothy Gale|The Wonderful Wizard of Oz|2
Mary Lennox|The Secret Garden|3
Tom Sawyer|The Adventures of Tom Sawyer|1
Ishmael|Moby-Dick|3
Jean Valjean|Les Misérables|3
Victor Frankenstein|Frankenstein|2
Jonathan Harker|Dracula|4
Dorian Gray|The Picture of Dorian Gray|2
Mrs. Danvers|Rebecca|4
Pip|Great Expectations|3`,
    qs: [{ q: 'In which book does {who} appear?', a: 'book' }]
  },
  {
    pack: 'art-poems', cat: 'art', cols: ['poem', 'who', 'd', 'alt'],
    rows: `
"The Raven" ("Quoth the Raven, 'Nevermore'")|Edgar Allan Poe|2|Poe
"Annabel Lee"|Edgar Allan Poe|4|Poe
"Ozymandias"|Percy Bysshe Shelley|4|Shelley
"The Road Not Taken"|Robert Frost|3|Frost
"Stopping by Woods on a Snowy Evening"|Robert Frost|3|Frost
"I Wandered Lonely as a Cloud" (the daffodils poem)|William Wordsworth|3|Wordsworth
"The Rime of the Ancient Mariner"|Samuel Taylor Coleridge|3|Coleridge
"Kubla Khan"|Samuel Taylor Coleridge|4|Coleridge
"Do Not Go Gentle into That Good Night"|Dylan Thomas|3|Thomas
"The Waste Land"|T. S. Eliot|4|Eliot
"Old Possum's Book of Practical Cats", which inspired "Cats"|T. S. Eliot|3|Eliot
"If—"|Rudyard Kipling|3|Kipling
"The Charge of the Light Brigade"|Alfred, Lord Tennyson|3|Tennyson
"Paradise Lost"|John Milton|3|Milton
"The Canterbury Tales"|Geoffrey Chaucer|2|Chaucer
"The Iliad" and "The Odyssey"|Homer|1
"The Aeneid"|Virgil|3
"Leaves of Grass"|Walt Whitman|4|Whitman
"In Flanders Fields"|John McCrae|3|McCrae
"Jabberwocky"|Lewis Carroll|3|Carroll
"The Owl and the Pussy-cat"|Edward Lear|3|Lear
"Ode to a Nightingale"|John Keats|4|Keats
"She Walks in Beauty"|Lord Byron|4|Byron
"Because I could not stop for Death"|Emily Dickinson|4|Dickinson
"Still I Rise"|Maya Angelou|3|Angelou
"The Tyger" ("Tyger Tyger, burning bright")|William Blake|3|Blake
"Dulce et Decorum Est"|Wilfred Owen|4|Owen
"A Visit from St. Nicholas" ("'Twas the night before Christmas")|Clement Clarke Moore|4|Clement Moore;Moore
"Auld Lang Syne"|Robert Burns|2|Burns
"To a Mouse"|Robert Burns|4|Burns
"Gitanjali"|Rabindranath Tagore|4|Tagore
"Twenty Love Poems and a Song of Despair"|Pablo Neruda|4|Neruda
"The Rubaiyat"|Omar Khayyam|4|Omar Khayyám
"Sonnet 18" ("Shall I compare thee to a summer's day?")|William Shakespeare|2|Shakespeare`,
    qs: [{ q: 'Who wrote {poem}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'art-movements', cat: 'art', cols: ['who', 'move', 'd'],
    rows: `
Claude Monet|Impressionism|2
Pierre-Auguste Renoir|Impressionism|3
Edgar Degas|Impressionism|3
Camille Pissarro|Impressionism|4
Paul Cézanne|Post-Impressionism|4
Paul Gauguin|Post-Impressionism|4
Georges Seurat|Pointillism|3
Pablo Picasso|Cubism|2
Georges Braque|Cubism|4
Salvador Dalí|Surrealism|2
René Magritte|Surrealism|3
Joan Miró|Surrealism|4
Andy Warhol|Pop art|2
Roy Lichtenstein|Pop art|3
Jackson Pollock|Abstract Expressionism|3
Mark Rothko|Abstract Expressionism|4
Henri Matisse|Fauvism|4
Gustav Klimt|Art Nouveau|4
Alphonse Mucha|Art Nouveau|4
Edvard Munch|Expressionism|4
Marcel Duchamp|Dada|4
Caravaggio|Baroque|4
J. M. W. Turner|Romanticism|4
Caspar David Friedrich|Romanticism|4
Dante Gabriel Rossetti|Pre-Raphaelite Brotherhood|4
Umberto Boccioni|Futurism|5
Sandro Botticelli|Renaissance|3
Banksy|Street art|2
Damien Hirst|Young British Artists|4`,
    qs: [{ q: 'Which art movement is {who} most associated with?', a: 'move' }]
  },
  {
    pack: 'art-phrases', cat: 'art', cols: ['phrase', 'mean', 'lang', 'd'],
    rows: `
carpe diem|Seize the day|Latin|2
et cetera|And the rest|Latin|2
per se|By itself|Latin|3
bona fide|In good faith|Latin|3
ad hoc|For this purpose|Latin|4
status quo|The existing state of affairs|Latin|3
quid pro quo|Something for something|Latin|3
in vino veritas|In wine, there is truth|Latin|3
tempus fugit|Time flies|Latin|3
mea culpa|My fault|Latin|3
caveat emptor|Let the buyer beware|Latin|3
e pluribus unum|Out of many, one|Latin|4
alma mater|Nourishing mother|Latin|4
déjà vu|Already seen|French|2
c'est la vie|That's life|French|1
bon appétit|Enjoy your meal|French|1
faux pas|False step|French|3
joie de vivre|Joy of living|French|2
je ne sais quoi|I don't know what|French|3
laissez-faire|Let them do|French|4
savoir-faire|Knowing how to do|French|4
coup d'état|Blow against the state|French|4
RSVP (répondez s'il vous plaît)|Please reply|French|2
bon voyage|Have a good trip|French|1
hasta la vista|Until we see each other again|Spanish|2
mañana|Tomorrow|Spanish|1
siesta|Afternoon nap|Spanish|1
aficionado|Enthusiast|Spanish|3
dolce vita|The sweet life|Italian|3
al dente|To the tooth|Italian|3
prima donna|First lady|Italian|3
ciao|Hello or goodbye|Italian|1
gesundheit|Health|German|2
kindergarten|Children's garden|German|2
wanderlust|Desire to travel|German|3
schadenfreude|Pleasure at someone else's bad luck|German|3
zeitgeist|Spirit of the time|German|3
doppelgänger|Double-goer, a look-alike|German|3
poltergeist|Noisy ghost|German|3
karaoke|Empty orchestra|Japanese|3
tsunami|Harbour wave|Japanese|4
sayonara|Goodbye|Japanese|1
arigatō|Thank you|Japanese|2
namaste|I bow to you|Sanskrit|3
aloha|Hello, goodbye and love|Hawaiian|2
smörgåsbord|Sandwich table|Swedish|4
hygge|Cosy contentment|Danish|3
ombudsman|Representative|Swedish|5`,
    qs: [{ q: 'What does the {lang} word or phrase "{phrase}" mean?', a: 'mean', group: 'lang' }]
  },
  {
    pack: 'art-roman-numerals', cat: 'art', cols: ['r', 'n', 'd', 'w'],
    rows: romanRows,
    qs: [{ q: 'What number is the Roman numeral {r}?', a: 'n', wrong: 'w' }]
  }
];
