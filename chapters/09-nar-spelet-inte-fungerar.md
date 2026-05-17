# Kapitel 9: När spelet inte fungerar

## Varför detta kapitel finns

Förr eller senare händer det: spelet fungerar inte.

Det betyder inte att du har misslyckats. Det betyder att du har kommit till en av de viktigaste delarna av speldesign. Ett spel som inte fungerar ger dig information. Det visar var reglerna skaver, var spelarna tappar intresset och var din idé behöver bli tydligare.

Många första spel fastnar inte för att idén är dålig, utan för att designern försöker lösa fel problem. Man lägger till fler kort när spelet egentligen behöver färre val. Man skriver längre regler när problemet är att turen är otydlig. Man gör spelet svårare när det egentligen bara är långsamt.

Det här kapitlet hjälper dig att felsöka ditt spel utan panik. Vi ska titta på vanliga problem, hur du känner igen dem och hur du gör små, testbara ändringar.

## Lärandemål

Efter kapitlet ska du kunna:

- skilja mellan symptom och grundproblem i ett spel
- känna igen vanliga fel i första brädspelsprototyper
- välja en rimlig åtgärd utan att bygga om hela spelet
- skapa en enkel problemdiagnos efter ett playtest
- förbättra Skattkartan med riktade ändringar

## Innan vi börjar

I kapitel 7 testspelade vi och samlade observationer. I kapitel 8 arbetade vi med balans och tempo.

Nu går vi ett steg längre. Vi antar att något fortfarande känns fel. Kanske tar Skattkartan för lång tid. Kanske vet spelarna inte vad de ska göra. Kanske känns farokorten slumpmässiga och orättvisa. Kanske vinner samma typ av strategi varje gång.

När du hamnar där är det lockande att tänka: "Jag behöver bara en bättre idé." Ofta behöver du inte det. Du behöver förstå vilket problem spelet faktiskt har.

## Symptom och grundproblem

Ett symptom är det du märker vid bordet. Ett grundproblem är orsaken bakom symptomet.

Här är några exempel:

| Symptom | Möjligt grundproblem |
|---|---|
| Spelarna frågar hela tiden vad de får göra | Turalternativen är otydliga eller för många |
| Spelet känns segt | Varje tur ger för liten förändring |
| Ingen vågar ta risker | Belöningen är för låg eller straffet för hårt |
| Alla gör samma sak | Ett val är uppenbart bättre än alternativen |
| Spelarna skrattar men spelet tar för lång tid | Upplevelsen fungerar, men strukturen behöver kortas |
| Spelarna ser förvirrade ut | Regler, komponenter och mål säger olika saker |

Ett vanligt misstag är att lösa symptomet direkt. Om spelarna frågar mycket kan man vilja skriva fler regler. Men om problemet är att det finns fem nästan likadana handlingar kan en kortare regeltext och färre handlingar vara bättre.

## En enkel felsökningsmetod

När ett spel inte fungerar kan du använda fyra steg.

### Steg 1: Skriv vad som hände

Börja konkret. Skriv inte "spelet är dåligt". Skriv vad du såg.

Exempel:

- Två spelare glömde att de kunde vila.
- Alla valde att söka nästan varje tur.
- Ingen hann tillbaka till lägret.
- Farokorten stoppade spelet i flera rundor.
- En spelare väntade länge utan att kunna påverka något.

Bra felsökning börjar med beteenden, inte känslor.

### Steg 2: Fråga varför det hände

För varje observation, fråga: varför uppstod detta?

Om alla valde att söka kan det bero på att:

- söka ger för stor belöning
- utforska känns för farligt
- vila känns som bortkastad tid
- kartan redan är tillräckligt öppen
- spelarna inte förstod nyttan med andra handlingar

Du behöver inte hitta det perfekta svaret direkt. Men du behöver flera möjliga förklaringar.

### Steg 3: Välj ett problem att lösa

Ändra inte fem saker samtidigt. Välj ett problem som verkar påverka mycket.

Ett bra första problem är ofta ett av dessa:

- spelarna förstår inte vad de ska göra
- spelet tar för lång tid
- ett val dominerar allt
- spelet avgörs för mycket av slump
- spelarna har för lite att påverka

### Steg 4: Testa en liten ändring

Gör en ändring som är lätt att ångra.

Exempel:

- minska antalet farokort
- ge spelaren två tydliga handlingar i stället för tre
- höj belöningen för riskabla platser
- sänk tidsmarkören med två steg
- låt vila också ge en liten ledtråd

Skriv vad du ändrade och varför. Testa sedan igen.

## Vanliga problem i första spel

### För många idéer samtidigt

Det här är kanske det vanligaste problemet. Du vill ha karta, resurser, strid, hemliga roller, utrustning, uppdrag, väder, nivåer och specialförmågor. Varje del verkar rolig för sig. Tillsammans blir de för mycket.

