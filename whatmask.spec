%define name whatmask
%define version 1.2
%define release %mkrel 7

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
