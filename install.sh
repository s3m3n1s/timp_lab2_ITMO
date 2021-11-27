#!/bin/bash

sudo cp ./name_saver.py /usr/bin/name_saver.py
sudo chmod 755 /usr/bin/name_saver.py
mkdir ~/.namesaver/ || echo "Already installed"
if ! test -f ~/.co
 then touch ~/.co
echo "4
30" > ~/.co;
fi


echo "{\"names\":[]}" > ~/.namesaver/names.json