# Exportguide

## Grundregel
Export ska utgå från `docs/export-metadata.yaml` och kapitelordningen där.

## Före export
Kontrollera att:
- titel, undertitel, författare, språk, identifierare, datum och version finns i metadata
- `chapters/00-inledning.md` ligger först
- alla kapitel som anges i metadata finns
- markdown renderas till riktig formatering
- inga rubriker använder H4 eller lägre
- alla bildlänkar pekar på existerande filer

## EPUB
EPUB ska ha luftig layout och ingen innehållsförteckning som eget textkapitel.

## PDF
PDF ska ha innehållsförteckning före inledningen och sidbrytning före varje kapitel.

## DOCX
DOCX ska rendera rubriker, listor, fetstil, kursiv, tabeller och kodblock som riktig formatering.
