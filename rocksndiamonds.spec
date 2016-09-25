Summary:	Boulderdash clone
Summary(pl.UTF-8):	Klon Boulderdasha
Summary(pt_BR.UTF-8):	Jogo tipo Boulderdash de pegar diamantes com mais de 10.000 níveis
Name:		rocksndiamonds
Version:	3.3.1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/%{name}-%{version}.tar.gz
# Source0-md5:	9fb7d125a314f55c5148c0e47f9ebb42
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-tape.patch
Patch1:		%{name}-make.patch
URL:		http://www.artsoft.org/rocksndiamonds/
BuildRequires:	SDL-devel >= 1.1.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		rodir	%{_datadir}/games/%{name}
%define		rwdir	/var/games/%{name}

%description
Rocks'n'Diamonds is an arcade game for Unix, Mac OS X, Windows and DOS
in the tradition of:
- "Boulderdash" (8-bit),
- "Emerald Mine" (Amiga),
- "Supaplex" (Amiga/PC),
- "Sokoban" (PC).

Included are many levels known from the classic games "Boulderdash",
"Emerald Mine", "Sokoban" and "Supaplex". Other levels are available
in separate packages (rocksndiamonds-levels-*).

Some features:
- network multiplayer support (up to 4 players) for Unix,
- local multiplayer support (up to 4 players),
- soft scrolling with 50 frames/s,
- customizable keyboard and joystick support,
- stereo sound effects and music,
- music modules and fullscreen support (in SDL version),
- lots of additional levels available (over 10000).

%description -l pl.UTF-8
Rocks'n'Diamonds to gra dla Uniksa, Mac OS X, Windows oraz DOS-a
utrzymana w tradycji gier:
- Boulderdash (ośmiobitowce),
- Emerald Mine (Amiga),
- Supaplex (Amiga/PC),
- Sokoban (PC).

Załączonych jest wiele poziomów z klasycznych gier "Boulderdash",
"Emerald Mine", "Sokoban" i "Supaplex". Inne poziomy są dostępne w
osobnych pakietach (rocksndiamonds-levels-*).

Niektóre cechy:
- możliwość gry wieloosobowej przez sieć (do 4 graczy, tylko Unix),
- możliwość gry wieloosobowej lokalnie (do 4 graczy),
- płynne przewijanie z 50 klatkami/sekundę,
- konfigurowalna obsługa klawiatury i joysticka,
- efekty dźwiękowe stereo i muzyka,
- odtwarzanie modułów muzycznych i tryb pełnoekranowy (w wersji SDL),
- wiele dostępnych dodatkowych poziomów (ponad 10000).

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

%prep
%setup -q
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

install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2}	$RPM_BUILD_ROOT%{_pixmapsdir}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS README docs/elements
%attr(2755,root,games) %{_bindir}/rocksndiamonds
%dir %{rodir}
%{rodir}/graphics
%{rodir}/music
%{rodir}/sounds
%dir %{rodir}/levels
%{rodir}/levels/Classic_Games
%{rodir}/levels/Tutorials
%{_desktopdir}/rocksndiamonds.desktop
%{_pixmapsdir}/rocksndiamonds.png
%{_mandir}/man6/rocksndiamonds.6*
%defattr(664,root,games,755)
%dir %{rwdir}
%dir %{rwdir}/scores
%dir %{rwdir}/scores/classic_boulderdash
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/classic_boulderdash/*.score
%dir %{rwdir}/scores/classic_sokoban
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/classic_sokoban/*.score
%dir %{rwdir}/scores/rnd_tutorial_aaron_davidson
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/rnd_tutorial_aaron_davidson/*.score
%dir %{rwdir}/scores/rnd_tutorial_niko_boehm
%config(noreplace) %verify(not md5 mtime size) %{rwdir}/scores/rnd_tutorial_niko_boehm/*.score
