---
title: "EOS Practicum — Gentoo"
keywords: [EOS]
---

# EOS Practicum — Gentoo

Deze opdracht is individueel. De opdracht is het installeren van een Gentoo Linux systeem. Tijdens de installatie houdt je een log bij wat je hebt gedaan, en waar je moeite mee had. Ook beantwoord je tijdens de installatie een aantal vragen. Het resultaat neem je door met de docent. Ook demonstreer je de werkende computer of VM (dit mag via SSH als je een vaste computer hebt gebruikt). **Let op: lees het gehele document goed door, en beantwoord alle vragen!**

## TL;DR
- Er is geen TL;DR! Lees de opdracht helemaal door en voer deze daarna uit. **Sla niets over, anders kan je mogelijk opnieuw beginnen!**
- Verslaglegging weegt zwaarder dan succes. Het is ok als niet alles gelukt is, zo lang je beschrijft wat er mis ging en wat je hieruit op kan maken.
- Vraag docenten en student-assistenten om hulp als je er niet uit komt.
- Sommige stappen duren *erg* lang; ga ondertussen iets anders doen.

## Over Gentoo

Gentoo is een Linux distributie die je geheel zelf op moet bouwen. Waar de meeste distributies een mooi installatie-script hebben, moet je voor de installatie van Gentoo zelf de command-line induiken en configuratiebestanden schrijven. Het voordeel hiervan is dat je een systeem hebt waarvan je zelf weet waar alles staat. Ook heb je veel controle over wat er wel en niet geïnstalleerd wordt.

Een ding om rekening mee te houden bij Gentoo is dat de distributie source-based is. Dit betekent dat alles tijdens de installatie (van het systeem, of van extra software) gecompileerd wordt. Bij de meeste distributies wordt een binary gedownload en op de juiste plek op je systeem gezet; dit duurt meestal enkele seconden. Bij Gentoo wordt de source-code gedownload, waarna het compilen nog de nodige tijd kan duren (enkele minuten tot zelf uren voor erg grote en complexe paketten). Hou hier rekening mee met de uitvoering van dit practicum: begin op tijd, en hou er rekening mee dat je soms even moet wachten voordat je verder kunt.

## Voordat we beginnen

