#!/bin/bash

echo -n "Password: "
read -s password
printf "\n"
printf "$password" | python3 login.py $1
printf "\n"



