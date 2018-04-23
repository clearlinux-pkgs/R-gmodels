#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gmodels
Version  : 2.16.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/gmodels_2.16.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gmodels_2.16.2.tar.gz
Summary  : Various R Programming Tools for Model Fitting
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gdata
Requires: R-rms
BuildRequires : R-gdata
BuildRequires : R-rms
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n gmodels

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521209242

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521209242
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmodels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmodels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gmodels
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gmodels|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gmodels/ChangeLog
/usr/lib64/R/library/gmodels/DESCRIPTION
/usr/lib64/R/library/gmodels/INDEX
/usr/lib64/R/library/gmodels/Meta/Rd.rds
/usr/lib64/R/library/gmodels/Meta/features.rds
/usr/lib64/R/library/gmodels/Meta/hsearch.rds
/usr/lib64/R/library/gmodels/Meta/links.rds
/usr/lib64/R/library/gmodels/Meta/nsInfo.rds
/usr/lib64/R/library/gmodels/Meta/package.rds
/usr/lib64/R/library/gmodels/NAMESPACE
/usr/lib64/R/library/gmodels/NEWS
/usr/lib64/R/library/gmodels/R/gmodels
/usr/lib64/R/library/gmodels/R/gmodels.rdb
/usr/lib64/R/library/gmodels/R/gmodels.rdx
/usr/lib64/R/library/gmodels/help/AnIndex
/usr/lib64/R/library/gmodels/help/aliases.rds
/usr/lib64/R/library/gmodels/help/gmodels.rdb
/usr/lib64/R/library/gmodels/help/gmodels.rdx
/usr/lib64/R/library/gmodels/help/paths.rds
/usr/lib64/R/library/gmodels/html/00Index.html
/usr/lib64/R/library/gmodels/html/R.css
