%define		zope_subname	CMFQuickInstallerTool
Summary:	A Zope product independent from the former CMFQuickInstaller
Summary(pl):	Dodatek do Zope niezale¿ny od poprzedniego CMFQuickInstallera
Name:		Zope-%{zope_subname}
Version:	1.5.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tgz
# Source0-md5:	c31d26cbfb515fb90169aafe17f0bdfa
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF

%define 	product_dir	/usr/lib/zope/Products

%description
CMFQuickInstallerTool is a Zope product independent from the former
CMFQuickInstaller. The main difference to CMFQuickInstaller the
tracking of what a product creates during install.

%description -l pl
CMFQuickInstallerTool jest dodatkiem do Zope niezale¿nym od
poprzedniego CMFQuickInstallera. G³ówna ró¿nica w stosunku do
CMFQuickInstallera to mo¿liwo¶æ ¶ledzenia, co tworzy dany produkt w
czasie instalacji.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {forms,interfaces,*.py,*.gif,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README.txt ChangeLog DEPENDS
%{_datadir}/%{name}
