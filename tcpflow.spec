%define name         tcpflow
%define version 0.21
%define release %mkrel 10

Summary: Network traffic recorder
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Other
Source:  http://www.circlemud.org/pub/jelson/tcpflow/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.circlemud.org/~jelson/software/tcpflow/
# autoconf required to rebuild the ./configure, which seems outdated.
BuildRequires: libpcap-devel autoconf

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
autoreconf -fis

%configure2_5x
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root,755)
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL
%{_bindir}/*
%{_mandir}/man*/*
