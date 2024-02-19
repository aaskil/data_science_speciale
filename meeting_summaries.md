## Fredag 16. feb - CMD

Christian vil gerne snakke om afhandling (krav)

    - Hvad virker / virker ikke
        - Alt vi laver skal være generaliserbart - vi må ikke bare køre fuldt virksomhedsprojekt.

        Strukturen:
        - Introduktion - motivation (hvorfor er det vigtigt at forske i det her)
        - Introducer casen (Skal være specifikt, gør det meget præcist hvad vi skriver om)
        - Related work (forklar state of the art) 
            - Stereo vision
            - Object detection
        - Teoretisk framework - hvad tager vi udgangspunkt
        - Data beskrivelse (setup)
        - Empirisk sektion - vi må tage alt vi vil og så tilpasse det til specifikke løsning. Hvordan hænger empiri og teori sammen. (Gælder github kode fra andre paper's fx
        - Resultatsektion (veldokumenteret), hvad betyder resultaterne (hvad for nogle metrics)

Mangler navn på den Huggingface Meta object detector model


## Torsdag 8. feb - Scape Technologies

Fokuser på at lave vores afstandsbedømmelse. Hovedfokus. Vi kan altid bygge oven på bagefter

Succeskriterier:
- Fuldstændig fjernelse af 3D scanner, så to stereo billeder vil være nok for at robotten vil kunne køre kun med dem.
- Afstandsbedømmelse ud fra dataset
- Objektgenkendelse 

dataindsamling
- Kalibrering med oprindelig pointcloud scanner
- Nemmest at ryste posen hver gang for pålidelig data
- Hvor præcist kan det være - hvad er tradeoff ved forskellige løsninger
    -  hvad er godt nok, følsomhed hvor præcis skal den være

individuelle spørgsmål:
- hvor meget kan vi, skal vi implementere. det er meget code på github fra forsknings artikler, og den er meget kompleks. så det er måske urealistisk at implementere det hele, men for lidt at bare bruge det?
