Summary:	Disposable Soft Synth Interface specification
Summary(pl.UTF-8):   Specyfikacja Disposable Soft Synth Interface
Name:		dssi
Version:	0.9.1
Release:	2
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	1a353c3ae80328cded838853ddf52164
URL:		http://dssi.sourceforge.net/
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel >= 1.0
BuildRequires:	liblo-devel >= 0.12
# lib{sndfile,samplerate} are req. to build examples
#BuildRequires:	libsndfile-devel
#BuildRequires:	libsamplerate-devel
Requires:	alsa-lib-devel >= 0.9
Requires:	ladspa-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

DSSI consists of a C language API for use by plugins and hosts, based
on the LADSPA API, and an OSC (Open Sound Control) API for use in user
interface to host communications. The DSSI specification consists of
an RFC which describes the background for the proposal and defines the
OSC part of the specification, and a documented header file which
defines the C API.

%description -l pl.UTF-8
DSSI (wymawiane "dizzy") to API dla wtyczek dźwiękowych z
zastosowaniem szczególnie dla wtyczek syntezy programowej z natywnymi
interfejsami użytkownika. DSSI to otwarta specyfikacja stworzona do
używania w linuksowych aplikacjach dźwiękowych, ale przenośna na inne
platformy. Można ją określić jako LADSPA dla instrumentów lub coś
porównywalnego do VSTi.

DSSI składa się z API języka C do użytku przez wtyczki i hosty, oparte
o API LADSPA oraz API OSC (Open Sound Control) do użytku w
interfejsach użytkownika do komunikacji z hostem. Specyfikacja DSSI
składa się z RFC opisującego tło propozycji i definiującego część OSC
specyfikacji oraz udokumentowanego pliku nagłówkowego definiującego
API C.

%package host-jack
Summary:	A simple JACK/ALSA-sequencer plugin host
Summary(pl.UTF-8):   Prosty host wtyczek sekwencera JACK/ALSA
Group:		Applications/Sound
Requires:	liblo >= 0.12

%description host-jack
A simple JACK/ALSA-sequencer plugin host.

%description host-jack -l pl.UTF-8
Prosty host wtyczek sekwencera JACK/ALSA.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/TODO doc/*.txt
%{_includedir}/dssi.h
%{_pkgconfigdir}/dssi.pc

%files host-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack-dssi-host
