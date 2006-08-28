%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_version %(php-config --version 2>/dev/null || echo 0)


Summary: 	PECL A zip management extension
Summary(fr): 	PECL Une extension de gestion des ZIP
Name: 		php-pecl-zip
Version: 	1.7.2
Release: 	2%{?dist}
License: 	PHP License
Group: 		Development/Languages
URL: 		http://pecl.php.net/package/zip
Source: 	http://pecl.php.net/get/zip-%{version}.tgz
Source1:	PHP-LICENSE-3.01
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: 	php-pecl(zip) = %{version}-%{release}, php-zip = %{version}-%{release}
Requires: 	php-api >= %{php_apiver}
BuildRequires: 	php-devel, zlib-devel

%description
Zip is an extension to create and read zip files.

%description -l fr
Zip est une extension pour créer et lire les archives au format ZIP.

%prep 
%setup -q -n zip-%{version}

%{__install} -m 644 -c %{SOURCE1} LICENSE

%build
phpize
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/zip.ini << 'EOF'
; Enable ZIP extension module
extension=zip.so
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc LICENSE CREDITS examples
%config(noreplace) %{_sysconfdir}/php.d/zip.ini
%{php_extdir}/zip.so

%changelog
* Mon Aug 28 2006 Remi Collet <Fedora@FamilleCollet.com> 1.7.2-2
- rebuild for FE6

* Sun Aug 27 2006 Remi Collet <Fedora@FamilleCollet.com> 1.7.2-1
- update to 1.7.2

* Sat Aug 26 2006 Remi Collet <Fedora@FamilleCollet.com> 1.7.1-2
- use php_zip.c version 1.73 from CVS 
- see http://pecl.php.net/bugs/bug.php?id=8564

* Fri Aug 25 2006 Remi Collet <Fedora@FamilleCollet.com> 1.7.1-1
- update to 1.7.1
- change macros to conform to PHP Guidelines

* Sun Aug 20 2006 Remi Collet <Fedora@FamilleCollet.com> 1.7.0-1
- update to 1.7.0

* Sun Jul 30 2006 Remi Collet <Fedora@FamilleCollet.com> 1.6.0-1
- update to 1.6.0 (Big change : Rename Class Zip to ZipArchive)

* Sun Jul 16 2006 Remi Collet <Fedora@FamilleCollet.com> 1.5.0-1
- update to 1.5.0
- Requires: php-api

* Thu Jun 29 2006 Remi Collet <Fedora@FamilleCollet.com> 1.4.1-1
- update to 1.4.1
- bundle the v3.01 PHP LICENSE file
- Suppr. Requires zip, Add Provides php-pecl(zip) and php-zip
- change defattr

* Fri Apr 28 2006 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-2
- Add zlib(devel) to Requires

* Thu Apr 27 2006 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-1
- update to 1.3.1

* Wed Apr 26 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.3-1
- initial RPM for extras
- add french summary & description
- add examples to doc.

* Tue Apr 11 2006 Remi Collet <RPMS@FamilleCollet.com> 1.2.3-1
- initial RPM
