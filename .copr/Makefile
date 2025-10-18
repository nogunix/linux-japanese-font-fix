# .copr/Makefile

COPR_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT := $(abspath $(COPR_DIR)/..)

TARBALLS := 50-user-jp-fonts.conf README.md README.ja.md LICENSE

TOPDIR := $(COPR_DIR)/_build
SOURCES := $(TOPDIR)/SOURCES
SRPMS := $(TOPDIR)/SRPMS

SPEC_DIR := $(REPO_ROOT)
ifdef spec
SPEC_DIR := $(abspath $(spec))
endif

OUTDIR := $(COPR_DIR)
ifdef outdir
OUTDIR := $(abspath $(outdir))
endif

SPEC_FILE := $(abspath $(SPEC_DIR)/linux-japanese-font-fix.spec)
SOURCE_FILES := $(addprefix $(SPEC_DIR)/,$(TARBALLS))

srpm:
	@rm -rf $(TOPDIR)
	@mkdir -p $(SOURCES) $(OUTDIR)
	@cp $(SOURCE_FILES) $(SOURCES)/
	@rpmbuild -D "_topdir $(TOPDIR)" -bs $(SPEC_FILE)
	@cp $(SRPMS)/*.src.rpm $(COPR_DIR)/
	@cp $(SRPMS)/*.src.rpm $(OUTDIR)/
	@ls $(OUTDIR)/linux-japanese-font-fix-*.src.rpm | head -n 1 > $(COPR_DIR)/srpm.list

srpm_path:
	@cat $(COPR_DIR)/srpm.list

.PHONY: srpm srpm_path
