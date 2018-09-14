touch log
mkdir Spammy-Bot
chmod +x start.sh || chmod +X start.sh
pip install discord || pip3 install discord 
mv spammy.py Spammy-Bot 
mv README.md Spammy-Bot 
cd Spammy-Bot 
python3 spammy.py 
echo created Spammy-Bot... > log
echo moving spammy.py > log
echo moving README.md > log
echo changing current dir > log
echo bot is running > log
