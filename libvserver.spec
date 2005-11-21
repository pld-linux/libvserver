%define		_pre	pre20051119
Summary:	Linux-VServer syscall library
Summary(pl):	Biblioteka wywo³añ systemowych Linux-VServer
Name:		libvserver
Version:	1.0
Release:	0.%{_pre}.0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dev.gentoo.org/~hollow/vserver/libvserver/%{name}-%{version}_%{_pre}.tar.bz2
# Source0-md5:	26a9f54e058abaad939f0a90f99314cf
URL:		http://dev.gentoo.org/~hollow/vserver/libvserver/
Conflicts:	util-vserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a clean implementation of the Linux-VServer 2.0 API using a
library which handles all vserver syscalls and provides a interface
usable in other applications such as the tools provided with
libvserver. The tools directory contains the most basic implementation
of the syscall commands in user space. High-level programs such as the
"vserver" command of util-vserver can use these tools to access the
VServer API.

%description -l pl
Pakiet zawiera czyst± implementacjê API Linux-VServera przy u¿yciu
biblioteki, która obs³uguje wszystkie wywo³ania systemowe vservera
oraz dostarcza interfejs dla innych aplikacji takich jak narzêdzia
dostarczane z libvserver. Katalog narzêdzi zawiera najprostsz±
implementacjê poleceñ obs³ugi wywo³añ systemowych w przestrzeni
u¿ytkownika. Wysokopoziomowe programy, takie jak polecenie "vserver"
z pakietu util-vserver, mog± u¿ywaæ tych narzêdzi do dostêpu do API
VServera.

%package devel
Summary:	Header files for libvserver library
Summary(pl):	Pliki nag³ówkowe biblioteki libvserver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	linux-libc-headers
Conflicts:	util-vserver-devel < 1.0

%description devel
This is the package containing the header files for libvserver.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe dla biblioteki libvserver.

%package static
Summary:	Static libvserver library
Summary(pl):	Biblioteka statyczna libvserver
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	util-vserver-static < 1.0

%description static
Static libvserver library.

%description static -l pl
Biblioteka statyczna libvserver.

%prep
%setup -q -n %{name}-%{version}_%{_pre}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libvserver.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvserver.so
%{_libdir}/libvserver.la
%{_includedir}/linux/vserver
%{_includedir}/vserver.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a
