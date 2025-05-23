Summary:	A simple converter to create Ogg Theora files
Name:		ffmpeg2theora
Version:	0.30
Release:	2
Group:		Video
License:	GPLv3
URL:		https://www.v2v.cc/~j/ffmpeg2theora/
Source0:	http://v2v.cc/~j/ffmpeg2theora/downloads/%{name}-%{version}.tar.bz2
Patch1:		ffmpeg2theora-0.29-link.patch
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	libvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	scons
BuildRequires:	libkate-devel

%description
Simple converter to create Ogg Theora files.

%prep
%setup -q
%autopatch -p1

%build
scons prefix=%_prefix mandir=%_mandir APPEND_LINKFLAGS="%ldflags" APPEND_CCFLAGS="%optflags"

%install
scons install destdir=%buildroot prefix=%_prefix mandir=%_mandir APPEND_LINKFLAGS="%ldflags" APPEND_CCFLAGS="%optflags"
install -D %name.1 %buildroot%_mandir/man1/%name.1

cat > %{_builddir}/%{name}-%{version}/README.omv << EOF

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
%doc COPYING ChangeLog AUTHORS README TODO README.omv
%{_bindir}/%{name}
%_mandir/man1/%name.1*

