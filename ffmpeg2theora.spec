Summary:	A simple converter to create Ogg Theora files
Name:		ffmpeg2theora
Version:	0.29
Release:	2.1
License:	GPLv2+
Group:		Video
Url:		http://www.v2v.cc/~j/ffmpeg2theora/
Source0:	http://v2v.cc/~j/ffmpeg2theora/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	scons
BuildRequires:	ffmpeg-devel >= 0.6
BuildRequires:	pkgconfig(kate)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)

%description
Simple converter to create Ogg Theora files.

%prep
%setup -q

%build
scons prefix=%{_prefix} mandir=%{_mandir}

%install
scons install destdir=%{buildroot} prefix=%{_prefix} mandir=%{_mandir}
install -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


cat > %{_builddir}/%{name}-%{version}/README.mdv << EOF

some examples using ffmpeg2theora:

to convert your DV file, called videoclip.dv to Ogg Theora:

ffmpeg2theora videoclip.dv

this will create an Ogg Theora file called videoclip.dv.ogg.

to encode with another quality, lets say Video Quality 7 and Audio Quality 3:

ffmpeg2theora -v 7 -a 3 videoclip.dv

you can also use the v2v Presets to encode your video

ffmpeg2theora -p preview videoclip.dv

or

ffmpeg2theora -p pro videoclip.dv

on linux you can use ffmpeg2theora to stream to an icecast server:
this needs the latest icecast-kh version and a small tool to send the ogg stream to the icecast server.

dvgrab --format raw - | \
	ffmpeg2theora -a 0 -v 5 -f dv -x 320 -y 240 -o /dev/stdout - | \ 
	oggfwd  icecastserver  8000 pwd /theora.ogg

crop the input

ffmpeg2theora --croptop 16 --cropbottom 16 --cropright 32 --cropleft 8 file.avi

further examples and discussion

EOF

%files
%doc COPYING ChangeLog AUTHORS README TODO README.mdv
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

