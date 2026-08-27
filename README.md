# Designa ditt eget brädspel

Projekt för läroboken **Designa ditt eget brädspel: Från idé till färdigt spel**.

Boken är en svensk, hobby-/entusiastisk nybörjarbok för vuxna som vill skapa sitt första korta brädspel. Fokus ligger på spel som kan spelas på under cirka 30 minuter.

## Struktur

- `docs/` innehåller bokspecifikation, kapitelplan, canon, terminologi, projektstatus och exportmetadata.
- `chapters/` innehåller inledning och kapitel.
- `exercises/` innehåller övningar separerade per kapitel vid behov.
- `examples/` innehåller exempelspel, scenarier och prototypmaterial.
- `assets/` innehåller omslag, bildpromptar och eventuella illustrationer.
- `exports/` är reserverad för EPUB/PDF/DOCX/Markdown-exporter.


## Senaste uppdatering

Kapitel 12, `chapters/12-nasta-steg-som-speldesigner.md`, har skapats tillsammans med övningar, bildprompt och uppdaterade projektdokument. Alla planerade kapitel finns nu i projektet.
## GitHub Actions och publicering

Projektet innehåller samma publiceringskoncept som Romanskaparen-referensen:

- `Validate` kör projektvalidering vid relevanta pull requests och push till `main`.
- `Build Preview` kan startas manuellt och skapar EPUB + PDF i ett gemensamt Actions-artifact.
- `Release` körs för taggar som matchar `v*` och publicerar EPUB + PDF som separata GitHub Release-assets.
- Pandoc är låst till version `3.1.11.1` för reproducerbara byggen.

Lokalt kan validering köras med `python3 scripts/validate_project.py .`. Med rätt Pandoc- och XeLaTeX-version installerad kan boken byggas med `python3 scripts/build_book.py --output-dir exports`.
