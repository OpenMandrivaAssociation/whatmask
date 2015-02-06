%define name whatmask
%define version 1.2
%define release 9

Summary: Convert between different netmask types
Name: %name
Version: %version
Release: %release
License: GPL
Group: Networking/Other
Source: %name-%version.tar.bz2
URL: http://www.laffeycomputer.com/whatmask.html
BuildRoot: %_tmppath/%{name}-buildroot               

%description
Whatmask is a small C program that will help you with network 
settings.

It can analyze CIDR, netmask, netmask (hex), and wildcard bit 
notations to give useful information about the network block in 
question.

%prep
%setup -q
%configure

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 man/whatmask.1 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 whatmask $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/whatmask
%{_mandir}/man1/whatmask.1*
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-8mdv2010.0
+ Revision: 434744
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-7mdv2009.0
+ Revision: 261932
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-6mdv2009.0
+ Revision: 255937
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2-4mdv2008.1
+ Revision: 136572
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 1.2-4mdv2008.0
+ Revision: 68707
- rebuild


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 22:58:40 (41260)
- rebuild

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 22:56:18 (41259)
Import whatmask

* Fri Feb 04 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.2-2mdk
- birthday rebuild

* Mon Jan 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- mandrakize package
- from Aleksander Adamowski <aleksander.adamowski@altkom.pl> :
	- Correction in %%files section to handle manpages compressed by bzip2 
  	in some distros

* Wed Dec 10 2003 Joe Laffey <software@laffeycomputer.com>
- Upgraded to version 1.2 with incorporated manpage.

