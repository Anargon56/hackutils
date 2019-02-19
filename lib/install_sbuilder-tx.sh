cd ~
git clone https://github.com/Pix-head/stealBuilder
cd stealBuilder
pip download pyinstaller
tar -xzf PyInstaller*.tar.gz
cd PyInstaller*
sed -i'' -e 's#"/usr/tmp"#"/data/data/com.termux/files/usr/tmp"#g' bootloader/src/pyi_utils.c
CFLAGS="-I/data/data/com.termux/files/usr/include/libandroid-support" LDFLAGS="-landroid-support" pip install .
cd ..