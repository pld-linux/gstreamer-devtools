#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	rust	# Rust based gst-dots-viewer

%define		gstmver		1.0
%define		gst_ver		1.26.0
%define		gstpb_ver	1.26.0
%define		gstpd_ver	1.26.0
%define		gstrtsp_ver	%{gst_ver}
Summary:	GStreamer development and validation tools
Summary(pl.UTF-8):	Narzędzia programistyczne i sprawdzające do GStreamera
Name:		gstreamer-devtools
Version:	1.26.0
Release:	1
License:	LGPL v2.1+, GPL v3+ (debug-viewer), MPL v2.0 (dot-viewer)
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-devtools/gst-devtools-%{version}.tar.xz
# Source0-md5:	a99f8fcd8ff7ea239c303423e0894e37
# cd gst-devtools-%{version}/dots-viewer
# cargo vendor-filterer --platform='*-unknown-linux-*' --tier=2
# cd ../..
# tar cJf gst-devtools-%{version}-vendor.tar.xz gst-devtools-%{version}/dots-viewer/vendor
Source1:	gst-devtools-%{version}-vendor.tar.xz
# Source1-md5:	07238aa1f4f12c4a64afb479ee485eb5
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.64.0
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
BuildRequires:	gstreamer-rtsp-server-devel >= %{gstrtsp_ver}
BuildRequires:	gstreamer-transcoder-devel >= %{gstpd_ver}
BuildRequires:	gtk+3-devel >= 3.0
%{?with_apidocs:BuildRequires:	hotdoc}
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	meson >= 1.4
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python3 >= 1:3.4
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.050
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with rust}
BuildRequires:	cargo >= 1.40
BuildRequires:	rust
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer development and validation tools including GstValidate, a
testing framework aiming at providing GStreamer developers tools that
check the GstElements they write behave the way they are supposed to.

%description -l pl.UTF-8
Narzędzia programistyczne i sprawdzające do GStreamera, w tym
GstValidate, szkielet testowy, którego celem jest zapewnienie
programistom narzędzi sprawdzających, czy obiekty GstElement zachowują
się w pożądany sposób.

%package apidocs
Summary:	API documentation for GstValidate library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GstValidate
Group:		Documentation
Obsoletes:	gstreamer-validate-apidocs < 1.18
BuildArch:	noarch

%description apidocs
API documentation for GstValidate library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GstValidate.

%package -n gstreamer-validate
Summary:	GstValidate - suite of tools to run GStreamer integration tests
Summary(pl.UTF-8):	GstValidate - zestaw narzędzi do uruchamiania testów integracyjnych GStreamera
Group:		Libraries
Requires:	glib2 >= 1:2.64.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	gstreamer-rtsp-server >= %{gstrtsp_ver}
Requires:	gstreamer-transcoder >= %{gstpd_ver}
Requires:	json-glib >= 1.0
Requires:	python3-modules >= 1:3.4

%description -n gstreamer-validate
The goal of GstValidate is to be able to detect when elements are not
behaving as expected and report it to the user so he knows how things
are supposed to work inside a GstPipeline. In the end, fixing issues
found by the tool will ensure that all elements behave all together in
the expected way.

%description -n gstreamer-validate -l pl.UTF-8
Celem GstValidate jest umożliwienie wykrycia sytuacji, kiedy elementy
nie zachowują się w sposób oczekiwany i zgłaszanie tego faktu
użytkownikowi tak, aby wiedział, jak powinny działać elementy wewnątrz
GstPipeline. W efekcie, poprawienie problemów wykrytych przez to
narzędzie zapewni, że wszystkie elementy razem będą się zachowywały w
sposób zgodny z oczekiwaniami.

%package -n gstreamer-validate-devel
Summary:	Header files for GstValidate library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GstValidate
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.64.0
Requires:	gstreamer-devel >= %{gst_ver}
Requires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
Requires:	gstreamer-validate = %{version}-%{release}

%description -n gstreamer-validate-devel
Header files for GstValidate library.

%description -n gstreamer-validate-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GstValidate.

%package -n gstreamer-debug-viewer
Summary:	Examine GStreamer debug log information
Summary(pl.UTF-8):	Badanie informacji z logów diagnostycznych GStreamera
License:	GPL v3+
Group:		Development/Tools
# Gtk-3.0.typelib
Requires:	gtk+3 >= 3.0
Requires:	python3-pygobject3 >= 3.0

%description -n gstreamer-debug-viewer
Tool to view and read GStreamer debug logs in an efficient way.

%description -n gstreamer-debug-viewer -l pl.UTF-8
Narzędzie do wydajnego przeglądania i czytania logów diagnostycznych
GStreamera.

%package -n gstreamer-dots-viewer
Summary:	GStreamer dot files viewer
Summary(pl.UTF-8):	Przeglądarka plików dot GStreamera
License:	MPL v2.0
%{?rust_req}

%description -n gstreamer-dots-viewer
Simple HTTP server that watches a directory for GStreamer "*.dot"
files in a local path and serves them as a web page allowing you to
browse them easily. See `gst-dots-viewer --help` for more information.

