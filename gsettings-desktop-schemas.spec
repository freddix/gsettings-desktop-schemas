Summary:	A collection of GSettings schemas
Name:		gsettings-desktop-schemas
Version:	3.6.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	5f7d7c88c04b1abcf59c3f27027c05c2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of GSettings schemas.

%package devel
Summary:	Development files for gsettings-desktop-schemas
Group:		Development/Libraries

%description devel
Development files for gsettings-desktop-schemas.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%{_libdir}/girepository-1.0/GDesktopEnums-3.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.input-sources.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.session.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.thumbnailers.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.wm.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.wm.preferences.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.locale.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/GDesktopEnums-3.0.gir
%{_includedir}/gsettings-desktop-schemas
%{_npkgconfigdir}/gsettings-desktop-schemas.pc

