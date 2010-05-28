#
# TODO:
#  - Source8 disappeared from repo, maybe we should remove it from the spec
#  - change Emerald_Mine_Club level file's extension to proper one and create
#    score files for each level
#  - move levels to separate spec file (rocksndiamonds-levels ?) and make it
#    noarch
#
Summary:	Boulderdash clone
Summary(pl.UTF-8):	Klon Boulderdasha
Summary(pt_BR.UTF-8):	Jogo tipo Boulderdash de pegar diamantes com mais de 10.000 níveis
Name:		rocksndiamonds
Version:	3.3.0.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/%{name}-%{version}.tar.gz
# Source0-md5:	191b7a63de9706b0aee52cdf983b3267
Source1:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Emerald_Mine_Club-2.1.0.7z
# Source1-md5:	731719b16587da63697b0d6e2d49a23e
Source2:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
# Source2-md5:	3af9a97e59f29995f3f7fc4da0595af6
Source3:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
# Source3-md5:	fbc250f7995c666c1c745dbaf591ce32
Source4:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Contributions-1.2.0.7z
# Source4-md5:	241114637643024fd427d1bf40b82e47
Source5:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/BD2K3-1.0.0.zip
# Source5-md5:	ebc8e019fa9a799757d90828e242c206
Source6:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Snake_Bite-1.0.0.zip
# Source6-md5:	52ef211765c995ea40ecb646345fdc2b
Source7:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Boulder_Dash_Dream-1.0.0.zip
# Source7-md5:	a7d78a41eb13932efce568cedc9b3388
#Source8:	rocksndiamonds-3.0.8-Boulderdash.tar.gz
## Source8-md5:	d05d38c64c6e65a913932f587e37db4a
Source9:	%{name}.desktop
Source10:	%{name}.png
Source11:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Sokoban-1.0.0.7z
# Source11-md5:	2d34a14fbee9f62a8d8bec9fdb333ec6
Source12:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Zelda-1.0.0.zip
# Source12-md5:	8e9d7c8e9d7595ac987d879774c488cd
Source13:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/ZeldaII-1.0.0.zip
# Source13-md5:	d8e6449f6ad5e29a07354e0e15290481
Patch0:		%{name}-tape.patch
Patch1:		%{name}-make.patch
URL:		http://www.artsoft.org/rocksndiamonds/
BuildRequires:	SDL-devel >= 1.1.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	p7zip
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		rodir	%{_datadir}/games/%{name}
%define		rwdir	/var/games/%{name}

%description
A game like "Boulderdash" (C 64), "Emerald Mine" (Amiga) or "Supaplex"
(PC). Included are many levels known from the games "Boulderdash",
"Emerald Mine", "Sokoban", "Supaplex" and "DX-Boulderdash", level
elements for "Diamond Caves II" style games and a lot of new levels
designed by other players.

Some features:
- joystick support,
- local multiplayer support,
- network multiplayer support,
- soft scrolling with 50 frames/s,
- stereo sound effects and music,
- music module support,
- fullscreen support,
- over 10000 available levels (over 1000 in main package).

%description -l pl.UTF-8
Gra podobna do Boulderdasha (ośmiobitowce), Emerald Mine (Amiga) lub
Supapleksa (PC). Załączonych jest wiele poziomów z gier "Boulderdash",
"Emerald Mine", "Sokoban", "Supaplex" i "DX-Boulderdash", jak i
zupełnie nowych, zaprojektowanych przez innych graczy. Gra wspiera
również elementy poziomów z "Diamond Caves II".

Niektóre cechy:
- obsługa joysticka,
- wsparcie dla lokalnej gry wieloosobowej,
- wsparcie dla sieciowej gry wieloosobowej,
- płynne przewijanie z 50 klatkami/s,
- efekty dźwiękowe stereo i muzyka,
- odtwarzanie modułów muzycznych,
- wyświetlanie na całym ekranie,
- ponad 10000 dostępnych poziomów (ponad 1000 w głównym pakiecie).

%description -l pt_BR.UTF-8
O Rocks'n'Diamonds é um jogo tipo pegue-diamantes/evite-inimigos, com
mais de 10.000 níveis para sua diversão! Se você conhece o jogo
"Boulderdash" para Commodore C64, "Emerald Mine" para Amiga ou
"Supaplex" para PC, então você sabe do que se trata este jogo.

