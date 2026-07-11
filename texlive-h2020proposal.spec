%global tl_name h2020proposal
%global tl_revision 38428

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX class and template for EU H2020 RIA proposal
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/h2020proposal
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/h2020proposal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/h2020proposal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package consists of a class file as well as FET and ICT proposal
templates for writing EU H2020 RIA proposals and generating
automatically the many cross-referenced tables that are required.

