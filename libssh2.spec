# based on PLD Linux spec git://git.pld-linux.org/packages/libssh2.git
Summary:	Library implementing the SSH2 protocol
Name:		libssh2
Version:	1.4.3
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://www.libssh2.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	071004c60c5d6f90354ad1b701013a0b
URL:		http://libssh2.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libssh2 is a C library implementing the SSH2 protocol.

%package devel
Summary:	Header files for libssh2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel

%description devel
Header files for libssh2 library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--with-openssl=%{_prefix}

# AC_LIB_HAVE_LINKFLAGS adds unwanted -L/usr/lib to each LTLIB* - override it
%{__make} \
	LTLIBSSL="-lssl -lcrypto" \
	LTLIBZ="-lz"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README RELEASE-NOTES TODO
%attr(755,root,root) %ghost %{_libdir}/libssh2.so.1
%attr(755,root,root) %{_libdir}/libssh2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libssh2.so
%{_includedir}/libssh2*.h
%{_mandir}/man3/libssh2_*.3*
%{_pkgconfigdir}/libssh2.pc

