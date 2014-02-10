Summary:	Network traffic recorder
Name:		tcpflow
Version:	1.3.0
Release:	1
License:	GPL
Group:		Networking/Other
Source0:	https://github.com/downloads/simsong/tcpflow/%{name}-%{version}.tar.gz
URL:		http://afflib.org
BuildRequires:	libpcap-devel autoconf

%description
tcpflow is a program that captures data transmitted as part of TCP 
connections (flows), and stores the data in a way that is convenient
for protocol analysis or debugging.
A program like 'tcpdump' shows a summary of packets seen on the wire,
but usually doesn't store the data that's actually being transmitted.
In contrast, tcpflow reconstructs the actual data streams and stores
each flow in a separate file for later analysis.

%prep
%setup -q -n %{name}-%{version}
chmod -x COPYING

%build
%configure2_5x
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL
%{_bindir}/*
%{_mandir}/man*/*


%changelog
* Tue Aug 21 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.9-1
+ Revision: 815525
- version update 1.2.9

* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.7-1
+ Revision: 802341
- version update 1.2.7

* Wed May 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.6-1
+ Revision: 795135
- version update 1.2.6

* Mon Apr 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.3-1
+ Revision: 788720
- version update 1.2.3

* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 781163
- version update 1.1.1

* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.0-1
+ Revision: 771302
- version update 1.1.0

* Mon Dec 05 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.0.6-1
+ Revision: 737976
- rpmlint fix
- version update 1.0.6

* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 0.21-11mdv2010.0
+ Revision: 454052
- bump release
- fix build
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.21-8mdv2009.1
+ Revision: 298407
- rebuilt against libpcap-1.0.0

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.21-7mdv2009.0
+ Revision: 261434
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.21-6mdv2009.0
+ Revision: 254261
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 0.21-4mdv2008.1
+ Revision: 187644
- rebuild for 2008.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Olivier Thauvin <nanardon@mandriva.org> 0.21-3mdv2008.0
+ Revision: 68890
- rebuild
- Import tcpflow