För ett spel under 30 minuter behöver du vara hårdare.

Fråga:

- Behövs den här regeln för att spelets huvudidé ska fungera?
- Kan den vänta till en senare version?
- Skulle spelet bli tydligare om vi tog bort den?

För Skattkartan betyder det att vi fortfarande väntar med specialförmågor och strid. Kärnan är utforskning, ledtrådar, risk och tid.

### Spelet börjar för långsamt

Ett snabbspel behöver komma igång snabbt. Om de första fem minuterna mest handlar om att ställa upp komponenter, läsa kort eller göra val utan konsekvens tappar spelet fart.

Möjliga lösningar:

- börja med några platser redan synliga
- ge spelarna ett första mål direkt
- minska startförberedelserna
- låt första rundan vara mycket enkel
- flytta specialregler till senare i spelet

I Skattkartan kan du till exempel låta lägret och tre närliggande platser vara synliga från start. Då får spelarna genast vägval.

### Valen känns inte viktiga

Ett val känns viktigt när spelaren förstår alternativen och tror att beslutet kan påverka resultatet.

Om valen känns oviktiga kan det bero på att:

- utfallet är för slumpmässigt
- alla alternativ leder till nästan samma sak
- spelaren inte har tillräcklig information
- belöningen kommer för sent
- spelet ändå avgörs av ett annat system

För Skattkartan kan valet mellan utforska och söka bli svagt om spelaren inte ser skillnaden. Då behöver handlingarna få tydligare roller:

- Utforska öppnar nya platser.
- Söka ger ledtrådar.
- Vila minskar risk eller återhämtar resurser.

### Spelet straffar spelarna för hårt

Risk är roligt när spelaren känner att hen valde den. Risk är frustrerande när spelet bara säger "du förlorar en tur" utan att spelaren kunde påverka situationen.

Var försiktig med straff som tar bort spelarens nästa tur. I korta spel är väntan dyrt.

Bättre straff kan vara:

- förlora en ledtråd
- flytta tillbaka ett steg
- öka tidsmarkören
- behöva välja mellan två nackdelar
- ta en riskmarkör som kan hanteras senare

I Skattkartan kan ett farokort därför hellre säga "flytta tidsmarkören ett steg" än "stå över nästa tur".

### Spelet saknar riktning

Ibland är reglerna tydliga men spelarna vet ändå inte vad de bör försöka göra. Då saknas riktning.

Riktning kan skapas genom:

- ett tydligt huvudmål
- delmål
- synliga framsteg
- korta påminnelser på komponenterna
- en tydlig sluttrigger

Skattkartan har ett huvudmål: hitta skatten och återvänd till lägret. Men den kan behöva delmål:

- samla tre ledtrådar
- hitta tempelplatsen
- avslöja skattens plats
- återvänd innan tiden tar slut

Då ser spelarna hur nära de är.

## Exempel: Skattkartan fungerar inte

Efter ett test av Skattkartan ser anteckningarna ut så här:

- Spelet tog 42 minuter.
- Spelarna gillade äventyrskänslan.
- Flera glömde att vila fanns.
- Farokorten gjorde att två spelare tappade flera turer.
- En spelare sökte nästan varje runda och vann enkelt.
- Kartan kändes spännande i början men rörig i slutet.

Det här är inte ett misslyckande. Det är ett utmärkt testresultat.

### Diagnos

Vi kan dela upp problemen:

| Observation | Trolig diagnos |
|---|---|
| 42 minuter | För många rundor eller för lite framdrift per tur |
| Vila glöms bort | Handlingen är för svag eller otydlig |
| Farokort tar bort turer | Straff skapar väntan i stället för spänning |
| Söka är alltid bäst | Belöningen för söka är för stark |
| Kartan blir rörig | För många platser eller för lite struktur |

Nu väljer vi inte alla problem samtidigt. Vi väljer tre små ändringar som hänger ihop med tempo och val.

### Ändringspaket A: snabbare och tydligare

För nästa test gör vi detta:

1. Kartan börjar med tre synliga platser.
2. Farokort tar inte längre bort spelarens nästa tur.
3. Söka kan bara göras på platser med ledtrådssymbol.
4. Vila ger både skydd mot nästa fara och möjlighet att flytta ett steg.
5. Antalet platser minskas från 12 till 10.

Det här är fortfarande samma spel. Vi har inte lagt till ett nytt system. Vi har bara gjort kärnan tydligare.

### Vad vi testar nästa gång

Nästa test ska inte försöka besvara allt. Det ska besvara tre frågor:

- Tar spelet nu 20–30 minuter?
- Väljer spelarna olika handlingar?
- Känns faror spännande utan att skapa väntan?

Om svaret blir ja är spelet på rätt väg.

## När du ska ta bort i stället för att lägga till

När ett spel inte fungerar är den vanligaste impulsen att lägga till något.

