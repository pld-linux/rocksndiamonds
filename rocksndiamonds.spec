Summary: 	RocksNDiamonds - Intense strategy game for X
Name: 		rocksndiamonds
Version: 	1.3.0
Release: 	1
Source: 	ftp.pht.com:/pub/linux/sunsite/X11/games/video/%{name}-%{version}.tar.gz
Patch: 		rocksndiamonds-Makefile.patch
Copyright: 	GPL
Group: 		Games/Video
Vendor: 	Pacific HiTech
Packager: 	Kjetil Wiekhorst Jørgensen <jorgens+rpm@pvv.org>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make}

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING CREDITS HARDWARE INSTALL README TODO
%attr(755,root,root) /usr/X11R6/bin/rocksndiamonds
%doc %{_mandir}/man6/rocksndiamonds.6
%dir %{_libdir}/games/rocksndiamonds
%dir %{_libdir}/games/rocksndiamonds/graphics
%{_libdir}/games/rocksndiamonds/graphics/*
%dir %{_libdir}/games/rocksndiamonds/levels
%{_libdir}/games/rocksndiamonds/levels/*
%dir %{_libdir}/games/rocksndiamonds/sounds
%{_libdir}/games/rocksndiamonds/sounds/*
%dir %{_libdir}/games/rocksndiamonds/scores
