# Generated from barista-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name barista

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 1%{?dist}
Summary: Simple, transparent coffeescript integration for Rails and Rack applications
Group: Development/Languages
License: MIT
URL: http://github.com/Sutto/barista
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(coffee-script) => 2.2
Requires: rubygem(coffee-script) < 3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem-rspec
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Barista provides simple, integrated support for CoffeeScript in Rack and Rails
applications.
Much like Compass does for Sass, It also provides Frameworks (bundleable code
which can be shared via Gems).
Lastly, it also provides a Rack Application (which can be used to server
compiled code), a around_filter-style precompiler (as Rack middleware) and
simple helpers for rails and Haml.
For more details, please see the the README file bundled with it.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
git clone https://github.com/vedharish/barista-spec.git && cd barista-spec
tar -xvf spec.tar.gz
cp -pr spec/ %{buildroot}%{gem_instdir}
pushd %{buildroot}%{gem_instdir}
rspec -Ilib spec
rm -rf spec
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/.document
%{gem_instdir}/.rspec
%{gem_instdir}/.rvmrc.example
%{gem_instdir}/DESCRIPTION
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/barista.gemspec


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Sun Apr 28 2013 Harish Ved - 1.3.0-1
- Initial package
