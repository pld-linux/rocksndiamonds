Summary: 	RocksNDiamonds - Intense strategy game for X
Name: 		rocksndiamonds
Version: 	1.3.0
Release: 	1
Source: 	ftp.pht.com:/pub/linux/sunsite/X11/games/video/%{name}-%{version}.tar.gz
Patch: 		rocksndiamonds-Makefile.patch
Copyright: 	GPL
Group: 		games/video
Vendor: 	Pacific HiTech
Packager: 	Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org>
BuildRoot: 	/tmp/%{name}-%{version}-root

%description
This is a nice little game with color graphics and sound for your
Unix system with color X11. You need an 8-Bit color display or better.
It will not work on black&white systems, and maybe not on gray scale systems.

If you know the game "Boulderdash" (Commodore C64) or "Emerald Mine"
(Amiga), you know what "ROCKS'N'DIAMONDS" is about.


%prep
%setup -q

%patch -p1

%build
make

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING CREDITS HARDWARE INSTALL README TODO
%attr(755,root,root) /usr/X11R6/bin/rocksndiamonds
%doc %{_mandir}/man6/rocksndiamonds.6
%dir /usr/lib/games/rocksndiamonds
%dir /usr/lib/games/rocksndiamonds/graphics
/usr/lib/games/rocksndiamonds/graphics/*
%dir /usr/lib/games/rocksndiamonds/levels
/usr/lib/games/rocksndiamonds/levels/*
%dir /usr/lib/games/rocksndiamonds/sounds
/usr/lib/games/rocksndiamonds/sounds/*
%dir /usr/lib/games/rocksndiamonds/scores

%changelog
* Thu Jan 11 1999 Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org> [1.3.0-1]

- upgraded to version 1.3.0

* Sat Dec 19 1998 Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org> [1.2.0-1]

- initial version packaged by me.