- Spelet är otydligt: lägg till en regel.
- Spelet är långsamt: lägg till fler belöningar.
- Spelet är obalanserat: lägg till undantag.
- Spelet känns tomt: lägg till fler kort.

Ibland är det rätt. Men ofta blir spelet bättre av att ta bort.

Ta bort när:

- en regel bara används ibland
- spelarna ofta glömmer en handling
- en komponent inte skapar beslut
- ett kort kräver mycket text men lite spel
- ett system inte stödjer huvudidén

För Skattkartan kan vi fråga: behöver spelet verkligen både farokort, resursmarkörer, blockerade vägar och specialplatser i första versionen? Kanske räcker farokort och tidsmarkör.

## Tre bra frågor efter varje misslyckat test

När du känner att spelet inte fungerar, använd de här frågorna:

1. Vad var roligast trots problemen?
2. Vad skapade mest förvirring eller väntan?
3. Vilken enda ändring vill jag testa först?

Den första frågan är viktig. Den hindrar dig från att kasta bort det som faktiskt fungerar.

Om Skattkartans testare säger "det var kul när vi vågade gå in i templet trots att tiden nästan var slut", då finns spelets hjärta där. Skydda det. Förenkla runt det.

## Vanliga misstag

- **Misstag: Att ändra allt efter ett dåligt test.**
  - Varför det händer: Du vill snabbt rädda spelet.
  - Hur man undviker det: Välj ett huvudproblem och en liten ändring.

- **Misstag: Att lyssna för mycket på lösningsförslag.**
  - Varför det händer: Testare vill vara hjälpsamma.
  - Hur man undviker det: Lyssna först på vad de upplevde, inte exakt vilken regel de föreslår.

- **Misstag: Att behålla en regel för att du gillar idén.**
  - Varför det händer: Regeln känns kreativ eller personlig.
  - Hur man undviker det: Fråga om regeln hjälper spelet vid bordet.

- **Misstag: Att göra spelet mer komplext för att lösa otydlighet.**
  - Varför det händer: Mer förklaring känns som mer kontroll.
  - Hur man undviker det: Testa först att förenkla valet, komponenten eller turstrukturen.

- **Misstag: Att tro att ett dåligt test betyder att spelet är dåligt.**
  - Varför det händer: Playtest känns personligt.
  - Hur man undviker det: Se testet som information, inte dom.

## Övningar

### Övning 1: Gör en problemdiagnos

Titta på din senaste prototyp eller använd Skattkartan. Skriv fem observationer från ett tänkt eller verkligt test.

För varje observation, fyll i:

| Observation | Möjlig orsak | Första lilla ändring |
|---|---|---|
| | | |
| | | |
| | | |

Försök hålla ändringarna små.

### Övning 2: Ta bort en regel

Välj en regel, komponent eller handling i ditt spel.

Svara på frågorna:

1. Vad tillför den?
2. Vad händer om den tas bort?
3. Vilket problem skulle den kunna skapa?
4. Vill du behålla, förenkla eller ta bort den?

Gör gärna testet praktiskt: spela en kort runda utan regeln.

### Övning 3: Reparera Skattkartan

Anta att Skattkartan har tre problem:

- spelet tar 40 minuter
- söka är nästan alltid bästa handlingen
- farokort gör spelarna frustrerade

Föreslå högst tre ändringar. Skriv också vad du vill mäta i nästa test.

### Fördjupning

Skapa en "ändringslogg" för ditt spel.

Använd detta format:

| Version | Problem | Ändring | Vad ska testas? |
|---|---|---|---|
| 0.1 | | | |
| 0.2 | | | |

Det här gör att du kan se spelets utveckling och undvika att återinföra gamla problem.

## Snabb sammanfattning

- Ett spel som inte fungerar ger värdefull information.
- Skilj mellan symptom och grundproblem.
- Skriv vad som faktiskt hände vid bordet.
- Ändra inte allt på en gång.
- Förenkling är ofta starkare än nya regler.
- Skydda det som redan är roligt.
- Testa små ändringar och skriv varför du gör dem.

## Quiz och reflektionsfrågor

1. Vad är skillnaden mellan ett symptom och ett grundproblem?
2. Varför är det riskabelt att ändra fem saker efter ett playtest?
3. Nämn två tecken på att ett spel har för många idéer samtidigt.
4. Varför är det ofta bättre att undvika straff som gör att spelare tappar sin tur?
5. Vilken del av ditt spel skulle du kunna förenkla redan nu?
6. Vad verkar vara hjärtat i Skattkartan?

## Nästa steg

Nu har vi lärt oss hur man felsöker ett spel när det inte fungerar. Nästa kapitel handlar om tema, komponenter och presentation.

Där ska vi titta på hur spelets utseende, namn, kort, karta och symboler kan göra reglerna lättare att förstå och spelupplevelsen mer lockande.
