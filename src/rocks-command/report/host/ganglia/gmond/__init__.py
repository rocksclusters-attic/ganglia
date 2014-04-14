# $Id: __init__.py,v 1.16 2013/01/16 00:07:00 clem Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 6.1.1 (Sand Boa)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
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
# $Log: __init__.py,v $
# Revision 1.16  2013/01/16 00:07:00  clem
# Fix for mixed-arch gmond.conf generation
#
# Tyler Trafford reported this patch.
#
# when generating the gmond.conf the command
# rocks report host ganglia gmond <host>
# should be check the arch of the host, not the frontend.
#
# http://marc.info/?l=npaci-rocks-discussion&m=135828393118619&w=2
#
# Revision 1.15  2012/11/27 00:48:59  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.14  2012/05/06 05:49:08  phil
# Copyright Storm for Mamba
#
# Revision 1.13  2011/07/27 21:46:47  anoop
# gmond.conf has too much whitespace. Cleaup
#
# Revision 1.12  2011/07/23 02:31:00  phil
# Viper Copyright
#
# Revision 1.11  2010/10/22 22:38:36  bruno
# tell client nodes to periodically resend their metadata.
#
# this catches the case where gmond on the frontend is started after gmond on
# a client node. in this case, gmond on the frontend has no metadata info
# from the client nodes and it has no way to get it (the client nodes are deaf).
#
# Revision 1.10  2010/09/07 23:53:19  bruno
# star power for gb
#
# Revision 1.9  2010/03/04 19:29:19  mjk
# - ganglia multicast address is now an attribute
# - default address switched from 244.0.0.4 to 244.0.0.3 (IANA Unassigned)
#   www.iana.org/assignments/multicast-addresses
#
# Revision 1.8  2009/11/20 01:06:51  bruno
# fix from Yurly in New Zealand.
#
# without this fix, if you restart gmond on the frontend, then it requires
# restarting gmond on all the compute nodes in order to get metrics to report
# again.
#
# Revision 1.7  2009/07/13 21:51:48  bruno
# one more tweak
#
# Revision 1.6  2009/07/10 20:32:05  bruno
# get rocks-defined metrics back in ganglia roll
#
# Revision 1.5  2009/06/30 00:08:56  bruno
# change ganglia traffic from multicast to unicast
#
# Revision 1.4  2009/06/15 18:12:18  bruno
# nuke some characters from the user input fields that may cause ganglia to
# not correctly gather and report metrics
#
# Revision 1.3  2009/05/01 19:07:17  mjk
# chimi con queso
#
# Revision 1.2  2009/04/28 23:28:09  bruno
# fixes
#
# Revision 1.1  2009/04/21 18:10:55  bruno
#  - converted gmond dbreport to rocks command line
#  - added supporting packages for ganglia monitor core
#
#

import rocks.commands

