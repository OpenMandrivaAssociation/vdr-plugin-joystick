%define plugin	joystick

Summary:	VDR plugin: use a joystick as a remote
Name:		vdr-plugin-%plugin
Version:	0.0.3
Release:	22
Group:		Video
License:	GPL
URL:		http://www.powarman.de/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/joystick/vdr-%plugin-%{version}.tar.bz2
# workaround for glibc #22923
Patch1:		vdr-joystick-glibc-int32.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a joystick as a remote control for VDR. I recommend
a joystick with a minimum of 2 axes and 4 buttons.

%prep
%setup -q -n %plugin-%{version}
%patch1 -p0
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# joystick device
var=DEVICE
param=--device=DEVICE
default=/dev/input/js0
%vdr_plugin_params_end

perl -pi -e 's/^2/# 2/' examples/mappings.conf

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -D -m644 examples/mappings.conf %{buildroot}%{vdr_plugin_cfgdir}/%plugin/mappings.conf

%files -f %plugin.vdr
%doc README HISTORY
%dir %{vdr_plugin_cfgdir}/%{plugin}
%config(noreplace) %{vdr_plugin_cfgdir}/%{plugin}/mappings.conf




