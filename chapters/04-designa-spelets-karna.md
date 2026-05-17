# Kapitel 4: Designa spelets kärna

## Varför detta kapitel finns

Nu har Skattkartan en tydlig spelidé: äventyrare letar efter en gömd skatt på en liten karta, samlar ledtrådar och tar risker innan tiden tar slut. Det är en bra början, men en idé blir inte spelbar förrän spelarna vet vad de gör på sin tur.

I det här kapitlet designar vi spelets kärna. Med kärna menar vi de regler som återkommer hela tiden: hur en tur går till, vilka handlingar spelaren kan välja, hur spelet närmar sig sitt mål och hur spelarna påverkar varandra.

Målet är inte att skriva alla regler. Målet är att skapa en första spelbar struktur.

## Lärandemål

Efter kapitlet ska du kunna:

- beskriva en enkel turordning för ett kort brädspel
- välja 2–4 huvudhandlingar som spelaren kan göra
- formulera ett tydligt målvillkor och ett tydligt slutvillkor
- skapa spelarinteraktion utan att göra reglerna för tunga
- göra en första kärnloop för ditt eget spel

## Innan vi börjar

I kapitel 3 skilde vi mellan tema, mekanik och scope. Nu tar vi nästa steg.

För Skattkartan har vi redan bestämt:

- Tema: skattjakt och äventyr
- Kärnmekanik: vägval på en liten karta
- Stödmekanik: push-your-luck vid farliga platser
- Scope: 2–4 spelare, cirka 20–30 minuter och ungefär 10–12 platser

Det betyder att vi inte behöver uppfinna allt från början. Vi behöver bara fråga: hur ser en vanlig tur ut?

## Spelets kärna är det som händer om och om igen

Ett spel kan ha många detaljer, men spelaren upplever främst det som upprepas.

I många korta spel finns en enkel rytm:

1. Spelaren får information.
2. Spelaren väljer en handling.
3. Spelet svarar på handlingen.
4. Nästa spelare tar vid.

Den rytmen kallas ibland för en kärnloop. Ordet loop betyder att något upprepas. I ett brädspel är kärnloopen den lilla cykel som spelarna gör flera gånger under spelet.

För Skattkartan kan en första kärnloop vara:

1. Välj en plats att gå till.
2. Dra ett kort eller avslöja vad som finns där.
3. Ta en belöning, risk eller ledtråd.
4. Flytta tidsmarkören ett steg.
5. Nästa spelare tar sin tur.

Det är inte elegant än, men det är testbart. Det räcker för att bygga vidare.

## Börja med turordningen

Turordningen svarar på frågan: när får spelaren göra något?

För ett första spel är det klokt att börja enkelt. Den enklaste varianten är medsols turordning:

> Spelarna turas om medsols. På sin tur gör spelaren en handling. När handlingen är klar går turen vidare till nästa spelare.

Det låter nästan för enkelt, men enkelhet är en styrka i ett första snabbspel. Spelarna behöver inte diskutera vem som får agera. Spelet rör sig framåt.

Andra turordningar finns, till exempel att snabbaste spelaren agerar först, att alla väljer samtidigt eller att spelarna bjuder om turordningen. Spara sådana varianter tills du vet varför du behöver dem.

För Skattkartan väljer vi:

| Beslut | Första version |
|---|---|
| Turordning | Medsols |
| Turens längd | En tydlig handling per tur |
| Startspelare | Den som senast höll i en karta, eller slumpmässigt |
| Runda | När alla spelare haft en tur |

Det här är inte slutgiltigt. Det är ett arbetsbeslut.

## Välj få huvudhandlingar

En huvudhandling är något spelaren får göra på sin tur. I första prototypen bör antalet vara lågt. Två till fyra handlingar räcker ofta.

Om spelaren får för många alternativ blir spelet långsamt innan det ens har börjat. Om spelaren får för få alternativ kan spelet kännas automatiskt.

För Skattkartan kan vi börja med tre huvudhandlingar:

| Handling | Vad spelaren gör | Varför den finns |
|---|---|---|
| Utforska | Flytta till en angränsande okänd plats och avslöja den | Driver kartan framåt |
| Sök | Försök hitta en ledtråd på nuvarande plats | Driver målet framåt |
| Vila | Undvik risk eller återhämta en enkel resurs | Ger spelaren ett säkrare val |