Inclusos estão vários níveis dos jogos "Boulderdash", "Emerald Mine",
"Sokoban", "Supaplex" e "DX-Boulderdash", além de vários níveis feitos
por outros jogadores.

Ele tem gráficos legais, som e música estéreo, editor de níveis, modo
cooperativo, gravador em fita (para rever jogadas) e suporte a rede e
joystick.

%package levels-bd2k3
Summary:	BD2K3 level set
Summary(pl.UTF-8):	Zestaw poziomów BD2K3
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-bd2k3
BD2K3 level set by Alan Bond.

%description levels-bd2k3 -l pl.UTF-8
Zestaw poziomów BD2K3 autorstwa Alana Bonda.

%package levels-boulderdash
Summary:	Levels from several Boulderdash clones
Summary(pl.UTF-8):	Poziomy z kilku klonów Boulderdasha
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-boulderdash
Levels from several Boulderdash clones (Boulderdash II, Boulderdash
16, xbd) taken from Rocks'n'Diamonds 3.0.8.

%description levels-boulderdash -l pl.UTF-8
Poziomy z kilku klonów Boulderdasha (Boulderdash II, Boulderdash 16,
xbd) wzięte z Rocks'n'Diamonds 3.0.8.

%package levels-boulderdashdream
Summary:	Boulder Dash Dream level set
Summary(pl.UTF-8):	Zestaw poziomów Boulder Dash Dream
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-boulderdashdream
Boulder Dash Dream level set by Martijn Mooij.

%description levels-boulderdashdream -l pl.UTF-8
Zestaw poziomów Boulder Dash Dream autorstwa Martijna Mooija.

%package levels-contrib
Summary:	Rocks'n'Diamonds levels contributed by other players in 1995-2006
Summary(pl.UTF-8):	Poziomy do Rocks'n'Diamonds nadesłane przez innych graczy w latach 1995-2006
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-contrib
2712 Rocks'n'Diamonds levels contributed by other players in
1995-2006.

%description levels-contrib -l pl.UTF-8
2721 poziomów do Rocks'n'Diamonds nadesłanych przez innych graczy w
latach 1995-2006.

%package levels-dx
Summary:	Levels from DX Boulderdash
Summary(pl.UTF-8):	Poziomy z DX Boulderdash
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-dx
1400 levels from DX Boulderdash.

%description levels-dx -l pl.UTF-8
1400 poziomów z DX Boulderdash.

%package levels-emc
Summary:	Levels from Emerald Mine Club
Summary(pl.UTF-8):	Poziomy z Klubu Emerald Mine
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-emc
10318 levels from Emerald Mine Club.

%description levels-emc -l pl.UTF-8
10318 poziomów z Klubu Emerald Mine.

%package levels-snakebite
Summary:	Snake Bite levels
Summary(pl.UTF-8):	Poziomy Snake Bite
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-snakebite
Snake Bite levels.

%description levels-snakebite -l pl.UTF-8
Poziomy Snake Bite.

%package levels-sokoban
Summary:	Sokoban style levels
Summary(pl.UTF-8):	Poziomy w stylu Sokobana
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-sokoban
764 Sokoban style levels.

%description levels-sokoban -l pl.UTF-8
764 poziomy w stylu Sokobana.

%package levels-supaplex
Summary:	Supaplex style levels
Summary(pl.UTF-8):	Poziomy w stylu Supaplexa
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-supaplex
1443 Supaplex style levels.

%description levels-supaplex -l pl.UTF-8
1443 poziomy w stylu Supaplexa.

%package levels-zelda
Summary:	Zelda levels
Summary(pl.UTF-8):	Poziomy Zelda
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-zelda
2 levels: Zelda and Zelda 2.

%description levels-zelda -l pl.UTF-8
2 poziomy: Zelda oraz Zelda 2.

%prep
%setup -q -a2 -a3
7z x %{SOURCE1} -olevels
7z x %{SOURCE4} -olevels
unzip -q %{SOURCE5} -d levels
unzip -q %{SOURCE6} -d levels
unzip -q %{SOURCE7} -d levels
unzip -q %{SOURCE12} -d levels
unzip -q %{SOURCE13} -d levels
7z x %{SOURCE11} -olevels
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTIONS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}" \
	RO_GAME_DIR=%{rodir} \
	RW_GAME_DIR=%{rwdir} \
	SCORE_ENTRIES=MANY_PER_NAME

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{rodir},%{_desktopdir},%{_pixmapsdir}}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{rodir}

