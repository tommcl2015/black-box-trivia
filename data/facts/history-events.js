// Fact tables: awards, games, leaders. Each row is "key|value" or "key|value|difficulty".
module.exports = {
  bestPicture: `
1927|Wings|4
1934|It Happened One Night|5
1935|Mutiny on the Bounty|5
1937|The Life of Emile Zola|5
1938|You Can't Take It with You|5
1939|Gone with the Wind|3
1940|Rebecca|4
1941|How Green Was My Valley|5
1942|Mrs. Miniver|5
1943|Casablanca|3
1944|Going My Way|5
1945|The Lost Weekend|5
1946|The Best Years of Our Lives|5
1948|Hamlet|5
1949|All the King's Men|5
1950|All About Eve|4
1951|An American in Paris|4
1952|The Greatest Show on Earth|5
1953|From Here to Eternity|4
1954|On the Waterfront|4
1955|Marty|5
1956|Around the World in 80 Days|5
1957|The Bridge on the River Kwai|4
1958|Gigi|5
1959|Ben-Hur|3
1960|The Apartment|4
1961|West Side Story|3
1962|Lawrence of Arabia|4
1963|Tom Jones|5
1964|My Fair Lady|4
1965|The Sound of Music|3
1966|A Man for All Seasons|5
1967|In the Heat of the Night|4
1968|Oliver!|4
1969|Midnight Cowboy|4
1970|Patton|4
1971|The French Connection|4
1972|The Godfather|3
1973|The Sting|4
1974|The Godfather Part II|4
1975|One Flew Over the Cuckoo's Nest|4
1976|Rocky|3
1977|Annie Hall|4
1978|The Deer Hunter|4
1979|Kramer vs. Kramer|4
1980|Ordinary People|5
1981|Chariots of Fire|4
1982|Gandhi|4
1983|Terms of Endearment|4
1984|Amadeus|4
1985|Out of Africa|4
1986|Platoon|4
1987|The Last Emperor|4
1988|Rain Man|3
1989|Driving Miss Daisy|4
1990|Dances with Wolves|3
1991|The Silence of the Lambs|3
1992|Unforgiven|4
1993|Schindler's List|3
1994|Forrest Gump|2
1995|Braveheart|3
1996|The English Patient|4
1997|Titanic|2
1998|Shakespeare in Love|3
1999|American Beauty|3
2000|Gladiator|3
2001|A Beautiful Mind|3
2002|Chicago|3
2003|The Lord of the Rings: The Return of the King|3
2004|Million Dollar Baby|3
2005|Crash|4
2006|The Departed|3
2007|No Country for Old Men|3
2008|Slumdog Millionaire|3
2009|The Hurt Locker|3
2010|The King's Speech|3
2011|The Artist|3
2012|Argo|3
2013|12 Years a Slave|3
2014|Birdman|3
2015|Spotlight|4
2016|Moonlight|3
2017|The Shape of Water|3
2018|Green Book|3
2019|Parasite|3
2020|Nomadland|4
2021|CODA|4
2022|Everything Everywhere All at Once|3
2023|Oppenheimer|2
2024|Anora|3`,

  summerOlympics: `
1896|Athens|3
1900|Paris|4
1904|St. Louis|5
1908|London|5
1912|Stockholm|5
1920|Antwerp|5
1924|Paris|4
1928|Amsterdam|5
1932|Los Angeles|5
1936|Berlin|3
1948|London|4
1952|Helsinki|5
1956|Melbourne|5
1960|Rome|4
1964|Tokyo|4
1968|Mexico City|4
1972|Munich|3
1976|Montreal|2
1980|Moscow|3
1984|Los Angeles|3
1988|Seoul|3
1992|Barcelona|3
1996|Atlanta|2
2000|Sydney|2
2004|Athens|2
2008|Beijing|2
2012|London|2
2016|Rio de Janeiro|2
2024|Paris|1`,

  winterOlympics: `
1924|Chamonix|5
1928|St. Moritz|5
1932|Lake Placid|5
1936|Garmisch-Partenkirchen|5
1948|St. Moritz|5
1952|Oslo|5
1956|Cortina d'Ampezzo|5
1960|Squaw Valley|5
1964|Innsbruck|5
1968|Grenoble|5
1972|Sapporo|4
1976|Innsbruck|5
1980|Lake Placid|4
1984|Sarajevo|4
1988|Calgary|2
1992|Albertville|4
1994|Lillehammer|3
1998|Nagano|3
2002|Salt Lake City|3
2006|Turin|3
2010|Vancouver|1
2014|Sochi|2
2018|Pyeongchang|2
2022|Beijing|2`,

  // year|host|winner
  worldCup: `
1930|Uruguay|Uruguay
1934|Italy|Italy
1938|France|Italy
1950|Brazil|Uruguay
1954|Switzerland|West Germany
1958|Sweden|Brazil
1962|Chile|Brazil
1966|England|England
1970|Mexico|Brazil
1974|West Germany|West Germany
1978|Argentina|Argentina
1982|Spain|Italy
1986|Mexico|Argentina
1990|Italy|West Germany
1994|United States|Brazil
1998|France|France
2002|South Korea and Japan|Brazil
2006|Germany|Italy
2010|South Africa|Spain
2014|Brazil|Germany
2018|Russia|France
2022|Qatar|Argentina`,

  womensWorldCup: `
1991|United States
1995|Norway
1999|United States
2003|Germany
2007|Germany
2011|Japan
2015|United States
2019|United States
2023|Spain`,

  usPresidents: `
1|George Washington|1
2|John Adams|3
3|Thomas Jefferson|3
4|James Madison|4
5|James Monroe|4
6|John Quincy Adams|5
7|Andrew Jackson|4
8|Martin Van Buren|5
9|William Henry Harrison|5
10|John Tyler|5
11|James K. Polk|5
12|Zachary Taylor|5
13|Millard Fillmore|5
14|Franklin Pierce|5
15|James Buchanan|5
16|Abraham Lincoln|2
17|Andrew Johnson|4
18|Ulysses S. Grant|4
19|Rutherford B. Hayes|5
20|James A. Garfield|5
21|Chester A. Arthur|5
23|Benjamin Harrison|5
25|William McKinley|5
26|Theodore Roosevelt|4
27|William Howard Taft|5
28|Woodrow Wilson|4
29|Warren G. Harding|5
30|Calvin Coolidge|5
31|Herbert Hoover|5
32|Franklin D. Roosevelt|4
33|Harry S. Truman|4
34|Dwight D. Eisenhower|4
35|John F. Kennedy|3
36|Lyndon B. Johnson|4
37|Richard Nixon|4
38|Gerald Ford|4
39|Jimmy Carter|4
40|Ronald Reagan|3
41|George H. W. Bush|4
42|Bill Clinton|3
43|George W. Bush|3
44|Barack Obama|2
46|Joe Biden|2`,

  canadianPMs: `
1|John A. Macdonald|1
2|Alexander Mackenzie|4
3|John Abbott|5
4|John Thompson|5
5|Mackenzie Bowell|5
6|Charles Tupper|5
7|Wilfrid Laurier|4
8|Robert Borden|4
9|Arthur Meighen|5
10|William Lyon Mackenzie King|4
11|R. B. Bennett|5
12|Louis St. Laurent|5
13|John Diefenbaker|4
14|Lester B. Pearson|4
15|Pierre Trudeau|4
16|Joe Clark|4
17|John Turner|5
18|Brian Mulroney|4
19|Kim Campbell|4
20|Jean Chrétien|4
21|Paul Martin|4
22|Stephen Harper|3
23|Justin Trudeau|3
24|Mark Carney|3`
};
