// Mythology fact tables (Arts & Literature).
module.exports = [
  {
    pack: 'art-gods', cat: 'art', cols: ['god', 'kind', 'of', 'pan', 'd', 'alt'],
    rows: `
Zeus|god|the sky and thunder, and king of the gods|Greek|1
Hera|goddess|marriage, and queen of the gods|Greek|2
Poseidon|god|the sea|Greek|1
Hades|god|the underworld|Greek|1
Athena|goddess|wisdom and strategy|Greek|2|Athene
Apollo|god|music, light and prophecy|Greek|2
Artemis|goddess|the hunt and the moon|Greek|2
Ares|god|war|Greek|2
Aphrodite|goddess|love and beauty|Greek|1
Hephaestus|god|fire and the forge|Greek|3
Hermes|god|messengers, travellers and thieves|Greek|2
Dionysus|god|wine and celebration|Greek|2
Demeter|goddess|the harvest|Greek|3
Hestia|goddess|the hearth and home|Greek|4
Persephone|goddess|spring, and queen of the underworld|Greek|3
Nike|goddess|victory|Greek|2
Nemesis|goddess|revenge|Greek|3
Hypnos|god|sleep|Greek|4
Morpheus|god|dreams|Greek|3
Pan|god|the wild and shepherds|Greek|3
Gaia|goddess|the Earth|Greek|3|Gaea
Asclepius|god|medicine|Greek|4
Tyche|goddess|luck and fortune|Greek|5
Iris|goddess|the rainbow|Greek|4
Jupiter|god|the sky, and king of the gods|Roman|2
Juno|goddess|marriage, and queen of the gods|Roman|3
Neptune|god|the sea|Roman|1
Pluto|god|the underworld|Roman|2
Minerva|goddess|wisdom|Roman|3
Mars|god|war|Roman|1
Venus|goddess|love and beauty|Roman|1
Vulcan|god|fire and the forge|Roman|2
Mercury|god|messengers and trade|Roman|2
Bacchus|god|wine|Roman|2
Ceres|goddess|the harvest|Roman|3
Vesta|goddess|the hearth|Roman|4
Diana|goddess|the hunt and the moon|Roman|3
Janus|god|beginnings and doorways, with two faces|Roman|3
Fortuna|goddess|luck|Roman|3
Aurora|goddess|the dawn|Roman|3
Odin|god|wisdom, and king of the gods|Norse|2|Woden;Wotan
Thor|god|thunder|Norse|1
Loki|god|mischief and trickery|Norse|1
Freyja|goddess|love, beauty and fertility|Norse|3|Freya
Frigg|goddess|marriage and motherhood, and queen of the gods|Norse|4|Frigga
Baldur|god|light and purity|Norse|4|Balder;Baldr
Tyr|god|war and justice, who lost a hand to a wolf|Norse|4|Týr
Heimdall|god|watchman, guarding the rainbow bridge Bifröst|Norse|4
Hel|goddess|the realm of the dead|Norse|3
Njord|god|the sea and wind|Norse|5|Njörd
Idun|goddess|youth, keeper of magic apples|Norse|5|Iðunn;Idunn
Ra|god|the sun|Egyptian|1|Re
Osiris|god|the afterlife and the dead|Egyptian|2
Isis|goddess|magic and motherhood|Egyptian|3
Horus|god|the sky, shown with a falcon's head|Egyptian|3
Anubis|god|embalming, shown with a jackal's head|Egyptian|2
Thoth|god|writing and wisdom, shown with an ibis head|Egyptian|4
Set|god|chaos, storms and the desert|Egyptian|4|Seth
Bastet|goddess|cats and the home|Egyptian|3|Bast
Sekhmet|goddess|war, shown as a lioness|Egyptian|4
Hathor|goddess|love, music and joy, often shown as a cow|Egyptian|4
Sobek|god|the Nile, shown as a crocodile|Egyptian|4
Ma'at|goddess|truth and justice|Egyptian|4|Maat
Amun|god|the hidden one, later king of the gods|Egyptian|4|Amun-Ra;Amon
Ganesha|god|new beginnings, with an elephant's head|Hindu|2|Ganesh
Shiva|god|destruction and transformation|Hindu|3
Vishnu|god|preservation|Hindu|3
Brahma|god|creation|Hindu|3
Lakshmi|goddess|wealth and good fortune|Hindu|3
Saraswati|goddess|knowledge, music and the arts|Hindu|4
Hanuman|god|strength and devotion, shown as a monkey|Hindu|3
Indra|god|storms, and king of heaven|Hindu|4
Surya|god|the sun|Hindu|4`,
    qs: [
      { q: 'In {pan} mythology, who is the {kind} of {of}?', a: 'god', group: o => o.pan + o.kind, alt: 'alt' },
      { q: 'In {pan} mythology, {god} is the {kind} of what?', a: 'of', group: 'pan', dAdd: 1 }
    ]
  },
  {
    pack: 'art-greek-roman', cat: 'art', cols: ['greek', 'roman', 'd'],
    rows: `
Zeus|Jupiter|2
Hera|Juno|3
Poseidon|Neptune|2
Hades|Pluto|2
Athena|Minerva|3
Ares|Mars|2
Aphrodite|Venus|2
Hephaestus|Vulcan|3
Hermes|Mercury|2
Dionysus|Bacchus|3
Demeter|Ceres|4
Hestia|Vesta|4
Artemis|Diana|3
Eros|Cupid|2
Persephone|Proserpina|4
Cronus|Saturn|4
Eos|Aurora|4
Nike|Victoria|4`,
    qs: [
      { q: 'What is the Roman name for the Greek god {greek}?', a: 'roman' },
      { q: 'The Roman deity {roman} matches which Greek deity?', a: 'greek', dAdd: 1 }
    ]
  },
  {
    pack: 'art-myth-creatures', cat: 'art', cols: ['desc', 'name', 'd', 'alt'],
    rows: `
the three-headed dog guarding the Greek underworld|Cerberus|2
the winged horse of Greek myth|Pegasus|1
the woman with snakes for hair whose gaze turns people to stone|Medusa|1
the half-man, half-bull monster in the Cretan labyrinth|Minotaur|1|The Minotaur
the many-headed serpent that grew two heads for each one cut off|Hydra|2|Lernaean Hydra
the half-man, half-horse creature|Centaur|1
the one-eyed giant blinded by Odysseus|Polyphemus|4
the race of one-eyed giants in Greek myth|Cyclopes|2|Cyclops
the bird that bursts into flame and is reborn from its ashes|Phoenix|1
the monster with a lion's body and a human head, who asked a famous riddle in Thebes|Sphinx|2
the creature with an eagle's head and wings and a lion's body|Griffin|2|Gryphon
the sea creatures whose songs lured sailors to their deaths|Sirens|2|Siren
the Norse world tree that links the nine worlds|Yggdrasil|4
the hall in Asgard where slain warriors feast|Valhalla|2
the giant wolf who will swallow Odin at Ragnarök|Fenrir|4
Thor's hammer|Mjölnir|3|Mjolnir
Odin's eight-legged horse|Sleipnir|4
the warrior maidens who choose the slain for Odin|Valkyries|3|Valkyrie
the Norse end of the world|Ragnarök|3|Ragnarok
the giant serpent that circles Midgard|Jörmungandr|5|Jormungandr;Midgard Serpent
the Greek hero who killed the Minotaur|Theseus|3
the Greek hero who performed twelve labours|Heracles|2|Hercules
the Greek hero who killed Medusa|Perseus|3
the hero whose only weak spot was his heel|Achilles|1
the king who turned everything he touched into gold|Midas|1|King Midas
the woman who opened a jar (later called a box) that released the world's evils|Pandora|1
the Titan who stole fire from the gods and gave it to humans|Prometheus|2
the Titan who holds up the sky|Atlas|2
the boy who flew too close to the sun on wings of wax|Icarus|1
the craftsman who built the labyrinth and wings of wax|Daedalus|3
the beautiful youth who fell in love with his own reflection|Narcissus|2
the musician who went to the underworld to bring back Eurydice|Orpheus|3
the hero who led the Argonauts to find the Golden Fleece|Jason|2
the hero of Homer's "Odyssey", who took ten years to get home|Odysseus|2|Ulysses
the Trojan prince who took Helen to Troy|Paris|3
the Trojan prophetess whom no one believed|Cassandra|3
the king condemned to roll a boulder uphill forever|Sisyphus|3
the man punished with water and fruit always just out of reach|Tantalus|4
the ferryman who carries souls across the River Styx|Charon|3
the river of forgetfulness in the Greek underworld|Lethe|4
King Arthur's sword, pulled from the stone or given by the Lady of the Lake|Excalibur|1
the wizard who advised King Arthur|Merlin|1
the knight who found the Holy Grail in many tellings|Galahad|4|Sir Galahad
the queen whose love for Lancelot helped bring down Camelot|Guinevere|3
Robin Hood's forest|Sherwood Forest|1|Sherwood
the legendary Swiss hero who shot an apple off his son's head|William Tell|2
the giant Irish hero who is said to have built the Giant's Causeway|Finn McCool|4|Fionn mac Cumhaill
the Japanese folk hero born from a peach|Momotarō|5|Momotaro
the Chinese Monkey King of "Journey to the West"|Sun Wukong|4`,
    qs: [{ q: 'In myth and legend, who or what is {desc}?', a: 'name', alt: 'alt' }]
  }
];
