## environment

WSL2

### building environment memo

```bash
 1717  mkdir rpa_ws
 1718  cd ./rpa_ws/
 1719  python3 -m pip install rpaframework
 1720  cd
 1721  cd ./tensorflow/
 1722  ls
 1723  cd ./venv/
 1724  lks
 1725  ls
 1726  cd ./lib
 1727  ls
 1728  cd ./python3.12/
 1729  ls]
 1730  ls
 1731  cd ./site-packages/
 1732  ls
 1733  cd
 1734  cd ./rpa_ws/
 1735  python3 -m venv venv
 1736  ls
 1737  source ./venv/bin/activate
 1738  ls
 1739  pip3 install rpaframework
 1740  touch test.py
 1741  chmod +x test.py 
 1742  pip3 install playwright
 1743  playwright install
 1744  VcXsrv
 1745  sudo apt-get update
 1746  sudo apt-get upgrade
 1747  sudo playwright install-deps
 1748  sudo apt install python3-playwright
 1749  sudo apt-get install -y     libnss3     libnspr4     libasound2     libxshmfence1     libxcomposite1     libxrandr2     libxtst6     libpangocairo-1.0-0     libatk-bridge2.0-0     libcups2     libdbus-1-3     libgdk-pixbuf2.0-0     libgtk-3-0     libx11-xcb1     libxdamage1     libxinerama1
 1750  sudo apt-get install -y     libnss3     libnspr4     libxshmfence1     libxcomposite1     libxrandr2     libxtst6     libpangocairo-1.0-0     libatk-bridge2.0-0     libcups2     libdbus-1-3     libgdk-pixbuf2.0-0     libgtk-3-0     libx11-xcb1     libxdamage1     libxinerama1
 1751  sudo apt install libasound2
 1752  sudo apt install libasound2-dev 
 1753  playwright install
 1754  sudo apt install                libwoff2dec.so.1.0.2            libvpx.so.9                     libevent-2.1.so.7               libopus.so.0                    libgstallocators-1.0.so.0       libgstapp-1.0.so.0              libgstpbutils-1.0.so.0          libgstaudio-1.0.so.0            libgstgl-1.0.so.0               libgsttag-1.0.so.0              libgstvideo-1.0.so.0            libgstcodecparsers-1.0.so.0     libgstfft-1.0.so.0              libflite.so.1                   libflite_usenglish.so.1         libflite_cmu_grapheme_lang.so.1 libflite_cmu_grapheme_lex.so.1  libflite_cmu_indic_lang.so.1    libflite_cmu_indic_lex.so.1     libflite_cmulex.so.1            libflite_cmu_time_awb.so.1      libflite_cmu_us_awb.so.1        libflite_cmu_us_kal16.so.1      libflite_cmu_us_kal.so.1        libflite_cmu_us_rms.so.1        libflite_cmu_us_slt.so.1        libwebpdemux.so.2               libavif.so.16                   libharfbuzz-icu.so.0            libwebpmux.so.3                 libenchant-2.so.2               libsecret-1.so.0                libhyphen.so.0                  libmanette-0.2.so.0             libGLESv2.so.2                  libx264.so
 1755  ifconfig
 1756  deactivate 
 1757  cd
 1758  vi .bashrc 
 1759  source .bashrc 
 1760  echo $DISPLAY 
 1761  sudo apt-get install x11-apps
 1762  xeyes 
 1763  echo $DISPLAY 
 1764  cd ./rpa_ws/
 1765  python3 rpa_script.py 
 1766  source ./venv/bin/activate
 1767  python3 rpa_script.py 
 1768  deactivate 
 1769  cd
 1770  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
 1771  echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
 1772  cat /etc/apt/sources.list.d/google-chrome.list
 1773  sudo apt update
 1774  sudo apt-get install -y google-chrome-stable
 1775  google-chrome
 1776  sudo apt-get install -y firefox
 1777  firefox
 1778  sudo apt-get install -y chromium-driver
 1779  chromedriver --version
 1780  sudo apt-get install -y firefox-geckodriver
 1781  which google-chrome
 1782  echo $PATH
 1783  echo $PATH | grep /usr/bin
 1784  cd ./rpa_ws/
 1785  ls
 1786  source ./venv/bin/activate
 1787  python3 rpa_script.py 
 1788  touch playwright_script.py
 1789  chmod +x playwright_script.py 
 1790  python3 playwright_script.py 
 1791  pip3 install pandas
 1792  pip3 install beautifulsoup4
 1793  touch amazon_script.py
 1794  chmod +x amazon_script.py 
 1795  google-chrome
 1796  python3 amazon_script.py 
 1797  ls
 1798  chmod +x digikey_script.py 
 1799  ls
 1800  git init
 1801  git status
 1802  touch .gitignore
 1803  vi .gitignore 
 1804  touch readme.md
 1805  history 300 > readme.md 
```