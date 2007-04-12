%define name whatmask
%define version 1.2
%define release %mkrel 3

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

%setup

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


* Fri Feb 04 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.2-2mdk
- birthday rebuild

* Mon Jan 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- mandrakize package
- from Aleksander Adamowski <aleksander.adamowski@altkom.pl> :
	- Correction in %files section to handle manpages compressed by bzip2 
  	in some distros

* Wed Dec 10 2003 Joe Laffey <software@laffeycomputer.com>
- Upgraded to version 1.2 with incorporated manpage.

* Sat Nov 30 2002 Tim Jackson <tim@timj.co.uk>
- Adjusted packaging; can build as non-root and does not overwrite
  system files whilst building

* Thu Sep 13 2001 Joe Laffey <software@laffeycomputer.com>
- Upgraded to version 1.1.

* Thu Jul 05 2001 Joe Laffey <software@laffeycomputer.com>
- Initial RPM packaging
