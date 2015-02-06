Summary:	Network traffic recorder
Name:		tcpflow
Version:	1.4.4
Release:	2
License:	GPL
Group:		Networking/Other
Source0:	http://www.digitalcorpora.org/downloads/tcpflow/%{name}-%{version}.tar.gz
URL:		http://afflib.org
BuildRequires:	libpcap-devel
BuildRequires:	autoconf
BuildRequires:	boost-devel
BuildRequires:	gtk+2.0
BuildRequires:	pkgconfig(openssl)

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
