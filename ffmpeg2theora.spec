
Name:      ffmpeg2theora
Version:   0.29
Release:   2
Summary:   A simple converter to create Ogg Theora files
License:   GPLv2+
URL:       http://www.v2v.cc/~j/ffmpeg2theora/
Group:     Video
Source0:   http://v2v.cc/~j/ffmpeg2theora/downloads/%{name}-%{version}.tar.bz2
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
scons debug=1 prefix=%_prefix mandir=%_mandir

%install
scons install debug=1 destdir=%buildroot prefix=%_prefix mandir=%_mandir
install -D %name.1 %buildroot%_mandir/man1/%name.1


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
%_mandir/man1/%name.1*




%changelog
* Tue Jul 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.29-1
+ Revision: 807941
- version update 0.29

* Fri Nov 11 2011 Götz Waschk <waschk@mandriva.org> 0.28-2
+ Revision: 730080
- rebuild

* Mon Aug 08 2011 Götz Waschk <waschk@mandriva.org> 0.28-1
+ Revision: 693630
- update to new version 0.28

* Fri Jul 22 2011 Götz Waschk <waschk@mandriva.org> 0.27-3
+ Revision: 691049
- rebuild

* Wed Jul 21 2010 Götz Waschk <waschk@mandriva.org> 0.27-2mdv2011.0
+ Revision: 556479
- don't display usage information on installation (pterjan)

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.27-1mdv2011.0
+ Revision: 550285
- new version

* Wed Dec 23 2009 Götz Waschk <waschk@mandriva.org> 0.25-1mdv2010.1
+ Revision: 481666
- build with libkate
- new version
- drop patch

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.24-2mdv2010.0
+ Revision: 437539
- rebuild

* Fri Mar 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.24-1mdv2009.1
+ Revision: 359035
- update to new version 0.24

* Wed Mar 11 2009 Götz Waschk <waschk@mandriva.org> 0.23-1mdv2009.1
+ Revision: 353680
- update to new version 0.23

* Sat Oct 25 2008 Götz Waschk <waschk@mandriva.org> 0.22-1mdv2009.1
+ Revision: 297105
- new version
- fix build
- fix installation

* Mon Oct 13 2008 Götz Waschk <waschk@mandriva.org> 0.21-2mdv2009.1
+ Revision: 293151
- rebuild for new ffmpeg

* Mon Jun 30 2008 Götz Waschk <waschk@mandriva.org> 0.21-1mdv2009.0
+ Revision: 230137
- new version
- drop patch
- remove plf build option

* Fri Apr 25 2008 Götz Waschk <waschk@mandriva.org> 0.20-4mdv2009.0
+ Revision: 197465
- fix plf build

* Fri Apr 25 2008 Götz Waschk <waschk@mandriva.org> 0.20-3mdv2009.0
+ Revision: 197453
- fix build with new ffmpeg
- update license tag

* Fri Jan 18 2008 Götz Waschk <waschk@mandriva.org> 0.20-2mdv2008.1
+ Revision: 154558
- rebuild

* Wed Jan 02 2008 Götz Waschk <waschk@mandriva.org> 0.20-1mdv2008.1
+ Revision: 140421
- new version
- patch to make it build with new ffmpeg
- rebuild for new ffmpeg

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.19-2mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 0.19-2mdv2008.0
+ Revision: 58010
- fix description

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 0.19-1mdv2008.0
+ Revision: 57990
- new version

