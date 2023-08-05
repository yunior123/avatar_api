
python --version
wget -O mini.sh https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh
chmod +x mini.sh
bash ./mini.sh -b -f -p /usr/local



nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader


update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 2
update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.9 1
python --version
apt-get update
apt install software-properties-common
sudo dpkg --remove --force-remove-reinstreq python3-pip python3-setuptools python3-wheel
apt-get install python3-pip
pip3 install ipywidgets

git clone https://github.com/Winfredy/SadTalker &> /dev/null

export PYTHONPATH=/content/SadTalker:$PYTHONPATH
python3.8 -m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
apt update
apt install ffmpeg &> /dev/null
cd SadTalker
python3.8 -m pip install -r requirements.txt


