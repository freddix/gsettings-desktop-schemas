Summary:	A collection of GSettings schemas
Name:		gsettings-desktop-schemas
Version:	3.10.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	22ed383ea2b08ec6d9022f3206290e73
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1:2.38.0
BuildRequires:	gobject-introspection-devel >= 1.38.0
BuildRequires:	intltool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings >= 1:2.38.0
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
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.datetime.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.input-sources.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.notifications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.privacy.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.search-providers.gschema.xml
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

