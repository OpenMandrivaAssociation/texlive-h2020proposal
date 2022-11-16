Name:		texlive-h2020proposal
Version:	38428
Release:	1
Summary:	LaTeX class and template for EU H2020 RIA proposal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/h2020proposal
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/h2020proposal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/h2020proposal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of a class file as well as FET and ICT
proposal templates for writing EU H2020 RIA proposals and
generating automatically the many cross-referenced tables that
are required.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/h2020proposal
%doc %{_texmfdistdir}/doc/latex/h2020proposal

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