Tre handlingar ger val utan att skapa regeltyngd. Spelaren frågar sig:

- Ska jag röra mig vidare?
- Ska jag stanna och leta?
- Ska jag spela säkert?

Det är redan en liten designmotor.

## Gör målet konkret

Ett mål måste vara lätt att förstå vid bordet. “Få mest äventyrspoäng” kan fungera, men för ett första spel är ett mer konkret mål ofta bättre.

För Skattkartan väljer vi:

> Hitta skatten och återvänd till lägret innan tiden tar slut.

Det målet har tre viktiga delar:

| Del | Funktion |
|---|---|
| Hitta skatten | Ger riktning |
| Återvänd till lägret | Skapar ett avslutande vägval |
| Innan tiden tar slut | Skapar tempo och press |

Målet gör att spelaren inte bara springer runt på kartan. Varje tur behöver föra spelaren närmare ledtrådar, skatt eller läger.

## Bestäm hur spelet slutar

Ett spel behöver ett slutvillkor. Det är regeln som säger när spelet är över.

För korta spel är slutvillkoret extra viktigt. Utan tydligt slut riskerar spelet att dra ut på tiden.

Skattkartan kan ha två slutvillkor:

1. En spelare hittar skatten och återvänder till lägret.
2. Tidsmarkören når sista rutan.

Det första slutvillkoret ger spelarna hopp. Det andra ser till att spelet inte blir för långt.

Nu behöver vi också veta vem som vinner.

Första version:

- Om en spelare återvänder till lägret med skatten vinner den spelaren.
- Om tiden tar slut vinner den spelare som har flest ledtrådar.
- Vid lika antal ledtrådar vinner den spelare som är närmast lägret.

Det här är inte nödvändigtvis perfekt. Men det är tillräckligt tydligt för att testas.

## Skapa interaktion utan att bromsa spelet

Spelarinteraktion betyder att spelarnas beslut påverkar varandra. I korta spel behöver interaktion ofta vara snabb och lätt att förstå.

Det finns flera enkla sätt att skapa interaktion:

| Typ av interaktion | Exempel | Risk |
|---|---|---|
| Tävlan om samma mål | Flera spelare vill hitta samma skatt | Kan bli för slumpigt om en spelare har tur |
| Begränsade platser | Bara en spelare får stå på en plats | Kan skapa blockering |
| Delad information | Alla ser vilka platser som avslöjats | Kan göra val mer taktiska |
| Gemensam tidsmätare | Alla påverkas av samma tidspress | Kan kännas orättvist om vissa drabbas mer |

För Skattkartan börjar vi med mild interaktion:

- Spelarna tävlar om samma skatt.
- Avslöjade platser ligger kvar så alla kan använda informationen.
- En plats kan ha högst en spelare åt gången, men lägret är undantag.
- Tiden är gemensam och rör sig framåt efter varje tur.

Det gör att spelarna påverkar varandra utan att spelet blir elakt eller långsamt.

## Exempel: Skattkartans första kärna

Nu kan vi skriva en första version av spelets kärna.

### Arbetsversion

Skattkartan spelas av 2–4 spelare. Spelarna börjar i lägret. På sin tur väljer spelaren en av tre handlingar: utforska, söka eller vila. Efter handlingen flyttas tidsmarkören ett steg. Sedan går turen vidare medsols.

Målet är att hitta skatten och återvända till lägret innan tiden tar slut. Om tiden tar slut vinner spelaren med flest ledtrådar. Avslöjade platser ligger kvar på kartan och kan användas av alla spelare.

Det här är fortfarande ett utkast. Det saknar många detaljer:

- Hur hittar man ledtrådar?
- Hur vet man var skatten finns?
- Vad händer vid farliga platser?
- Hur många steg har tidsmarkören?
- Vad betyder vila?

Men kärnan är på plats. Vi vet vad spelaren gör på sin tur, vad spelet handlar om och hur spelet kan ta slut.

## Gör inte kärnan för smart

Det är lockande att lägga till specialregler direkt.

