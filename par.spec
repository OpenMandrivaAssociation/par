%define name	par
%define version	1.52
%define release	%mkrel 6

Summary:	A paragraph reformatter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	Par152.tar.bz2
URL:		http://www.nicemice.net/par/
License:	Distributable - Copyright (C) 2000 by Adam M. Costello
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.52-6mdv2010.0
+ Revision: 430237
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.52-5mdv2009.0
+ Revision: 255032
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.52-3mdv2008.1
+ Revision: 131021
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import par


* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 1.52-3mdk
- rebuild for rpm 4.2

* Thu Dec  6 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.52-2mdk
- Fix non-readable files

* Wed Aug 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.52-1mdk
- updated to 1.52

* Tue Apr 10 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.51-2mdk
- sanitized specfile (s/Copyright/License)
- added releasenotes (doc)

* Tue Feb 27 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.51-1mdk
- First Mandrake package

# end of file
