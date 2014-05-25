Name:      afraid-dyndns
Version:   1.1
Release:   3%{?dist}
Summary:   A dynamic DNS client for the free service afraid.org
Group:     System Environment/Daemons
License:   GPLv3+
URL:       https://github.com/Xenopathic/afraid-dyndns
Source:    https://github.com/Xenopathic/afraid-dyndns/archive/v%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: perl
Requires: perl(Getopt::Long)

%description
This utility implements a client for the free afraid.org dynamic DNS
service.

%build

%install
rm -rf %{buildroot}
./install %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/afraid-dyndns.conf
%dir %{_localstatedir}/cache/afraid-dyndns
%ghost %{_localstatedir}/cache/afraid-dyndns/IP

%changelog
* Sun Nov 15 2009 Erick Calder <rpm@arix.com> - 1.1-3
- Fixes broken dependencies on ppc platforms

* Thu Oct 15 2009 Erick Calder <rpm@arix.com> - 1.1-2
- fixed patch for F10

* Thu Oct 15 2009 Erick Calder <rpm@arix.com> - 1.1-1
- modifications for OSX support

* Sat Oct 03 2009 Erick Calder <rpm@arix.com> - 1.0-5
- fix to application of patch, which breaks with the error 'missing header for unified diff at line 5 of patch

* Sat Oct 03 2009 Erick Calder <rpm@arix.com> - 1.0-4
- fixed broken reference to patch

* Sat Oct 03 2009 Erick Calder <rpm@arix.com> - 1.0-3
- added patch to fix issue with Makefile for F10

* Sun Sep 27 2009 Erick Calder <rpm@arix.com> - 1.0-2
- tarball extension changed

* Sat Sep 12 2009 Erick Calder <rpm@arix.com> - 1.0-1
- Initial build
