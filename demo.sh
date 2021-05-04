#!/bin/bash

demo_username="neki_username"
demo_password="nekipassword"
demo_krivi_password="krivipassword"
demo_novi_password="novipassword"

chmod u+x usermgmt.sh
chmod u+x login.sh

echo "Demo"
echo "Dodavanje korisnika:"
echo "./usermgmt.sh add $demo_username"
echo "Nakon izvođenja ove naredbe, dobit ćemo prompt za upis passworda."
echo "Upisani password će biti $demo_password."
printf "$demo_password\n$demo_password" | ./usermgmt.sh add $demo_username

echo "Novi korisnik će biti pohranjen u datoteku save.json"

read -p "Pritisnite enter za nastavak."

echo "Forsiranje korisnika na promjenu passworda: "
echo "./usermgmt.sh forcepass $demo_username"
./usermgmt.sh forcepass $demo_username

echo "Sada će pri sljedećoj prijavi, korisnik $demo_username biti prisiljen promijeniti password."

read -p "Pritisnite enter za nastavak."

echo "Primjer logiranja korisnika: "

echo "Budući da smo prošlom naredbom odredili da korisnik $demo_username mora promijeniti password, molim da upišete novi password na promptu."
echo "./login.sh $demo_username"
printf "$demo_password" | ./login.sh $demo_username

read -p "Pritisnite enter za nastavak."

echo "Pogledajmo sada što će se desiti ako se korisnik pokuša prijaviti sa krivim passwordom: "
echo "./login.sh $demo_username"
printf "$demo_krivi_password" | ./login.sh $demo_username

read -p "Pritisnite enter za nastavak."

echo "Korisnikov username također može mijenjati admin: "
echo "Novi password će biti $demo_novi_password."
echo "./usermgmt.sh passwd $demo_username"
printf "$demo_novi_password\n$demo_novi_password" | ./usermgmt.sh passwd $demo_username

read -p "Pritisnite enter za nastavak."

echo "Za brisanje korisnika koristi se naredba: "
echo "./usermgmt.sh del $demo_username"
./usermgmt.sh del $demo_username

