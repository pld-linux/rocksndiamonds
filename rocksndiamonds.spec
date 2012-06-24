Summary:	Boulderdash clone
Summary(pl):	Klon Boulderdasha
Summary(pt_BR):	Jogo tipo Boulderdash de pegar diamantes com mais de 10.000 n�veis
Name:		rocksndiamonds
Version:	2.0.1
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/%{name}-%{version}.tar.gz
Source1:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-emc-1.0.tar.gz
Source2:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-sp-1.0.tar.gz
Source3:	http://www.artsoft.org/RELEASES/unix/rocksndiamonds/levels/rockslevels-dx-1.0.tar.gz
Source4:	%{name}.desktop
Source5:	%{name}.png
Patch0:		%{name}-tape.patch
Patch1:		%{name}-va_arg_fix.patch
URL:		http://www.artsoft.org/rocksndiamonds/
BuildRequires:	SDL-devel >= 1.1.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
- 14233 levels (1072 in main package.)

%description -l pl
Gra podobna do Boulderdasha (o�miobitowce), Emerald Mine (Amiga) lub
Supapleksa (PC). Za��czonych jest wiele poziom�w z gier "Boulderdash",
"Emerald Mine", "Sokoban", "Supaplex" i "DX-Boulderdash", jak i
zupe�nie nowych, zaprojektowanych przez innych graczy. Gra wspiera
r�wnie� elementy poziom�w z "Diamond Caves II".

Niekt�re cechy:
- obs�uga joysticka,
- wsparcie dla lokalnej gry wieloosobowej,
- wsparcie dla sieciowej gry wieloosobowej,
- p�ynne przewijanie z 50 klatkami/s,
- efekty d�wi�kowe stereo i muzyka,
- odtwarzanie modu��w muzycznych,
- wy�wietlanie na ca�ym ekranie,
- 14233 poziomy (1072 w g��wnym pakiecie.)

%description -l pt_BR
O Rocks'n'Diamonds � um jogo tipo pegue-diamantes/evite-inimigos, com
mais de 10.000 n�veis para sua divers�o! Se voc� conhece o jogo
"Boulderdash" para Commodore C64, "Emerald Mine" para Amiga ou
"Supaplex" para PC, ent�o voc� sabe do que se trata este jogo.

Inclusos est�o v�rios n�veis dos jogos "Boulderdash", "Emerald Mine",
"Sokoban", "Supaplex" e "DX-Boulderdash", al�m de v�rios n�veis feitos
por outros jogadores.

Ele tem gr�ficos legais, som e m�sica est�reo, editor de n�veis, modo
cooperativo, gravador em fita (para rever jogadas) e suporte a rede e
joystick.

%package levels-dx
Summary:	Levels from DX Boulderdash
Summary(pl):	Poziomy z DX Boulderdash
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description levels-dx
1400 levels from DX Boulderdash.

%description levels-dx -l pl
1400 poziom�w z DX Boulderdash.

%package levels-emc
Summary:	Levels from Emerald Mine Club
Summary(pl):	Poziomy z Klubu Emerald Mine
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description levels-emc
10318 levels from Emerald Mine Club.

%description levels-emc -l pl
10318 poziom�w z Klubu Emerald Mine.

%package levels-supaplex
Summary:	Supaplex style levels
Summary(pl):	Poziomy w stylu Supaplexa
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description levels-supaplex
1443 Supaplex style levels.

%description levels-supaplex -l pl
1443 poziomy w stylu Supaplexa.

%prep
%setup -q -a1 -a2 -a3
%patch0 -p1
%patch1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DTARGET_SDL `sdl-config --cflags` \
		-DSCORE_ENTRIES=MANY_PER_NAME \
		-DRO_GAME_DIR=\\\"%{_datadir}/%{name}\\\" \
		-DRW_GAME_DIR=\\\"/var/games/%{name}\\\"" \
	LDFLAGS="%{rpmldflags} -lSDL_image -lSDL_mixer `sdl-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir}/%{name},%{_applnkdir}/Games,%{_pixmapsdir}}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6
mv -f graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE4}	$RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE5}	$RPM_BUILD_ROOT%{_pixmapsdir}

# scores
install -d $RPM_BUILD_ROOT/var/games/%{name}/scores/
for i in $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/*
do
	cd $i
	for j in `find * -type d`
	do
		mkdir $RPM_BUILD_ROOT/var/games/%{name}/scores/$j
		cd $j
		for k in `ls | grep \\\.level`
		do
			touch $RPM_BUILD_ROOT/var/games/%{name}/scores/$j/`basename $k .level`.score
		done
		cd ..
	done
	cd ..
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HARDWARE README TODO
%attr(2755,root,games) %{_bindir}/%{name}
%doc %{_mandir}/man6/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/levels
%{_datadir}/%{name}/[gms]*
%{_datadir}/%{name}/levels/[BCT]*
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
%defattr(664,root,games,755)
%dir /var/games/%{name}
%dir /var/games/%{name}/scores
/var/games/%{name}/scores/[bcr]*

%files levels-dx
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/DX_Boulderdash
%defattr(664,root,games,755)
/var/games/%{name}/scores/dx*

%files levels-emc
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Emerald_Mine_Club
%defattr(664,root,games,755)
/var/games/%{name}/scores/emc*

%files levels-supaplex
%defattr(644,root,root,755)
%{_datadir}/%{name}/levels/Supaplex
%defattr(664,root,games,755)
/var/games/%{name}/scores/supaplex*