%description -n gstreamer-dots-viewer -l pl.UTF
Prosty serwer HTTP, śledzący lokalny katalog pod kątem plików
GStremera "*.dot" i serwujący je jako strony WWW, dzięki czemu można
je łatwo przeglądać. Więcej informacji w `gst-dots-viewer --help`.

%prep
%setup -q -n gst-devtools-%{version} -b1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	debug-viewer/gst-debug-viewer \
	validate/launcher/RangeHTTPServer.py \
	validate/tools/gst-validate-launcher.in

# use offline registry
CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >$CARGO_HOME/config.toml <<EOF
[source.crates-io]
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = '$PWD/dots-viewer/vendor'
EOF

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson \
	--default-library=shared \
	-Dcairo=enabled \
	-Ddebug_viewer=enabled \
	-Ddoc=%{__enabled_disabled apidocs} \
	-Ddots_viewer=%{__enabled_disabled rust} \
	-Dintrospection=enabled \
	-Dnls=enabled \
	-Dtests=disabled \
	-Dtools=enabled \
	-Dvalidate=enabled

%meson_build

%if %{with apidocs}
%meson_build build-gst-hotdoc-configs

cd build/docs
LC_ALL=C.UTF-8 hotdoc run --conf-file gst-devtools-doc.json
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson_install

%py3_comp $RPM_BUILD_ROOT%{_libdir}/gst-validate-launcher/python
%py3_ocomp $RPM_BUILD_ROOT%{_libdir}/gst-validate-launcher/python
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
cp -pr build/docs/gst-devtools-doc $RPM_BUILD_ROOT%{_docdir}/gstreamer-%{gstmver}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gstreamer-validate -p /sbin/ldconfig
%postun	-n gstreamer-validate -p /sbin/ldconfig

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gstreamer-%{gstmver}/gst-devtools-doc
%endif

%files -n gstreamer-validate
%defattr(644,root,root,755)
%doc ChangeLog NEWS RELEASE validate/README
%attr(755,root,root) %{_bindir}/gst-validate-1.0
%attr(755,root,root) %{_bindir}/gst-validate-images-check-1.0
%attr(755,root,root) %{_bindir}/gst-validate-launcher
%attr(755,root,root) %{_bindir}/gst-validate-media-check-1.0
%attr(755,root,root) %{_bindir}/gst-validate-rtsp-server-1.0
%attr(755,root,root) %{_bindir}/gst-validate-transcoding-1.0
%attr(755,root,root) %{_libdir}/libgstvalidate-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvalidate-1.0.so.0
%attr(755,root,root) %{_libdir}/libgstvalidate-default-overrides-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvalidate-default-overrides-1.0.so.0
%{_libdir}/girepository-1.0/GstValidate-1.0.typelib
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstvalidatetracer.so
%dir %{_libdir}/gstreamer-1.0/validate
%attr(755,root,root) %{_libdir}/gstreamer-1.0/validate/libgstvalidatefaultinjection.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/validate/libgstvalidategapplication.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/validate/libgstvalidategtk.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/validate/libgstvalidatessim.so
%dir %{_libdir}/gst-validate-launcher
%dir %{_libdir}/gst-validate-launcher/python
%dir %{_libdir}/gst-validate-launcher/python/launcher
%attr(755,root,root) %{_libdir}/gst-validate-launcher/python/launcher/RangeHTTPServer.py
%{_libdir}/gst-validate-launcher/python/launcher/__init__.py
%{_libdir}/gst-validate-launcher/python/launcher/[bchlmruv]*.py
%{_libdir}/gst-validate-launcher/python/launcher/__pycache__
%{_libdir}/gst-validate-launcher/python/launcher/apps
%{_libdir}/gst-validate-launcher/python/launcher/testsuites
%dir %{_datadir}/gstreamer-1.0
%{_datadir}/gstreamer-1.0/validate

%files -n gstreamer-validate-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstvalidate-1.0.so
%attr(755,root,root) %{_libdir}/libgstvalidate-default-overrides-1.0.so
%{_includedir}/gstreamer-1.0/gst/validate
%{_pkgconfigdir}/gstreamer-validate-1.0.pc
%{_datadir}/gir-1.0/GstValidate-1.0.gir

%files -n gstreamer-debug-viewer
%defattr(644,root,root,755)
%doc debug-viewer/README
%attr(755,root,root) %{_bindir}/gst-debug-viewer
%{py3_sitescriptdir}/GstDebugViewer
%{_datadir}/gst-debug-viewer
%{_datadir}/metainfo/org.freedesktop.GstDebugViewer.appdata.xml
%{_desktopdir}/org.freedesktop.GstDebugViewer.desktop
%{_iconsdir}/hicolor/48x48/apps/gst-debug-viewer.png
%{_iconsdir}/hicolor/scalable/apps/gst-debug-viewer.svg

%files -n gstreamer-dots-viewer
%defattr(644,root,root,755)
%doc dots-viewer/README.md
%attr(755,root,root) %{_bindir}/gst-dots-viewer
