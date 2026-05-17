# Kapitel 6: Bygg en enkel prototyp

## Varför detta kapitel finns

Nu har du en idé, en spelkärna och ett första regelutkast. Det är frestande att fortsätta tänka, skriva och förbättra på papper. Men ett brädspel blir inte verkligt förrän någon kan lägga komponenter på bordet och spela.

Det är här prototypen kommer in.

En prototyp är inte en snygg slutprodukt. Den är ett arbetsverktyg. Den hjälper dig upptäcka vad som faktiskt fungerar, vad som är otydligt och vad som bara lät bra i huvudet. I det här kapitlet bygger vi den första spelbara versionen av vårt exempelspel Skattkartan och du får samtidigt göra samma sak med ditt eget spel.

Målet är enkelt: efter kapitlet ska du ha något som går att spela, även om det är fult, skakigt och ofärdigt.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara vad en prototyp är och varför den ska vara enkel
- välja vilka komponenter som behövs för en första spelbar version
- skilja mellan nödvändiga och uppskjutna detaljer
- skapa en prototyp med papper, kort och markörer
- förbereda ditt spel för första testspelningen

## Innan vi börjar

I de tidigare kapitlen har vi byggt upp Skattkartan steg för steg.

Vi vet att spelet ska handla om äventyrare som utforskar en ö, samlar ledtrådar och försöker hitta skatten innan tiden tar slut. Vi har valt en enkel kärna: spelaren gör en handling per tur, kartan växer fram, och varje tur driver tiden framåt.

Vi har också ett första regelutkast. Det är tillräckligt för att börja bygga.

Det är viktigt att inte vänta på perfekta regler innan du gör prototypen. Reglerna blir bättre när de möter bordet.

## Vad en prototyp egentligen är

En prototyp är en enkel spelbar version av spelet.

Den behöver inte vara vacker. Den behöver inte vara balanserad. Den behöver inte innehålla alla framtida idéer.

Den behöver bara svara på en fråga:

> Går den här spelidén att spela på ett sätt som är intressant nog att fortsätta utveckla?

För ett första brädspel är det lätt att blanda ihop prototyp med slutversion. Du kanske vill välja typsnitt, rita omslag, hitta perfekta illustrationer och skriva snygga korttexter. Det är roligt, men det hjälper sällan den första testspelningen.

En bra första prototyp är:

- snabb att göra
- lätt att ändra
- tydlig nog att spela
- billig att kasta om idén behöver ändras

Tänk på prototypen som ett utkast i fysisk form.

## Börja med minsta spelbara version

När du bygger din första prototyp ska du inte fråga: “Vad kan spelet innehålla?”

Fråga i stället:

> Vad är det minsta som måste finnas för att vi ska kunna testa spelets kärna?

Det kallas ofta en minsta spelbar version. Det betyder inte att spelet är färdigt. Det betyder att spelet har precis tillräckligt många delar för att en testspelning ska kunna börja, fortsätta och ta slut.

För Skattkartan behöver vi testa:

- att spelarna kan utforska en karta
- att ledtrådar skapar framåtrörelse
- att faror skapar risk
- att tidsmätaren ger tempo
- att målet är begripligt

Det betyder att vi inte behöver:

- färdiga illustrationer
- avancerade karaktärer
- många olika föremål
- en lång bakgrundsberättelse
- perfekt balans mellan alla val

Den första prototypen ska skydda spelets kärna från att drunkna i detaljer.

## Komponenter för Skattkartans första prototyp

Vi kan bygga Skattkartan med mycket enkla material.

Första komponentlistan kan se ut så här:

| Komponent | Antal | Syfte |
|---|---:|---|
| Platsbrickor | 12 | Bygger kartan under spelets gång |
| Ledtrådskort | 16 | Ger spelarna framsteg mot skatten |
| Farokort | 10 | Skapar risk och osäkerhet |
| Spelarpjäser | 2–4 | Visar var spelarna befinner sig |
| Tidsmarkör | 1 | Visar hur många turer som återstår |
| Tidsbana | 1 | Begränsar spelets längd |
| Skattmarkör | 1 | Visar vem som hittat skatten |
| Regelblad | 1 | Gör spelet testbart utan muntlig förklaring |

