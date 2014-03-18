%define debug_package %{nil}

Summary:	A paragraph reformatter
Name:		par
Version:	1.52
Release:	7
Source0:	Par152.tar.bz2
URL:		http://www.nicemice.net/par/
License:	Distributable - Copyright (C) 2000 by Adam M. Costello
Group:		Text tools

%description
Par is a paragraph reformatter, similar to the standard Unix fmt
filter, but better. It uses a dynamic programming algorithm, which
produces much better-looking line breaks than the greedy algorithm
used by fmt. It can also deal correctly with a variety of quotation
and comment conventions.

%prep
%setup -q -n Par152

%build
%make -f protoMakefile CC="gcc %{optflags} -c" LINK1="gcc"

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install -m 755 -s par %{buildroot}/%{_bindir}
install -m 644 par.1 %{buildroot}/%{_mandir}/man1

# Make them world readable
chmod 0644 par.doc releasenotes

%files
%doc par.doc releasenotes
%{_bindir}/par
%{_mandir}/man1/par.1*