Begin met het downloaden van de [Gentoo ISO](https://www.gentoo.org/downloads). Kies voor de minimal installation CD (AMD64, **niet** x86) en sla dit bestand op je laptop op. Voor de installatie mag je een fysieke of virtuele machine (VM) gebruiken; we raden af om hiervoor je Raspberry Pi te gebruiken. Als je een laptop of computer hebt **die je niet gebruikt** (dit mag best een oud systeem zijn, zolang je maar niets kapot kunt maken dat je nodig hebt) dan kun je deze gebruiken, anders raden we aan [VirtualBox](https://www.virtualbox.org) te downloaden. Dit heeft als extra voordeel dat je snapshots kan maken (een backup van je systeem op een bepaald moment) als je geavanceerde opties wilt proberen, zodat je niet opnieuw hoeft te beginnen als dit mislukt en je systeem onwerkbaar is geworden.

Maak een nieuwe virtuele machine aan. Gentoo heeft als je geen grafische omgeving installeert niet heel veel nodig, 
maar reserver wel een paar GiB RAM en 10-20 GiB schijfruimte. Als je bij het maken van de virtual harddisk kiest voor dynamically allocated gebruikt de virtuele hardeschijf niet meer (echte) hardeschijfruimte dan nodig is. Als je de VM de naam Gentoo geeft kiest VirtualBox doorgaans de juiste instellingen — als dit niet lukt kun je dit handmatig doen of simpelweg voor de meest recente algemene versie van Linux (64-bits) kiezen. Selecteer **bij de eerste keer opstarten van de VM** de gedownloadde Gentoo ISO als je om een "virtual optic disk" gevraagd wordt. Als je een fysieke machine wilt installeren moet je de ISO naar een CD, DVD of USB stick branden (dat laatste kan met Etcher, dat je ook met CSN gebruikt hebt).

Zodra je de minimal installation CD geboot hebt, kom je terecht in een Linux command line. Je bent ingelogd als root gebruiker en kunt in een map je nieuwe Linux-systeem opbouwen. Zodra alles op z'n plek staat kun je naar je nieuwe systeem switchen om de installatie voort te zetten. Als alles goed is gegaan kun je na de installatie direct in je nieuwe sytseem booten.

We volgen de instructies in het [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Booting). We gaan ervan uit dat je een 64-bits (Intel / AMD) computer of VM hebt, mocht dit anders zijn dan moet je [hier](https://wiki.gentoo.org/wiki/Handbook:Main_Page) het juiste handbook kiezen voor jouw processor-architectuur. **Kies altijd hetzelfde aantal bits voor je VM als voor de image die je download en de guide die je volgt!**

## Booten
Als je de stappen hierboven tot nu toe hebt gevolgd, kun je bij Sectie 5 (Booting) beginnen. Je zal doorgaans geen boot opties nodig hebben, dus tenzij je ergens tegenaan loopt kun je de lijst met opties overslaan en gewoon op enter drukken. De rest van deze sectie is optioneel, dus kijk of er iets voor jou van toepassing is en begin met het controlleren van de netwerkverbinding ([Sectie 6](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Automatic_network_detection)). Volg vanaf hier de installation guide, en noteer welke stappen je gedaan hebt, of hebt kunnen overslaan. Dit kan per installatie verschillen, omdat een en ander van je hardware afhankelijk is. Maak verder aantekeningen over wat je gedaan hebt (en hoe), en of er dingen onduidelijk waren.

## De harde schijf
Bij [Sectie 8](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Introduction_to_block_devices) ga je de (eventueel virtuele) harde schijf klaar maken voor de installatie. Je hebt de keuze uit twee technologiën voor de partition table: het oudere MBR en het nieuwere GPT. Zoek zelf uit wat de voornaamste verschillen zijn. We kiezen bij onze installatie voor het nieuwere GPT, tenzij je (bijvoorbeeld door je hardware) een goede reden hebt om MBR te gebruiken. Maak je partitietabel met `parted` of `fdisk` en beschrijf welke indeling je hebt gekozen, en welke software je hebt gebruikt. Beschrijf daarna per partitie hoe je deze hebt geformateerd (welk type filesystem heb je gekozen, en waarom?). Als je het interessant vindt mag je van de standaard indeling afwijken, of geavanceerde opties gebruiken zoals [Btrfs RAID, LVM](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Advanced_storage) of [Dm-crypt](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch_Simplified). Beschrijf je ervaring in je verslag. **Let erop dat je alles goed gemount hebt; zo niet krijg je op een gegeven moment errors over te weinig ruimte, en moet je vanaf dit punt opnieuw beginnen!**

## Het basissysteem
In de volgende stap downloaden we een Stage 3 tarball. **Volg de instructies in het Gentoo Handbook**, en kies voor **no-multilib** tenzij je weet wat je doet en echt ondersteuning voor 32-bits software nodig hebt op een systeem dat je wilt blijven gebruiken. Gebruik `links` om de Stage 3 tarball te downloaden met het adres dat in het Gentoo Handbook staat. Kies als je om een mirror wordt gevraagd de *Universiteit Twente (HTTP)* (vanaf de Gentoo download site) en dan `releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-nomultilib-20180826T214503Z.tar.xz` (of een recentere versie). Pak deze file uit met `tar xpJvf stage3-*.tar.xz --wildcards --xattrs-include='*.*' --numeric-owner` (in het handbook staat iets anders, dit is verouderd).

## Configuratie
Bij [Sectie 16](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Configuring_compile_options) ga je bezig met de configuratie. Beschrijf wat de verschillende flags in de `CFLAGS`, `CXXFLAGS` en `MAKEOPTS` betekenen, en welke jij gekozen hebt. Na de `chroot` ga je verder met configureren. We gebruiken in principe het `no-multilib` profiel; het is op dit moment nog niet nodig voor een desktop te kiezen (gnome, plasma, etc.). Let er ook op dat je een recente versie kiest. Je moet nu de `@world` set updaten, waarom kan dit nodig zijn?

Beschrijf bij het configureren van de `USE` variabele welke flags je gekozen hebt, en waarom.

Voor de kernel-configuratie kiezen we voor de handmatige optie. Doorloop de stappen en geef aan welke opties je gekozen hebt.

Gebruik `blkid` om de UUIDs van je partities te vinden, en [gebruik deze](https://wiki.gentoo.org/wiki/Fstab#UUIDs_and_labels) om je `/etc/fstab` te vullen.

Bij het configureren van je netwerk gebruik je het commando `rc-update` om het netwerk tijdens het booten beschikbaar te maken. Zoek op wat `rc-update` doet en wat init-scripts zijn.

## Paketten
Vervolgens is het tijd om wat tools te installeren: een system logger, een cron daemon en een file indexer. Hoewel deze optioneel zijn, is het wel aan te bevelen deze te installeren. Je kan het proces iets versnellen door de verschillende paketten (`app-admin/sysklogd`, `sys-process/cronie`, ...) achter één `emerge --ask` te zetten. Zoek ondertussen op wat deze drie tools doen en beschrijf dat in je log. De genoemde paketten zijn de default-keuzes voor Gentoo, maar zeker niet de enige opties. Zoek voor elke tool een alternatief en kijk wat de verschillen zijn.

## Booten (revisited)
De laatste grote stap van de guide is het bootbaar maken van je systeem. Bekijk de verschillende opties (doe zelf een beetje onderzoek) en kies je bootloader. Welke bootloader heb je gekozen, en waarom juist deze?

## Afronden
Reboot je systeem en maak een user voor jezelf. Je kunt nu extra software installeren, zoals bijvoorbeeld een grafische schil. Als je zover gekomen bent, kudos! Teken je opdracht af en lever je log in.

## Bonus
Je kunt nu je systeem verder verkennen. Installeer bijvoorbeeld een window manager of desktop environment naar keuze en enkele applicaties. Bekende desktop environments zijn Gnome, KDE/Plasma, LXDE (bekend van de Raspberry Pi) en Xfce. Je kunt ook een eenvoudigere window manager kiezen, en deze combineren met andere software om een werkomgeving op te zetten. Google naar wat je interessant lijkt en go wild! Deel van de kracht van Linux is keuze: naast de opties die je hebt voor een desktop environment kun je voor bijna elk onderdeel uit verschillende programma's kiezen. Maak je machine eigen door verschillende opties uit te proberen.