Det här är inte en slutgiltig komponentlista. Det är en startpunkt.

Du kan göra platsbrickor av papperslappar. Ledtrådskort och farokort kan vara indexkort eller klippta pappersbitar. Spelarpjäser kan vara mynt, knappar eller lånade pjäser från ett annat spel.

Poängen är inte att imponera. Poängen är att spelet ska gå att testa.

## Gör platsbrickorna enkla

Eftersom Skattkartan är ett kartspel behöver vi platser. Men vi behöver inte rita en komplett karta i förväg.

I stället gör vi tolv platsbrickor som kan läggas ut när spelare utforskar ön.

En första uppsättning kan vara:

| Plats | Antal | Funktion |
|---|---:|---|
| Läger | 1 | Startplats och plats dit skatten ska återföras |
| Djungel | 3 | Vanlig plats utan specialregel |
| Ruin | 2 | Bra plats att söka ledtrådar på |
| Flod | 2 | Kan göra rörelse långsammare senare |
| Grotta | 2 | Farligare plats med större chans till fynd |
| Utkiksplats | 1 | Kan visa nästa plats eller ge information |
| Gömställe | 1 | Möjlig plats för skatten |

I första testet behöver varje plats inte ha unika regler. Det räcker att några platser känns olika. Om alla platser får specialregler direkt blir spelet svårare att testa.

En enkel första regel kan vara:

- Ruin och grotta gör sök-handlingen mer intressant.
- Flod och djungel är neutrala platser.
- Läger är start och mål.
- Gömställe kan användas när skatten avslöjas.

Det går att utveckla senare.

## Skapa kort som testar beslut, inte textmängd

Kort är praktiska i prototyper eftersom de är lätta att ändra.

Men skriv inte för mycket på varje kort. I första versionen ska korten testa spelbeslut, inte litterär stämning.

Ett ledtrådskort kan till exempel säga:

> Ledtråd: Du hittar ristningar som pekar mot den gamla ruinen. Behåll detta kort.

Ett farokort kan säga:

> Fara: Rasande regn. Om du inte vilar, förlora en ledtråd eller flytta tillbaka till föregående plats.

Det är tillräckligt för test. Senare kan texten bli snyggare.

För Skattkartan kan första kortlekarna se ut så här:

| Korttyp | Förslag |
|---|---|
| Ledtråd | 10 kort som ger en ledtråd |
| Tomt spår | 4 kort som inte ger något men inte skadar spelaren |
| Extra fynd | 2 kort som ger en liten bonus |
| Fara | 10 kort med enkla hinder eller kostnader |

Det viktiga är att korten skapar frågor under spel:

- Är det värt att söka här?
- Vågar jag fortsätta?
- Behöver jag vila?
- Har jag tillräckligt med tid?

## Bygg tidsmätaren tidigt

För spel som ska ta mindre än 30 minuter är tidsmätaren en av de viktigaste prototypdelarna.

Utan tidsbegränsning kan spelare ofta vandra runt tills någon till slut lyckas. Då blir det svårt att se om spelet har bra tempo.

Skattkartan kan börja med en enkel tidsbana på 20 steg.

Efter varje spelares tur flyttas tidsmarkören ett steg framåt. När markören når sista rutan tar spelet slut.

Det här är kanske inte perfekt. Det kan visa sig vara för kort eller för långt. Men det ger oss något konkret att testa.

En enkel tidsbana kan vara en rad rutor på ett papper:

1. Starta vid ruta 1.
2. Flytta fram ett steg efter varje tur.
3. När markören når ruta 20 slutar spelet.
4. Om ingen har återvänt med skatten vinner den spelare som har flest ledtrådar.

Detta gör att varje tur känns viktig.

## Skriv komponenterna direkt på prototypen

I tidiga prototyper är tydlighet viktigare än utseende.

