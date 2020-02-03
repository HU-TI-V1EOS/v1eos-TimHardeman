---
title: "EOS Practicum — Linux Scavengers Hunt"
keywords: [EOS]
---

# EOS Practicum — Linux Scavenger Hunt

Deze opdracht is individueel. Om de opdracht uit te voeren heb je een werkende Linux-installatie nodig. Er is een installatie-image beschikbaar voor een aangepaste versie van Lubuntu Linux, met daarin de meeste benodigdheden voor dit en volgende vakken. Het staat je vrij deze opdracht in een andere versie van Linux te doen, al kan je er daarbij tegenaan lopen dat dingen bij jou net anders werken. Als je de HU-image wilt gebruiken kun je deze installeren in een virtuele machine (in een later practicum zullen we gebruik maken van VirtualBox hiervoor), als multi-boot naast je bestaande Windows of Mac, of op een oude-maar-nog-werkende laptop - op oplopende volgorde van gemak.

## Benodigde bestanden
Gebruik het commando `cd ~/V1EOS-practica/scavenger_hunt` om in de mappen van dit practicum te komen. Van hieruit gebruik je het commando `./generate_clues.py "[HU-EMAIL]"` om de clues te genereren. Bijvoorbeeld:

    ./generate_clues.py "carmen.sandiego@student.hu.nl"

Je kunt nu met de eerste aanwijzing beginnen.

## Clue 1: The Hunt Begins

#### `man` ####

Het eerste commando dat we leren is `man`, kort voor manual. Als je `man [COMMAND]` typt krijg je een uitgebreide hulp-pagina (meestal een manpage genoemd) voor de meeste commando's. Door op `q` te drukken kom je weer terug in de shell.

#### `ls` ####

Het volgende commando is `ls` (list). Type `man ls` en lees de beschrijving. Type zodra je de manpage hebt gesloten het commando `ls`; de uitvoer ziet er ongeveer zo uit:

    clues generate_clues.py LICENSE.md next_clue.py README.md

Blauwe items zijn mappen, al het andere is een bestand. Als je wilt weten welke mappen en bestanden er in de huidige map zitten kun je `ls` gebruiken.

#### `cd` ####

Voordat we op jacht gaan hebben we nog twee dingen nodig. Om naar een andere map te gaan gebruiken we `cd` (change directory). Met `cd clues` kunnen we de map met aanwijzingen ingaan. Een map terug naar boven gaat met `cd ..` en je kunt altijd terug naar de beginmap van deze scanvenger hunt met `cd ~/V1EOS-practica/scavenger_hunt`. Als je de map `clues` bent binnengegaan en `ls` typt zie je dat er een hoop clue-mappen zijn. De meeste daarvan zijn afleiders, maar een aantal bevatten daadwerkelijke hints. Gebruik `cd` om naar de map `12345` in `clues` te gaan en type `ls`. In deze map is een bestand aanwezig, genaamde `clue`.

#### `cat` en `less` ####

Om een clue te lezen moeten we de inhoud van een bestand kunnen lezen. Hiervoor kunnen we de commando's `cat` en `less` gebruiken. `cat clue` print de gehele inhoud van het bestand op het scherm. `less clue` opent het bestand net als een manpage: we kunnen door het bestand scrollen en `q` gebruiken om `less` te verlaten.
De naam Less is afgeleid van het oudere programma More, waarbij je op `enter` moest drukken om meer te zien te krijgen. Less is More, en met met Less kan je ook terug naar boven scrollen.

Lees de clue en ga hier verder. Alle volgende aanwijzingen zitten in opvolgende clues verborgen. Schrijf op welke clues je gehad hebt, zodat je als je verdwaald bent terug kan gaan naar waar je wist dat je nog goed zat. Je kunt de clues ook naar een aparte map kopiëren of de inhoud in een tekstbestand zetten, als je wilt. Voor het kopiëren van bestanden kan je het commando `cp` gebruiken, raadpleeg de manpage als dit een goed idee lijkt. In een latere clue zullen we dit commando beter leren kennen.

## Attribution
This scavenger hunt is based on the work of [Christopher M. Retford](https://github.com/pushingice/scavenger-hunt). Used (and propagated) under the [MIT licence](LICENCE.md).
