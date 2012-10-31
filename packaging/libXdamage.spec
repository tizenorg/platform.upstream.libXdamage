Name:           libXdamage
Version:        1.1.3
Release:        3
License:        MIT
Summary:        X Damage extension library
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(damageproto) >= 1.1.0
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXdamage runtime library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxdamage-devel

%description devel
X.Org X11 libXdamage development package.

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install

make install DESTDIR=%{buildroot} INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXdamage.so.1
%{_libdir}/libXdamage.so.1.1.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.p
