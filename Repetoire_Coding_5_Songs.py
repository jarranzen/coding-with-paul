import random

songs = ["Old MacDonald",
"Little Peter Rabbit",
"BINGO",
"Kookaburra",
"Five little ducks",
"Galoomph went the little green frog",
"Mister frog",
"Three little speckled frogs",
"Baa baa black sheep",
"The teddy bears picnic",
"Give me a home among the gum trees",
"The play school theme song",
"Row, row, row your boat",
"Frere Jaques",
"The wheels on the bus",
"I am a fine musician",
"Oh we can play on the big bass drum",
"Incy wincy spider",
"Three cheeky monkeys",
"Bananas in pyjamas",
"Dingle dangle scarecrow",
"Open, shut them",
"I’m a little teapot",
"The hokey pokey",
"Heads and shoulders knees and toes",
"If you’re happy and you know it",
"Shake my sillies out",
"London bridge is falling down",
"Mary had a little lamb",
"Twinkle, twinkle little star",
"Humpty Dumpty",
"Hickory Dickory Dock",
"Hey diddle diddle",
"Dorothy - Wiggles",
"Rock-a-bye your bear - Wiggles",
"Point your fingers - Wiggles",
"Shake your Sillies out - Wiggles",
"Brahms lullaby",
"Puff the magic dragon",
"Jingle bells",
"Miss Polly had a dolly",
"There’s a Monster in my Garden",
"Santa Lucia (Italian)",
"Yalo Yalo (Greek)",
"O sole Mio (Italian)",
"Never on a Sunday (Greek)",
"De Zilverloot (Dutch)",
"The Happy Wanderer (German)",
"La Vie en Rose (French)",
"Reginella Campagnola (Italian)",
"Quizas Quizas Quizas (Spanish)",
"Shalom Chaverim (Hebrew)",
"Edelweiss (German/Austria)",
"Loch Lomond (Scottish)",
"9 to 5 – Dolly Parton",
"Annie’s Song – John Denver",
"Big Bad John – Jimmy Dean",
"Cold Cold Heart – Hank Williams",
"Country Roads - John Denver",
"Crazy – Willie Nelson/Patsy Cline",
"Folsom Prison Blues – Johnny Cash",
"The Gambler – Kenny Rogers",
"Ghost Riders in the Sky – Johnny Cash",
"Gold Mine in the Sky – Pat Boone",
"Hey Good Lookin’ – Hank Williams",
"I Can’t Stop Loving You – Ray Charles",
"If I Needed You - Townes Van Zandt",
"I Like Beer – Tom T Hall",
"I Walk the Line – Johnny Cash",
"Jackson – Johnny Cash",
"Jolene – Dolly Parton",
"Looking Forward – Slim Dusty",
"Luckenback Texas – Waylon Jennings",
"Me & Bobby Mcgee – Janis Jopin",
"On the Road Again – Willie Nelson",
"On the Wings of a Dove – Dolly Parton",
"One Day at a Time – Kris Kristofferson",
"Pamela Brown – Tom T Hall",
"The Pub with No Beer – Slim Dusty",
"Ring of Fire – Johnny Cash",
"Abide with Me – Traditional hymn",
"Accentuate the Positive",
"Ain’t She sweet?",
"Amazing Grace – Traditional hymn",
"As Time Goes By",
"Auld Lang Syne",
"Cruising down the River",
"Cheek to Cheek",
"Daisy Daisy",
"Danny Boy",
"Don’t’ Fence Me in",
"Fly me to the Moon",
"Galway Bay",
"Green Green Grass of Home",
"Greensleeves",
"Gundagai",
"I Wonder Who’s Kissing Her Now?",
"I’m Forever Blowing Bubbles",
"It’s a Long Way to Tipperary",
"Lily of Laguna",
"Lili Marlene",
"Lord is my Shepherd – hymn",
"Makin’ Whoopee",
"M’mosielle form Armentieres",
"Moon River",
"My Bonny",
"Nature Boy",
"Night and Day",
"Now is the Hour",
"Pack up Your Troubles",
"Somewhere over the rainbow",
"Summertime",
"Tea for Two",
"Waltzing Matilda",
"We’ll Meet Again",
"What a wonderful World",
"White Cliffs of Dover",
"You are My Sunshine",
"After the Goldrush – Neil Young",
"Ain’t no Sunshine – Bill Withers",
"All my loving – The Beatles",
"All shook up - Elvis",
"All along the watchtower – Bob Dylan",
"American Pie – Don McLean",
"Angel – Jimi Hendrix",
"April sun in Cuba - Dragon",
"As tears go by – Rolling Stones",
"Blue suede shoes - Elvis",
"Big Yellow taxi – Joni Mitchell",
"Both sides now – Joni Mitchell",
"The Boxer – Simon & Garfunkel",
"Blowin’ in the wind – Bob Dylan",
"Brown Eyed Girl – Van Morrison",
"Comfortably Numb – Pink Floyd",
"Dancing queen - ABBA",
"Dock of the bay – Otis Redding",
"Don’t be cruel – Elvis",
"Don’t let me down – The Beatles",
"Don’t Stop – Fleetwood Mac",
"Eagle rock – Daddy Cool",
"The Ghetto - Elvis",
"Good vibrations – Beach Boys",
"Hard day’s night – The Beatles",
"Helplessly hoping – Crosby, Still, Nash",
"Help – The Beatles",
"Here comes the sun – The Beatles",
"Honky tonk women – Rolling Stones",
"Hotel California – The Eagles",
"The House of the Rising Sun – Animals",
"I can hear music – Beach Boys",
"I can see clearly now – Johnny Nash",
"Imagine – John Lennon",
"Jailhouse rock - Elvis",
"Knockin’ on heaven’s door – Bob Dylan",
"Piano man – Billy Joel",
"Lady Madonna – The Beatles",
"Let it be – The Beatles"
"Light my fire – The Doors",
"Maggie May – Rod Stewart",
"Mama Mia - ABBA",
"Midnight special – Creedance Clearwater Revival",
"Moon shadow – Cat Stevens",
"No woman no cry – Bob Marley",
"Pretty woman – Roy Orbison",
"Proud Mary – Creedance Clearwater",
"Rave on – Buddy Holly",
"Riders on the storm – The Doors",
"Rocket man – Elton John",
"Satisfaction – Rolling Stones",
"Scarborough fair – Simon & Garfunkel",
"Shilo – Neil Diamond",
"Sweet Caroline – Neil Diamon",
"The sound of silence – Simon & Garfunkel",
"Space oddity – David Bowie",
"Stand by me – Ben E King",
"Take it easy – The Eagles",
"Ticket to ride – The Beatles",
"The times they are a changin’ – Bob Dylan",
"Vincent – Don McLean",
"When I’m 64 – The Beatles",
"Wild horses – Rolling Stones",
"Wish you were here – Pink Floyd",
"With a little help from my friends - Beatles",
"Wouldn’t it be nice? – Beach Boys",
"Yesterday – The Beatles",
"You’ve got a friend – Carol K",
"Alive – Pearl Jam",
"Angels – Robbie Williams",
"Another Lonely Day – Ben Harper",
"Better Be Home Soon – Crowded House",
"Before too Long – Paul Kelly",
"Brothers in Arms – Dire Straits",
"Cats in the Cradle – Harry Chapin",
"Choir Girl – Cold Chisel",
"Comfortably Numb – Pink Floyd",
"Down Under – Men at Work",
"Drops of Jupiter - Train",
"Dumb Things – Paul Kelly",
"End of the Line – Travelling Wilburies",
"Every Breath You Take – The Police",
"Good Riddance - Greenday",
"Hallelujah – Leonard Cohen",
"Handle with Care – Travelling Wilburys",
"How to Make Gravy – Paul Kelly",
"I Still Haven’t Found – U2",
"It’s a long way to the top - ACDC",
"Jack & Diane – John Mellencamp",
"Karma Chameleon – Boy George",
"Khe Sahn – Cold Chisel",
"Kokomo – Beach Boys",
"Lightning Crashes - Live",
"Look What You’ve Done - Jet",
"Mad World – Tear for Fears",
"Man In The Mirror – Michael Jackson",
"Opportunity – Pete Murray",
"My Happiness - Powderfinger",
"Never Tear Us Apart - INXS",
"Nothing Else Matters - Metallica",
"One – U2",
"Patience – Guns n Roses",
"Reckless – Australian Crawl",
"So Far Away – Dire Straits",
"Sweet Child O Mine – Guns n Roses",
"Tainted Love – Soft Cell",
"Tears in Heaven – Eric Clapton"]

def select_songs(songs):
    return random.sample(songs, 5)

selected_songs = select_songs(songs)
for song in selected_songs:
    print(song)