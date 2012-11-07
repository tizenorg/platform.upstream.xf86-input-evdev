Name:           xf86-input-evdev
Version:        2.7.3
Release:        0
License:        MIT
Summary:        Generic Linux input driver for the Xorg X server
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Servers/XF86_4
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1:        evdev.conf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
Requires:       udev

%description
evdev is an Xorg input driver for Linux's generic event devices. It
therefore supports all input devices that the kernel knows about,
including most mice, keyboards, tablets and touchscreens.

%package devel
Summary:        Generic Linux input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
evdev is an Xorg input driver for Linux's generic event devices. It
therefore supports all input devices that the kernel knows about,
including most mice, keyboards, tablets and touchscreens.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/10-evdev.conf


%remove_docs
%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%files
%defattr(-,root,root)
%doc COPYING
%{_sysconfdir}/X11/xorg.conf.d/10-evdev.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/evdev_drv.so

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-evdev.pc

%changelog
