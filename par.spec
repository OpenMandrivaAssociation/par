%define name	par
%define version	1.52
%define release	%mkrel 3

Summary:	A paragraph reformatter
Name:		%{name}
Version:	%{version}
Release:	%{release}
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
%make -f protoMakefile CC="gcc $RPM_OPT_FLAGS -c" LINK1="gcc"

%install
rm -rf $RPM_BUILD_ROOT

install -d %buildroot/%_bindir
install -d %buildroot/%_mandir/man1
install -m 755 -s par %buildroot/%_bindir
install -m 644 par.1 %buildroot/%_mandir/man1

# Make them world readable
chmod 0644 par.doc releasenotes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc par.doc releasenotes
%_bindir/par
%_mandir/man1/par.1*

