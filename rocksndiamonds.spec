Summary:	Rocks'N'Diamonds - Intense strategy game for X
Summary(pl):	Rocks'N'Diamonds - gra strategiczna pod X
Name:		rocksndiamonds
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Vendor:		Pacific HiTech
Source0:	ftp://ftp.pht.com/pub/linux/sunsite/X11/games/video/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a nice little game with color graphics and sound for your Unix
system with color X11. You need an 8-Bit color display or better. It
will not work on black&white systems, and maybe not on gray scale
systems.

If you know the game "Boulderdash" (8-bit computers) or "Emerald Mine"
(Amiga), you know what "ROCKS'N'DIAMONDS" is about.

%description -l pl
To jest ma³a gra z kolorow± grafik± i d¼wiêkiem pod X11. Potrzebuje co
najmniej 8-bitowego koloru. Je¿eli znasz "Boulderdash" (o¶miobitowce)
lub "Emerald Mine" (Amiga), bêdziesz wiedzia³ o czym jet
"Rocks'n'Diamonds".

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT

gzip -9nf CHANGES CREDITS HARDWARE README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz CREDITS.gz HARDWARE.gz README.gz TODO.gz
%attr(755,root,root) %{_bindir}/rocksndiamonds
%doc %{_mandir}/man6/rocksndiamonds.6
%dir %{_libdir}/games/rocksndiamonds
%{_libdir}/games/rocksndiamonds/graphics
%{_libdir}/games/rocksndiamonds/levels
%{_libdir}/games/rocksndiamonds/sounds
%dir %{_libdir}/games/rocksndiamonds/scores
