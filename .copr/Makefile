# .copr/Makefile

COPR_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT := $(abspath $(COPR_DIR)/..)

TARBALLS := 50-user-jp-fonts.conf README.md README.ja.md LICENSE

TOPDIR := $(COPR_DIR)/_build
SOURCES := $(TOPDIR)/SOURCES
SRPMS := $(TOPDIR)/SRPMS

# `spec` may be a spec file (as Copr's make_srpm method passes it) or the
# directory containing it.
SPEC_DIR := $(REPO_ROOT)
ifdef spec
ifeq ($(suffix $(spec)),.spec)
SPEC_DIR := $(abspath $(dir $(spec)))
else
SPEC_DIR := $(abspath $(spec))
endif
endif

OUTDIR := $(COPR_DIR)
ifdef outdir
OUTDIR := $(abspath $(outdir))
endif

SPEC_FILE := $(abspath $(SPEC_DIR)/linux-japanese-font-fix.spec)

# Source0 points at the GitHub tag tarball; build an equivalent tarball from
# the local tree so SRPM creation works offline and without the tag.
srpm:
	@command -v rpmbuild >/dev/null && command -v tar >/dev/null || \
		dnf -y install rpm-build tar
	@rm -rf $(TOPDIR)
	@mkdir -p $(SOURCES) $(OUTDIR)
	@set -e; \
	name=$$(rpmspec -q --srpm --qf '%{name}' $(SPEC_FILE)); \
	version=$$(rpmspec -q --srpm --qf '%{version}' $(SPEC_FILE)); \
	source0=$$(rpmspec -P $(SPEC_FILE) | awk '/^Source0:/ {print $$2; exit}'); \
	tar -C $(SPEC_DIR) --transform "s,^,$$name-$$version/," \
		--sort=name --owner=0 --group=0 --numeric-owner \
		-czf $(SOURCES)/$$(basename "$$source0") $(TARBALLS)
	@rpmbuild -D "_topdir $(TOPDIR)" -bs $(SPEC_FILE)
	@cp $(SRPMS)/*.src.rpm $(COPR_DIR)/
	@cp $(SRPMS)/*.src.rpm $(OUTDIR)/
	@ls $(OUTDIR)/linux-japanese-font-fix-*.src.rpm | head -n 1 > $(COPR_DIR)/srpm.list

srpm_path:
	@cat $(COPR_DIR)/srpm.list

.PHONY: srpm srpm_path