Kanske vill du ha olika äventyrare, utrustningskort, hemliga kartbitar, fällor, monster, väder, förbannelser och lagspel. Allt det kan vara roligt. Men i första prototypen är frågan inte “vad vore häftigt?”. Frågan är:

> Vilken minsta version kan visa om spelets grundidé fungerar?

En stark kärna är enkel nog att testas, men intressant nog att skapa val.

Om kärnan fungerar kan du lägga till mer senare. Om kärnan inte fungerar hjälper sällan fler regler.

## Vanliga misstag

- **För många handlingar från början.**
  - Varför det händer: Du vill ge spelaren frihet.
  - Hur du undviker det: Börja med 2–4 handlingar och lägg resten i en “senare”-lista.

- **Otydligt mål.**
  - Varför det händer: Temat känns tydligt i ditt huvud.
  - Hur du undviker det: Skriv målet som en konkret mening som en ny spelare kan upprepa.

- **Inget säkert slut.**
  - Varför det händer: Du tänker att spelet slutar när någon vinner.
  - Hur du undviker det: Lägg till ett slutvillkor som stoppar spelet efter en viss tid, runda eller resurs.

- **Interaktion som bara stör.**
  - Varför det händer: Du vill att spelarna ska påverka varandra.
  - Hur du undviker det: Börja med mild interaktion som delad information, gemensamma mål eller begränsade resurser.

- **Kärnan försöker lösa allt.**
  - Varför det händer: Du vill bygga hela spelet direkt.
  - Hur du undviker det: Skriv bara turordning, handlingar, mål och slutvillkor i första versionen.

## Miniövningar längs vägen

### Miniövning: skriv en turrunda

Beskriv en spelares tur i fyra korta steg. Använd verb som går att göra vid bordet, till exempel dra, välj, flytta, byt, avslöja eller betala.

Om du behöver fler än fyra steg, markera vilka som kan vänta till en senare version.

### Miniövning: kontrollera målet

Skriv spelets mål på en rad. Testa sedan om målet svarar på tre frågor:

1. Vad försöker spelaren uppnå?
2. Hur märker spelaren att målet är nära?
3. Vad händer när någon lyckas?

Om någon fråga saknar svar är målet fortfarande för otydligt.

## Övningar

### Övning 1: Skriv din kärnloop

Fyll i stegen för ditt eget spel:

1. Spelaren får eller ser:
2. Spelaren väljer:
3. Spelet svarar genom att:
4. Något i spelets läge förändras:
5. Turen går vidare genom att:

Skriv sedan kärnloopen som en kort lista med 4–6 steg.

### Övning 2: Välj huvudhandlingar

Skriv 2–4 handlingar som spelaren kan göra på sin tur.

| Handling | Vad spelaren gör | Varför handlingen finns |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

Stryk en handling om listan känns svår att förklara.

### Övning 3: Mål och slut

Svara på tre frågor:

1. Vad försöker spelaren uppnå?
2. När slutar spelet?
3. Hur avgörs vinnaren om huvudmålet inte uppnås?

Skriv svaren så att en ny spelare kan förstå dem utan bakgrundskunskap.

### Fördjupning

Gör två versioner av samma kärna:

- en tävlingsversion där spelarna försöker vinna var för sig
- en samarbetsversion där spelarna försöker vinna tillsammans

Jämför vilka regler som måste ändras.

## Snabb sammanfattning

- Spelets kärna är de regler och val som upprepas under spelet.
- En enkel turordning är ofta bäst i första prototypen.
- Två till fyra huvudhandlingar räcker långt.
- Målet behöver vara konkret och lätt att upprepa.
- Ett tydligt slutvillkor skyddar korta spel från att bli för långa.
- Spelarinteraktion kan vara mild och ändå skapa spänning.
- Första kärnan ska vara testbar, inte komplett.

## Quiz/reflektionsfrågor

1. Vad är en kärnloop?
2. Varför är det ofta bättre att börja med få handlingar?
3. Vad är skillnaden mellan mål och slutvillkor?
4. Vilken typ av interaktion passar bäst för ditt eget spel?
5. Vilken regel i din kärna är mest osäker och bör testas först?

## Nästa steg

Nu har spelet en första kärna. I nästa kapitel ska vi göra kärnan begriplig för andra människor genom att skriva regler som går att läsa, följa och testa.
