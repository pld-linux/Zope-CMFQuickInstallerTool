%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFQuickInstallerTool
Summary:	A Zope product independent from the former CMFQuickInstaller
Summary(pl):	Dodatek do Zope niezale¿ny od poprzedniego CMFQuickInstallera
Name:		Zope-%{zope_subname}
Version:	1.4
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}_%{version}.tgz
# Source0-md5:	11326c7bdcb4c651099957bd3c04cb8d
URL:		http://cvs.bluedynamics.org/viewcvs/CMFQuickInstallerTool/
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

rm -rf {forms,interfaces}/CVS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {forms,interfaces,*.py,*.gif} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%doc AUTHORS README.txt
%{_datadir}/%{name}
