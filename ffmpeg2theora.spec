%define name ffmpeg2theora
%define version 0.28
%define release		%mkrel 2

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   A simple converter to create Ogg Theora files
License:   GPLv2+
URL:       http://www.v2v.cc/~j/ffmpeg2theora/
Group:     Video
Source:    http://v2v.cc/~j/ffmpeg2theora/downloads/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ffmpeg-devel >= 0.6
BuildRequires: libvorbis-devel
BuildRequires: libtheora-devel
BuildRequires: scons
BuildRequires: libkate-devel

%description
Simple converter to create Ogg Theora files.

%prep
%setup -q

%build
scons prefix=%_prefix mandir=%_mandir

%install
rm -rf $RPM_BUILD_ROOT
scons install destdir=%buildroot prefix=%_prefix mandir=%_mandir
install -D %name.1 %buildroot%_mandir/man1/%name.1


cat > $RPM_BUILD_DIR/%{name}-%{version}/README.mdv << EOF

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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING ChangeLog AUTHORS README TODO README.mdv
%attr(0755,root,root) %{_bindir}/%{name}
%_mandir/man1/%name.1*