install %{SOURCE9}	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE10}	$RPM_BUILD_ROOT%{_pixmapsdir}

# scores
install -d $RPM_BUILD_ROOT%{rwdir}/scores
cd $RPM_BUILD_ROOT%{rodir}/levels
set +x
for i in *; do
	echo "Preparing score file for $i"
	cd $i
	for file in `find . -name '*.level' -type f`; do
		dir=$(dirname "$file")
		if [ "$dir" = "." ]; then
			dir="$i"
		fi
		file=$(basename "$file" .level)
		install -d $RPM_BUILD_ROOT%{rwdir}/scores/${dir}
		touch $RPM_BUILD_ROOT%{rwdir}/scores/${dir}/${file}.score
		echo -n .
	done
	cd ..
	echo "OK"
done
set -x
rm -f $RPM_BUILD_ROOT%{rodir}/levels/BD2K3/readme.txt
rm -f $RPM_BUILD_ROOT%{rodir}/levels/Boulder_Dash_Dream/readme.txt
rm -f $RPM_BUILD_ROOT%{rodir}/levels/zelda/readme.txt
#remove titlemessage_1.txt too?
rm -f $RPM_BUILD_ROOT%{rodir}/levels/zelda2/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS README docs/elements
%attr(2755,root,games) %{_bindir}/%{name}
%dir %{rodir}
%{rodir}/[gms]*
%dir %{rodir}/levels
%{rodir}/levels/Classic_Games
%{rodir}/levels/Tutorials
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man6/*
%defattr(664,root,games,755)
%dir %{rwdir}
%dir %{rwdir}/scores
%dir %{rwdir}/scores/classic_*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/classic_*/*.score

%files levels-bd2k3
%defattr(644,root,root,755)
%doc levels/BD2K3/readme.txt
%{rodir}/levels/BD2K3
%defattr(664,root,games,755)
%dir %{rwdir}/scores/BD2K3
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/BD2K3/*.score

%if 0
# Missing levels
%files levels-boulderdash
%defattr(644,root,root,755)
%{rodir}/levels/Boulderdash
%defattr(664,root,games,755)
%dir %{rwdir}/scores/bd_*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/bd_*/*.score
%endif

%files levels-boulderdashdream
%defattr(644,root,root,755)
%{rodir}/levels/Boulder_Dash_Dream
%defattr(664,root,games,755)
%dir %{rwdir}/scores/Boulder_Dash_Dream
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/Boulder_Dash_Dream/*.score

%files levels-contrib
%defattr(644,root,root,755)
%{rodir}/levels/Contributions
%defattr(664,root,games,755)
%dir %{rwdir}/scores/Contributions*
%dir %{rwdir}/scores/Contributions*/rnd_*
%dir %{rwdir}/scores/rnd_*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/Contributions*/rnd_*/*.score
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/rnd_*/*.score

%files levels-dx
%defattr(644,root,root,755)
%{rodir}/levels/DX_Boulderdash
%defattr(664,root,games,755)
%dir %{rwdir}/scores/dx*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/dx*/*.score

%files levels-emc
%defattr(644,root,root,755)
%{rodir}/levels/Emerald_Mine_Club
%defattr(664,root,games,755)
#%%dir %{rwdir}/scores/emc*
#%%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/emc*/*.score

%files levels-snakebite
%defattr(644,root,root,755)
%{rodir}/levels/Snake_Bite
%defattr(664,root,games,755)
%dir %{rwdir}/scores/snake_bite*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/snake_bite*/*.score

%files levels-sokoban
%defattr(644,root,root,755)
%{rodir}/levels/Sokoban
%defattr(664,root,games,755)
%dir %{rwdir}/scores/sb*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/sb*/*.score

%files levels-supaplex
%defattr(644,root,root,755)
%{rodir}/levels/Supaplex
%defattr(664,root,games,755)
%dir %{rwdir}/scores/supaplex*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/supaplex*/*.score

%files levels-zelda
%defattr(644,root,root,755)
%{rodir}/levels/zelda*
%defattr(664,root,games,755)
%dir %{rwdir}/scores/zelda*
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/zelda*/*.score
