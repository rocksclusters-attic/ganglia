# --------------------------------------------------- -*- Makefile -*- --
# $Id: Makefile,v 1.28 2012/11/27 00:48:57 phil Exp $
#
# @Copyright@
#
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
#
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided
# with the distribution.
#
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement:
#
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
#
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of
# the associated name, interested parties should contact Technology
# Transfer & Intellectual Property Services, University of California,
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910,
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.28  2012/11/27 00:48:57  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.27  2012/09/07 23:39:46  clem
# minor fixes to the Makefile
#
#  - moved some instruction in Makefile instead of nodes files
#    so that rpms are already fixed
#
# Revision 1.26  2012/05/06 05:49:06  phil
# Copyright Storm for Mamba
#
# Revision 1.25  2011/07/23 02:30:59  phil
# Viper Copyright
#
# Revision 1.24  2010/09/07 23:53:14  bruno
# star power for gb
#
# Revision 1.23  2009/05/01 19:07:16  mjk
# chimi con queso
#
# Revision 1.22  2009/04/24 22:07:49  anoop
# Moved the solaris specific startup scripts to ganglia-hpc package
#
# Revision 1.21  2009/04/23 20:04:13  bruno
# need to use DESTDIR instead of prefix for install
#
# Revision 1.20  2009/04/21 23:42:56  anoop
# Moved the build target from common Makefile to OS specific
# makefile
#
# Revision 1.19  2009/04/21 18:10:55  bruno
#  - converted gmond dbreport to rocks command line
#  - added supporting packages for ganglia monitor core
#
# Revision 1.18  2008/10/18 00:56:08  mjk
# copyright 5.1
#
# Revision 1.17  2008/10/15 20:13:03  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.16  2008/06/16 17:58:08  bruno
# include man pages
#
# Revision 1.15  2008/04/24 23:44:44  bruno
# updated for 3.0.7
#
# Revision 1.14  2008/03/06 23:41:51  mjk
# copyright storm on
#
# Revision 1.13  2007/09/29 00:58:43  anoop
# Force ganglia compilation using GCC. Sun studio compilers don't seem to work
#
# Revision 1.12  2007/06/23 04:03:35  mjk
# mars hill copyright
#
# Revision 1.11  2007/06/08 14:59:24  anoop
# INIT_SCRIPTS_DIR and not INIT_SCRIPTS_DIR
#
# Revision 1.10  2007/04/28 00:02:57  anoop
# Changed to a newer version of Ganglia
# Made creation of package more generic
# to support both linux and solaris
#
# Revision 1.9  2006/12/06 01:40:49  anoop
# Ganglia Roll changed to accomadate the MAKE,INSTALL and TAR variables
#
# Revision 1.8  2006/12/02 01:04:58  anoop
# Ridiculously big ass commit.
# Also known as the week after thanksgiving 2006. Or "The day Anoop
# broke Rocks".
#
# Main Changes.
#
# 1. Added a roll-profile.mk file. This is meant as a makefile for building
# the profile rpm containing all the XML files meant for the roll. This is a
# breakaway from the spec.in file method of building the profile RPM.
#
# 2. The variable PWD is now changed to CURDIR. The main reason for this is
# PWD is supplied by the shell. CURDIR is the variable supplied by gmake itself.
# This means we can have a slightly more platform independant way of doing things.
# Also Solaris was failing to set PWD correctly in the source directories, wreaking
# havoc on the location of the BUILD and PKG directories.
#
# Revision 1.7  2006/09/19 21:02:05  anoop
# Now the web frontend for Ganglia builds from source code rather than from the ganglia-web RPM.
# This gives us better control over source code.
#
# Revision 1.6  2006/09/11 22:48:13  mjk
# monkey face copyright
#
# Revision 1.5  2006/08/23 20:36:47  anoop
# Upgraded Ganglia from 2.5.7 to 3.0.3
# Upgraded RRD Tool from 1.0.38 to 1.2.15
#
# Changes to the roll to adapt the roll to the upgrades.
#
# Revision 1.4  2006/08/10 00:10:30  mjk
# 4.2 copyright
#
# Revision 1.3  2006/07/22 02:08:09  bruno
# already fixed -- see the XML nodes files
#
# Revision 1.2  2006/07/21 19:39:25  anoop
# Bug fix. Now it starts gmond correctly.
#
# Revision 1.1  2006/07/18 18:15:35  bruno
# no longer build ganglia from SRPM -- build it from the tarball
#
# Revision 1.2  2006/01/16 16:35:13  mjk
# coreutils build
#
# Revision 1.1  2006/01/16 15:47:00  mjk
# more foundation for non-linux OSes
#

PKGROOT		= /opt/ganglia
REDHAT.ROOT     = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


install::
	mkdir -p $(ROOT)/$(PKGROOT)
	mkdir -p $(ROOT)/usr/share/man/man1
	mkdir -p $(ROOT)/usr/share/man/man5
	mkdir -p $(ROOT)/var/lib/ganglia/rrds/
	chown -R nobody:nobody  $(ROOT)/var/lib/ganglia/rrds/
	( 							\
		cd $(ARCHIVE)-$(VERSION);			\
		$(MAKE) install DESTDIR=$(ROOT);	 	\
	)
	(							\
		cd $(ARCHIVE)-$(VERSION)/gmond;			\
		gzip gmond.conf.5;				\
		cp gmond.conf.5.gz $(ROOT)/usr/share/man/man5;	\
	)
	(							\
		cd $(ARCHIVE)-$(VERSION)/mans;			\
		gzip *.1;					\
		cp *.1.gz $(ROOT)/usr/share/man/man1;		\
	)

clean::
	rm -rf $(ARCHIVE)-$(VERSION)
