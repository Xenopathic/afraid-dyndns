PREFIX =
arch := $(shell uname -s)

all:

install:
ifeq ($(arch),Darwin)
	install -pm 0755 src/afraid-dyndns /usr/bin/afraid-dyndns
	perl -lne 's|/var/cache/afraid-dyndns/IP|/Library/Caches/afraid-dyndns-IP|; s|root\@localhost||; print;' conf > /etc/afraid-dyndns.conf
	touch /Library/Caches/afraid-dyndns-IP
else
	install -Dpm 0755 src/afraid-dyndns $(PREFIX)/usr/bin/afraid-dyndns
	install -DCm 0644 conf $(PREFIX)/etc/afraid-dyndns.conf
	install -dpm 0755 $(PREFIX)/var/cache/afraid-dyndns
	touch $(PREFIX)/var/cache/afraid-dyndns/IP
endif

.PHONY: install
