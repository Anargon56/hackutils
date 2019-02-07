cd ~
pkg install autoconf bison clang coreutils curl findutils git apr apr-util libffi-dev libgmp-dev libpcap-dev \
    postgresql-dev readline-dev libsqlite-dev openssl-dev libtool libxml2-dev libxslt-dev ncurses-dev pkg-config make ruby-dev termux-tools ncurses ncurses-utils termux-exec
git clone https://github.com/rapid7/metasploit-framework
cd metasploit-framework
curl -L https://github.com/rapid7/metasploit-framework/archive/5.0.0.tar.gz | tar xz
cd metasploit-framework-5.0.0
sed 's|git ls-files|find -type f|' -i metasploit-framework.gemspec
gem install rubygems-update
update_rubygems
gem install nokogiri -- --use-system-libraries
bundle install -j5