Skriv gärna direkt på kort och brickor:

- “Ruin: +1 chans att hitta ledtråd”
- “Grotta: dra ett farokort när du söker”
- “Läger: lämna skatten här för att vinna”
- “Fara: tappa en ledtråd eller vila nästa tur”

Undvik små symboler om du inte samtidigt skriver vad de betyder. Symboler är användbara senare, men i första testet kan de skapa onödig förvirring.

Om du ändå vill använda symboler, håll dig till mycket få:

| Symbol | Betydelse |
|---|---|
| ? | Sök efter ledtråd |
| ! | Risk för fara |
| ⏳ | Tid påverkas |
| ★ | Viktig plats |

Men kom ihåg: symbolerna ska hjälpa spelaren, inte skapa ett nytt språk som måste läras in.

## Prototypens regelblad

Regelbladet behöver inte vara vackert. Det ska bara göra testet möjligt.

För Skattkartan kan första regelbladet innehålla:

1. En mening om spelet.
2. Komponentlista.
3. Förberedelser.
4. Turordning.
5. De tre handlingarna.
6. Hur ledtrådar fungerar.
7. Hur skatten hittas.
8. Hur spelet slutar.
9. Frågor designern vill undersöka.

Den sista punkten är viktig. Eftersom detta är en prototyp ska regelbladet inte bara hjälpa spelarna. Det ska också hjälpa dig som designer att lära dig rätt saker.

Exempel på testfrågor:

- Förstår spelarna vad de ska göra på sin tur?
- Känns valet mellan utforska, söka och vila meningsfullt?
- Tar spelet slut innan det blir segt?
- Känns tre ledtrådar lagom för att hitta skatten?
- Är farorna irriterande eller spännande?

## Gör en komponentkontroll före första testet

Innan du spelar bör du kontrollera att prototypen faktiskt går att starta och avsluta.

Använd den här checklistan:

- Finns alla komponenter som reglerna nämner?
- Är startplatsen tydlig?
- Vet spelarna hur de vinner?
- Vet spelarna vad de får göra på sin tur?
- Finns ett slutvillkor?
- Finns en lösning om tiden tar slut?
- Går korten eller brickorna att läsa från bordet?
- Är det lätt att ändra saker efter testet?

Om du svarar nej på något är det inte ett misslyckande. Det är precis därför checklistan finns.

## När prototypen ser för ful ut

Många nybörjare känner motstånd mot fula prototyper. Det kan kännas pinsamt att visa papperslappar, handskrivna kort och lånade pjäser.

Men en ful prototyp har en stor fördel: den gör det lättare att ändra spelet.

Om du har lagt fem timmar på att illustrera varje kort blir det svårare att ta bort ett kort som inte fungerar. Om kortet är en papperslapp tar det fem sekunder.

Första prototypens jobb är inte att visa hur bra du är på formgivning. Den ska visa om spelet har en levande kärna.

Snygghet kommer senare.

## Exempel: Skattkartan på bordet

Låt oss föreställa oss första uppställningen.

Mitt på bordet ligger lägret. Resten av platsbrickorna ligger i en dold hög. Varje spelare har en enkel pjäs på lägret. Ledtrådskorten och farokorten ligger i två separata högar. Bredvid dem ligger tidsbanan med markören på första rutan.

Första spelaren väljer att utforska. Hen drar en platsbricka och lägger den bredvid lägret. Det blir en ruin. Spelaren flyttar sin pjäs dit. Tidsmarkören går fram ett steg.

Nästa spelare går till ruinen och väljer att söka. Hen drar ett ledtrådskort och får sin första ledtråd. Tidsmarkören går fram igen.

Efter några turer finns flera platser på bordet. En spelare har två ledtrådar. En annan har råkat ut för en fara i grottan. Tiden börjar kännas knapp.

Det är inte säkert att allt fungerar. Kanske är ruinerna för starka. Kanske händer det för lite på djungelplatserna. Kanske går tiden för fort. Men nu har spelet börjat prata tillbaka.

