// Science & nature fact tables.
module.exports = [
  {
    pack: 'sci-scientists', cat: 'sci', cols: ['who', 'what', 'd', 'alt'],
    rows: `
Isaac Newton|the laws of motion and universal gravitation|1|Newton
Albert Einstein|the theory of relativity and E = mc²|1|Einstein
Charles Darwin|the theory of evolution by natural selection|1|Darwin
Gregor Mendel|the laws of inheritance, found by breeding pea plants|3|Mendel
Galileo Galilei|discovering Jupiter's four largest moons with his telescope|2|Galileo
Johannes Kepler|the three laws of planetary motion|4|Kepler
Ernest Rutherford|discovering the atomic nucleus|3|Rutherford
James Chadwick|discovering the neutron|4|Chadwick
Niels Bohr|the model of electrons orbiting the nucleus in shells|3|Bohr
Antoine Lavoisier|showing that burning needs oxygen, and naming oxygen and hydrogen|4|Lavoisier
Robert Boyle|the law linking a gas's pressure and volume|4|Boyle
Michael Faraday|electromagnetic induction, the idea behind generators|3|Faraday
James Clerk Maxwell|the equations of electromagnetism|4|Maxwell
Louis Pasteur|germ theory and the first rabies vaccine|2|Pasteur
Rosalind Franklin|"Photo 51", the X-ray image that revealed DNA's shape|3|Franklin
James Watson and Francis Crick|describing DNA's double helix in 1953|2|Watson and Crick;Crick and Watson
Edwin Hubble|showing that the universe is expanding|3|Hubble
Stephen Hawking|predicting that black holes give off radiation|2|Hawking
Carl Linnaeus|the two-part Latin naming system for living things|3|Linnaeus
Alfred Wegener|the theory of continental drift|4|Wegener
Max Planck|founding quantum theory|3|Planck
Erwin Schrödinger|a thought experiment with a cat that is both alive and dead|3|Schrodinger;Schrödinger
Archimedes|the principle of buoyancy, supposedly discovered in his bath|2
Pythagoras|the theorem about the sides of right-angled triangles|1
William Harvey|showing how blood circulates around the body|4|Harvey
Robert Hooke|naming the "cell" after looking at cork through a microscope|4|Hooke
Antonie van Leeuwenhoek|first seeing bacteria, through microscopes he made himself|4|van Leeuwenhoek;Leeuwenhoek
Jane Goodall|discovering that wild chimpanzees make and use tools|2|Goodall
Rachel Carson|warning about pesticides in her book "Silent Spring"|3|Carson
Alessandro Volta|inventing the first electric battery|3|Volta
Georg Ohm|the law linking voltage, current and resistance|3|Ohm
Anders Celsius|a temperature scale with 100 degrees between freezing and boiling|2|Celsius
Lord Kelvin|the absolute temperature scale, starting at absolute zero|3|Kelvin;William Thomson
Dorothy Hodgkin|working out the structures of penicillin and vitamin B12|5|Hodgkin
Barbara McClintock|discovering "jumping genes"|5|McClintock
Katalin Karikó and Drew Weissman|the mRNA technology behind COVID-19 vaccines|4|Kariko and Weissman
Tu Youyou|discovering artemisinin, a malaria drug, from traditional Chinese medicine|5|Tu
Jennifer Doudna and Emmanuelle Charpentier|the CRISPR gene-editing tool|4|Doudna and Charpentier
Peter Higgs|predicting the particle that gives others mass|3|Higgs
Grace Hopper|creating one of the first compilers and popularizing the word "bug" for computer errors|4|Hopper
Edward Jenner|creating the first vaccine, using cowpox|3|Jenner
Nicolaus Copernicus|putting the Sun, not Earth, at the centre of the solar system|2|Copernicus
Marie Curie|discovering polonium and radium|2|Curie
Alexander Fleming|discovering penicillin|1|Fleming`,
    qs: [{ q: 'Which scientist is famous for {what}?', a: 'who', alt: 'alt' }]
  },
  {
    pack: 'sci-units', cat: 'sci', cols: ['what', 'unit', 'd'],
    rows: `
force|newton|2
energy|joule|2
power|watt|2
pressure|pascal|3
frequency|hertz|2
voltage|volt|1
electric charge|coulomb|3
temperature|kelvin|3
mass|kilogram|1
length|metre|1
time|second|1
amount of substance|mole|4
luminous intensity|candela|4
radioactivity|becquerel|5
magnetic flux density|tesla|4
capacitance|farad|5
electrical resistance|ohm|2
electric current|ampere|2`,
    qs: [
      { q: 'What is the SI unit of {what}?', a: 'unit' },
      { q: 'The {unit} is the SI unit of what?', a: 'what', unique: true }
    ]
  },
  {
    pack: 'sci-animal-groups', cat: 'sci', cols: ['animal', 'word', 'd'],
    rows: `
geese on the ground|gaggle|2
geese in flight|skein|5
fish|school|1
wolves|pack|1
bees|swarm|1
whales|pod|2
kangaroos|mob|3
zebras|dazzle|4
giraffes|tower|4
hippos|bloat|4
rhinos|crash|4
jellyfish|smack|4
ferrets|business|4
cats|clowder|4
ravens|unkindness|4
starlings|murmuration|3
larks|exaltation|5
baboons|troop|3
leopards|leap|4
cheetahs|coalition|4
hyenas|cackle|4
butterflies|kaleidoscope|4
toads|knot|5
frogs|army|4
crocodiles|bask|4
sharks|shiver|4
porcupines|prickle|4
foxes|skulk|4
badgers|cete|5
finches|charm|5
vultures feeding together|wake|4
gorillas|band|4
ants|colony|2`,
    qs: [{ q: 'What is a group of {animal} called?', a: 'word' }]
  },
  {
    pack: 'sci-baby-animals', cat: 'sci', cols: ['animal', 'baby', 'd'],
    rows: `
horse|foal|1
goat|kid|2
deer|fawn|2
goose|gosling|2
frog|tadpole|1
eagle|eaglet|2
seal|pup|2
turkey|poult|4
pigeon|squab|4
fish|fry|3
eel|elver|5
platypus|puggle|5
llama|cria|4
hawk|eyas|5
beaver|kit|4
oyster|spat|5
sheep|lamb|1
bear|cub|1
cow|calf|1
pig|piglet|1
duck|duckling|1
butterfly|caterpillar|1`,
    qs: [{ q: 'What is a baby {animal} called?', a: 'baby' }]
  },
  {
    pack: 'sci-animal-kinds', cat: 'sci', cols: ['animal', 'kind', 'd'],
    rows: `
a whale|Mammal|1
a dolphin|Mammal|1
a bat|Mammal|2
a platypus|Mammal|3
a penguin|Bird|1
an ostrich|Bird|1
a kiwi|Bird|2
a shark|Fish|1
a seahorse|Fish|3
an eel|Fish|3
a salamander|Amphibian|3
a newt|Amphibian|3
an axolotl|Amphibian|3
a toad|Amphibian|2
a tortoise|Reptile|2
a crocodile|Reptile|1
a Komodo dragon|Reptile|2
a spider|Arachnid|2
a scorpion|Arachnid|3
a tick|Arachnid|4
a crab|Crustacean|2
a lobster|Crustacean|2
a woodlouse|Crustacean|5
an octopus|Mollusc|3
a snail|Mollusc|2
a squid|Mollusc|3
a starfish|Echinoderm|4
a sea urchin|Echinoderm|4
a ladybird|Insect|2
a dragonfly|Insect|1`,
    qs: [{ q: 'What kind of animal is {animal}?', a: 'kind' }]
  },
  {
    pack: 'sci-acronyms', cat: 'sci', cols: ['abbr', 'full', 'd'],
    rows: `
CPU|Central Processing Unit|2
GPU|Graphics Processing Unit|3
RAM|Random Access Memory|2
USB|Universal Serial Bus|3
URL|Uniform Resource Locator|3
HTML|HyperText Markup Language|3
LED|Light-Emitting Diode|2
LCD|Liquid Crystal Display|3
SMS|Short Message Service|3
DVD|Digital Versatile Disc|3
ATM|Automated Teller Machine|2
PIN|Personal Identification Number|1
NASA|National Aeronautics and Space Administration|2
DNA|Deoxyribonucleic acid|2
MRI|Magnetic Resonance Imaging|3
CAPTCHA|Completely Automated Public Turing test to tell Computers and Humans Apart|5
VPN|Virtual Private Network|3
ISP|Internet Service Provider|3
JPEG|Joint Photographic Experts Group|4
GIF|Graphics Interchange Format|4
BIOS|Basic Input/Output System|4
SSD|Solid-State Drive|3
NFC|Near-Field Communication|4
QR, as in QR code|Quick Response|3
UFO|Unidentified Flying Object|1
SOS|Nothing — it was chosen because it is easy to send in Morse code|4`,
    qs: [{ q: 'What does "{abbr}" stand for?', a: 'full' }]
  },
  {
    pack: 'sci-phobias', cat: 'sci', cols: ['ph', 'fear', 'd'],
    rows: `
arachnophobia|Spiders|1
claustrophobia|Enclosed spaces|1
acrophobia|Heights|2
agoraphobia|Open or crowded places|3
aerophobia|Flying|3
ailurophobia|Cats|4
ophidiophobia|Snakes|4
nyctophobia|The dark|3
triskaidekaphobia|The number 13|3
trypophobia|Clusters of small holes|4
coulrophobia|Clowns|3
glossophobia|Public speaking|3
nomophobia|Being without your mobile phone|4
hippopotomonstrosesquippedaliophobia|Long words|3
mysophobia|Germs|4
astraphobia|Thunder and lightning|4
trypanophobia|Needles|4
ornithophobia|Birds|4
thalassophobia|The deep sea|4
haemophobia|Blood|4
arachibutyrophobia|Peanut butter sticking to the roof of your mouth|4`,
    qs: [{ q: 'What is {ph} the fear of?', a: 'fear' }]
  }
];
