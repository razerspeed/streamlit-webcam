mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"razerspeed@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

apt-get update && apt-get install -y \
locales \
tmux \
zsh \
curl \
wget \
vim \
emacs24 \
sudo \
libgl1-mesa-glx \
libgl1-mesa-dri \
mesa-utils \
unzip 
