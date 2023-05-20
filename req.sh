echo "A: Arch Linux"
echo "D: Debian"
echo "F: Fedora"
echo "Please select your OS:"

read select_os

if [ $select_os == 'A' ]
then
        sudo pacman -Ssyu -y
        sudo pacman -S smartmontools
        yay -S python-pip
        pip install flask
elif [ $select_os == 'D' ]
then
        sudo apt update -y 
        sudo apt upgrade -y
        sudo apt install smartmontools -y
        sudo apt install python3-pip
        pip install flask
elif [ $select_os == 'F' ]
then
        sudo dnf upgrade --refresh
        sudo dnf install smartmontools -y
        sudo dnf install python3-pip
        pip install flask
else
        echo "is not option"
fi
