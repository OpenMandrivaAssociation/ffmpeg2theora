%define name ffmpeg2theora
%define version 0.19
%define release		%mkrel 2
%define build_plf 0
%{?!mkrel:%define mkrel(c:) %{-c:0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.*)(\\d+)$/;$rel=$2-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   A simple converter to create Ogg Theora files
License:   GPL
URL:       http://www.v2v.cc/~j/ffmpeg2theora/
Group:     Video
Source:    http://www.v2v.cc/~j/ffmpeg2theora/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ffmpeg-devel >= 0.4.9-0.pre1.20060309.1mdk
BuildRequires: libvorbis-devel
BuildRequires: libtheora-devel
%if %build_plf
BuildRequires: libfaad2-devel
BuildRequires: dtsdec-devel
%endif

%description
Simple converter to create Ogg Theora files.

%if %build_plf
This package is in PLF as it violates some patents.
%endif

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

cat > $RPM_BUILD_DIR/%{name}-%{version}/README.urpmi << EOF

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
%doc COPYING ChangeLog AUTHORS README TODO README.urpmi
%attr(0755,root,root) %{_bindir}/%{name}
%_mandir/man1/%name.1*


