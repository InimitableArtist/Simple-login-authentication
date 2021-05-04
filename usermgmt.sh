#!/bin/bash

if [ $1 == "add" -o $1 == "passwd" ]
then
    echo -n "Password: "
    read -s password
    echo ""
    echo -n "Repeat password: "
    read -s repeat_password
    echo ""
    printf "$password\n$repeat_password" | python3 usermgmt.py $1 $2
else
    python3 usermgmt.py $1 $2
fi