Det är prototypens stora värde.

## Vanliga misstag

- **Misstag: Att göra prototypen för snygg för tidigt.**
  - Varför det händer: Det känns mer tillfredsställande att skapa något som ser färdigt ut.
  - Hur du undviker det: Bestäm att första versionen bara får använda enkla material och handskriven text.

- **Misstag: Att stoppa in alla idéer i första prototypen.**
  - Varför det händer: Varje idé känns viktig när spelet fortfarande är nytt.
  - Hur du undviker det: Skriv en separat lista med “senare idéer” och bygg bara det som behövs för att testa kärnan.

- **Misstag: Att sakna slutvillkor.**
  - Varför det händer: Designern fokuserar på vad spelarna gör, men glömmer när spelet ska vara över.
  - Hur du undviker det: Skriv alltid både vinstvillkor och reservslut innan första testet.

- **Misstag: Att inte kunna ändra komponenterna.**
  - Varför det händer: Kort och brickor görs för permanenta.
  - Hur du undviker det: Använd blyerts, lösa lappar, kortfickor eller tomma kort som kan skrivas om.


## Övningar

### Övning 1: Gör din komponentlista

Skriv en lista över alla komponenter ditt spel behöver för att kunna testas en gång.

Dela upp listan i tre kolumner:

| Måste finnas | Kan vänta | Osäker |
|---|---|---|
| Det som krävs för första testet | Sådant som kan läggas till senare | Sådant du inte vet ännu |

Var hård mot dig själv. Om något inte behövs för att testa spelets kärna, lägg det i “Kan vänta”.

### Övning 2: Bygg minsta spelbara version

Skapa en fysisk prototyp av ditt spel med enkla material.

Regel för övningen:

- använd inte mer än 60 minuter
- använd papper, kort, pennor eller lånade pjäser
- skriv hellre tydligt än snyggt
- gör det möjligt att ändra minst hälften av komponenterna efter test

När du är klar ska spelet kunna starta, spelas i några turer och ta slut.

### Övning 3: Skriv testfrågor

Skriv fem frågor du vill att första testet ska ge svar på.

Exempel:

1. Förstår spelarna målet?
2. Är turen lätt att genomföra?
3. Finns det ett val som känns för självklart?
4. Tar spelet ungefär rätt tid?
5. Vill spelarna spela en gång till?

Spara frågorna. De blir viktiga i nästa kapitel.

### Fördjupning: Gör två versioner av samma komponent

Välj en viktig komponent, till exempel ett kort, en bricka eller en resurs.

Gör två enkla versioner:

- en mycket enkel version
- en lite mer uttrycksfull version

Jämför vilken som är lättast att förstå vid bordet. I tidiga prototyper vinner ofta tydlighet över stämning.

## Snabb sammanfattning

- En prototyp är en enkel spelbar version, inte en färdig produkt.
- Första prototypen ska testa spelets kärna.
- Bygg minsta spelbara version innan du lägger till extra regler.
- Använd billiga och ändringsbara material.
- För korta spel är tidsmätare och slutvillkor särskilt viktiga.
- Skriv komponenter och regler så tydligt att andra kan prova spelet.
- Prototypens viktigaste uppgift är att hjälpa dig lära dig vad som fungerar.

## Quiz och reflektionsfrågor

1. Varför är det ofta bättre att göra en ful prototyp än en snygg prototyp i början?
2. Vad betyder minsta spelbara version?
3. Vilka komponenter behöver Skattkartan för att kunna testas första gången?
4. Varför är tidsmätaren viktig i ett spel som ska ta mindre än 30 minuter?
5. Vilka delar av ditt eget spel kan vänta till senare?
6. Vad vill du främst lära dig av din första testspelning?

## Nästa steg

Nu har spelet blivit spelbart. Nästa kapitel handlar om testspelning: hur du låter andra prova spelet, vad du ska titta efter och hur du samlar feedback utan att försvara varje designbeslut.

Det är då prototypen börjar göra sitt riktiga jobb.
