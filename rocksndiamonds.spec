Summary:	Boulderdash clone
Summary(pl):	Klon Boulderdasha
Summary(pt_BR):	Jogo tipo Boulderdash de pegar diamantes com mais de 10.000 níveis
Name:		rocksndiamonds
Version:	3.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/%{name}-%{version}.tar.gz
# Source0-md5:	6a6e0397f043314e3df8ee85c03590b5
Source1:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-emc-1.0.tar.gz
# Source1-md5:	9c6cbf7394e465a90af66236dc1db6f5
Source2:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
# Source2-md5:	3af9a97e59f29995f3f7fc4da0595af6
Source3:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
# Source3-md5:	fbc250f7995c666c1c745dbaf591ce32
Source4:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Contributions-1.1.0.tar.gz
# Source4-md5:	493c97dfad3cf72544257c63b9776642
Source5:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/BD2K3-1.0.0.zip
# Source5-md5:	ebc8e019fa9a799757d90828e242c206
Source6:	http://www.artsoft.org/RELEASES/rocksndiamonds/levels/Snake_Bite-1.0.0.zip
# Source6-md5:	52ef211765c995ea40ecb646345fdc2b
# from rocksndiamonds-3.0.8, missing in 3.1.0 or contrib(?)
Source7:	rocksndiamonds-3.0.8-Boulderdash.tar.gz
# Source7-md5:	d05d38c64c6e65a913932f587e37db4a
Source8:	%{name}.desktop
Source9:	%{name}.png
Patch0:		%{name}-tape.patch
URL:		http://www.artsoft.org/rocksndiamonds/
BuildRequires:	SDL-devel >= 1.1.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Gra podobna do Boulderdasha (o¶miobitowce), Emerald Mine (Amiga) lub
Supapleksa (PC). Za³±czonych jest wiele poziomów z gier "Boulderdash",
"Emerald Mine", "Sokoban", "Supaplex" i "DX-Boulderdash", jak i
zupe³nie nowych, zaprojektowanych przez innych graczy. Gra wspiera
równie¿ elementy poziomów z "Diamond Caves II".

Niektóre cechy:
- obs³uga joysticka,
- wsparcie dla lokalnej gry wieloosobowej,
- wsparcie dla sieciowej gry wieloosobowej,
- p³ynne przewijanie z 50 klatkami/s,
- efekty d¼wiêkowe stereo i muzyka,
- odtwarzanie modu³ów muzycznych,
- wy¶wietlanie na ca³ym ekranie,
- ponad 10000 dostêpnych poziomów (ponad 1000 w g³ównym pakiecie).

%description -l pt_BR
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
Summary(pl):	Zestaw poziomów BD2K3
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-bd2k3
BD2K3 level set by Alan Bond.

%description levels-bd2k3 -l pl
Zestaw poziomów BD2K3 autorstwa Alana Bonda.

%package levels-boulderdash
Summary:	Levels from several Boulderdash clones
Summary(pl):	Poziomy z kilku klonów Boulderdasha
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-boulderdash
Levels from several Boulderdash clones (Boulderdash II, Boulderdash
16, xbd) taken from Rocks'n'Diamonds 3.0.8.

%description levels-boulderdash -l pl
Poziomy z kilku klonów Boulderdasha (Boulderdash II, Boulderdash 16,
xbd) wziête z Rocks'n'Diamonds 3.0.8.

%package levels-contrib
Summary:	Rocks'n'Diamonds levels contributed by other players in 1995-2005
Summary(pl):	Poziomy do Rocks'n'Diamonds nades³ane przez innych graczy w latach 1995-2005
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-contrib
Rocks'n'Diamonds levels contributed by other players in 1995-2005.

%description levels-contrib -l pl
Poziomy do Rocks'n'Diamonds nades³ane przez innych graczy w latach
1995-2005.

%package levels-dx
Summary:	Levels from DX Boulderdash
Summary(pl):	Poziomy z DX Boulderdash
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-dx
1400 levels from DX Boulderdash.

%description levels-dx -l pl
1400 poziomów z DX Boulderdash.

%package levels-emc
Summary:	Levels from Emerald Mine Club
Summary(pl):	Poziomy z Klubu Emerald Mine
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-emc
10318 levels from Emerald Mine Club.

%description levels-emc -l pl
10318 poziomów z Klubu Emerald Mine.

%package levels-snakebite
Summary:	Snake Bite levels
Summary(pl):	Poziomy Snake Bite
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-snakebite
Snake Bite levels.

%description levels-snakebite -l pl
Poziomy Snake Bite.

%package levels-supaplex
Summary:	Supaplex style levels
Summary(pl):	Poziomy w stylu Supaplexa
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levels-supaplex
1443 Supaplex style levels.

%description levels-supaplex -l pl
1443 poziomy w stylu Supaplexa.

%prep
%setup -q -a1 -a2 -a3 -a7
tar xzf %{SOURCE4} -C levels
unzip -q %{SOURCE5} -d levels
unzip -q %{SOURCE6} -d levels
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTIONS="%{rpmcflags} -Wall" \
	RO_GAME_DIR=%{_datadir}/%{name} \
	RW_GAME_DIR=/var/games/%{name} \
	SCORE_ENTRIES=MANY_PER_NAME

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE8}	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE9}	$RPM_BUILD_ROOT%{_pixmapsdir}

# scores
install -d $RPM_BUILD_ROOT/var/games/%{name}/scores
cd $RPM_BUILD_ROOT%{_datadir}/%{name}/levels
for i in *; do
	cd $i
	for file in `find . -name '*.level' -type f`; do
		dir=$(dirname "$file")
		if [ "$dir" = "." ]; then
			dir="$i"
		fi
		file=$(basename "$file" .level)
		install -d $RPM_BUILD_ROOT/var/games/%{name}/scores/${dir}
		touch $RPM_BUILD_ROOT/var/games/%{name}/scores/${dir}/${file}.score
	done
	cd ..
done
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/BD2K3/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HARDWARE README TODO docs/elements
%attr(2755,root,games) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/[gms]*
%dir %{_datadir}/%{name}/levels
%{_datadir}/%{name}/levels/Classic_Games
%{_datadir}/%{name}/levels/Tutorials
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man6/*
%defattr(664,root,games,755)
%dir /var/games/%{name}
%dir /var/games/%{name}/scores
%dir /var/games/%{name}/scores/classic_*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/classic_*/*.score

%files levels-bd2k3
%defattr(644,root,root,755)
%doc levels/BD2K3/readme.txt
%{_datadir}/%{name}/levels/BD2K3
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/BD2K3
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/BD2K3/*.score

%files levels-boulderdash
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Boulderdash
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/bd_*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/bd_*/*.score

%files levels-contrib
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Contributions*
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/rnd_*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/rnd_*/*.score

%files levels-dx
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/DX_Boulderdash
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/dx*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/dx*/*.score

%files levels-emc
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Emerald_Mine_Club
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/emc*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/emc*/*.score

%files levels-snakebite
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Snake_Bite
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/snake_bite*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/snake_bite*/*.score

%files levels-supaplex
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Supaplex
%defattr(664,root,games,755)
%dir /var/games/%{name}/scores/supaplex*
%config(noreplace) %verify(not md5 mtime size) /var/games/%{name}/scores/supaplex*/*.score