class Command(rocks.commands.report.host.ganglia.command):
	"""
	Report the configuration file that can be used for gmond.

	<example cmd='report host ganglia gmond'>
	Report the machines that are managed by SGE.
	</example>
	"""

	def cleanstr(self, dirty):
		clean = []

		for c in dirty:
			if c not in [ '<', '>', '&', '"' ]:
				clean.append(c)

		return '%s' % (''.join(clean))


	def run(self, params, args):
		hosts = self.getHostnames(args)

		#
		# only takes one host
		#
		if len(hosts) != 1:
			return

		host = hosts[0]
		mcastaddr = self.db.getHostAttr(host, 'ganglia_address')

		#
		# all non-frontend nodes are 'deaf'
		#
		frontends = self.getHostnames( [ 'frontend' ] )

		if host in frontends:
			deaf = 'no'
			send_metadata_interval = 0
		else:
			deaf = 'yes'
			send_metadata_interval = 180

		#
		# Get information about the cluster.
		#
		try:
			owner = self.cleanstr(self.db.getHostAttr(host,
				'Info_CertificateOrganization'))
		except:
			owner = "unspecified"

		try:
			clustername = self.cleanstr(self.db.getHostAttr(host,
				'Info_ClusterName'))
		except:
			clustername = "unspecified"

		try:
			url = self.db.getHostAttr(host, 'Info_ClusterURL')
		except:
			url = "unspecified"

		try:
			latlong = self.cleanstr(self.db.getHostAttr(host,
				'Info_ClusterLatlong'))
		except:
			latlong = "unspecified"

		#
		# Get the location of the machine in the cluster.
		# The cluster is assumed to be 2 dimensional.
		#
		try:
			rack = self.db.getHostAttr(host, 'rack')
			rank = self.db.getHostAttr(host, 'rank')
			plane = 0
			location = "%u,%u,%u" % (rack, rank, plane)
		except:
			location = "unspecified"

		#
		# get the private interface. ganglia sends its traffic on
		# this interface
		#
		rows = self.db.execute("""select net.device from networks net,
			nodes n, subnets s where n.name = '%s' and
			n.id = net.node and s.name = 'private' and
			s.id = net.subnet""" % (host))

		if rows == 1:
			eth_if, = self.db.fetchone()
		else:
			eth_if = 'eth0'

		#
		# more networking info
		#
		private_address = self.db.getHostAttr(host,
			'Kickstart_PrivateAddress')
		private_network = self.db.getHostAttr(host,
			'Kickstart_PrivateNetwork')
		private_netmask = self.db.getHostAttr(host,
			'Kickstart_PrivateNetmaskCIDR')

		self.beginOutput()

		#
		# output the gmond configuration
		#
		# the globals
		#
		self.addText( '/* Global Configuration */\n')
		self.addText( """globals {
	daemonize = yes
	setuid = yes
	user = nobody
	debug_level = 0
	max_udp_msg_len = 1472
	mute = no
	deaf = %s
	host_dmax = 0 /* secs */
	cleanup_threshold = 300 /* secs */
	gexec = no
	send_metadata_interval = %s /* secs */
}\n""" % (deaf, send_metadata_interval))

		self.addText( "\n/* Cluster Specific attributes */\n")
		self.addText( """cluster {
	name = "%s"
	owner = "%s"
	latlong = "%s"
	url = "%s"
}\n""" % (clustername, owner, latlong, url))

		self.addText( "\n/* Host configuration */")
		self.addText( """host {
	location="%s"
}\n""" % (location))

		self.addText( "\n/* UDP Channels for Send and Recv */")
		self.addText( """udp_recv_channel {
	mcast_join = %s
	port = 8649
}\n""" % (mcastaddr))

		if host in frontends:
			sendinfo = 'mcast_join = %s' % mcastaddr
		else:
			sendinfo = 'mcast_join = %s\n\thost = %s' % \
				(mcastaddr, private_address)

		self.addText( """udp_send_channel {
	%s
	port = 8649
}\n""" % (sendinfo))

		self.addText( "\n/* TCP Accept Channel */\n")
		self.addText( """tcp_accept_channel {
	port = 8649

	acl {
		default = "deny"

		access {
			ip = 127.0.0.1
			mask = 32
			action = "allow"
		}

		access {
			ip = %s
			mask = %s
			action = "allow"
		}
	}
}\n""" % (private_network, private_netmask))

		#
		# load the metrics modules
		#
		if self.db.getHostAttr(host, 'arch') == 'i386':
			libdir = 'lib'
		else:
			libdir = 'lib64'

		self.addText( "\n/* Modules */\n")
		self.addText( """modules {
	module {
		name = "core_metrics"
	}

	module {
		name = "cpu_module"
		path = "modcpu.so"
	}

	module {
		name = "disk_module"
		path = "moddisk.so"
	}

	module {
		name = "load_module"
		path = "modload.so"
	}

	module {
		name = "mem_module"
		path = "modmem.so"
	}

	module {
		name = "net_module"
		path = "modnet.so"
	}

	module {
		name = "proc_module"
		path = "modproc.so"
	}

	module {
		name = "sys_module"
		path = "modsys.so"
	}

	module {
		name = "python_module"
		path = "modpython.so"
		params = "/opt/ganglia/%s/ganglia/python_modules"
	}
}\n""" % libdir)

		# Now this is an important part. Metrics in ganglia 3.x follow
		# the collection group style of collecting metrics. Look at the
		# ganglia README to define your own metrics. For this we create
		# a list with all the metrics we want to list, and then create
		# a metrics array. Finally, we assign a default value_threshold
		# of 10% to each metric. This means, data is sent every time any
		# metric increases by 10%.

		metric_array = [
			'location',
			'load_one',
			'mem_total',
			'cpu_intr',
			'proc_run',
			'load_five',
			'disk_free',
			'mem_cached',
			'mtu',
			'cpu_sintr',
			'pkts_in',
			'bytes_in',
			'bytes_out',
			'swap_total',
			'mem_free',
			'load_fifteen',
			'boottime',
			'cpu_idle',
			'cpu_aidle',
			'cpu_user',
			'cpu_nice',
			'sys_clock',
			'mem_buffers',
			'cpu_system',
			'part_max_used',
			'disk_total',
			'heartbeat',
			'mem_shared',
			'machine_type',
			'cpu_wio',
			'proc_total',
			'cpu_num',
			'cpu_speed',
			'pkts_out',
			'swap_free'
		]

		self.addText( "\n/* Metrics Collection group */\n")
		self.addText( """collection_group {
	collect_every = 60
	time_threshold = 300\n""")

		for i in metric_array:
			self.addText( """\tmetric {
		name = "%s"
		value_threshold = 10.0
	}\n""" % (i.strip()))

		self.addText("""\tmetric{
		name = 'os_name'
	}\n""")
		self.addText("""\tmetric{
		name = 'os_release'
	}\n""")
		self.addText( "}\n")

		#
		# point gmond to the configuration files for the user-defined
		# metrics
		#
		self.addText(
			"\ninclude ('/opt/ganglia/etc/conf.d/*.pyconf')\n")

		self.endOutput()
