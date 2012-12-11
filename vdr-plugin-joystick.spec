
%define plugin	joystick
%define name	vdr-plugin-%plugin
%define version	0.0.3
%define rel	19

Summary:	VDR plugin: use a joystick as a remote
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.powarman.de/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/joystick/vdr-%plugin-%version.tar.bz2
# workaround for glibc #22923
Patch1:		vdr-joystick-glibc-int32.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a joystick as a remote control for VDR. I recommend
a joystick with a minimum of 2 axes and 4 buttons.

%prep
%setup -q -n %plugin-%version
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

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%dir %{vdr_plugin_cfgdir}/%{plugin}
%config(noreplace) %{vdr_plugin_cfgdir}/%{plugin}/mappings.conf




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-18mdv2011.0
+ Revision: 404572
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-16mdv2009.1
+ Revision: 359328
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-15mdv2009.0
+ Revision: 197940
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-14mdv2009.0
+ Revision: 197682
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-13mdv2008.1
+ Revision: 145105
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-12mdv2008.1
+ Revision: 103145
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-11mdv2008.0
+ Revision: 50010
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-10mdv2008.0
+ Revision: 42096
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-9mdv2008.0
+ Revision: 22700
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-8mdv2007.0
+ Revision: 90934
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-7mdv2007.1
+ Revision: 74032
- rebuild for new vdr
- Import vdr-plugin-joystick

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2007.0
- use _ prefix for system path macros

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2007.0
- initial Mandriva release

